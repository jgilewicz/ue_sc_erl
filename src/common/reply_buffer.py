import torch
import numpy as np
from collections import deque
from collections import namedtuple

Transition = namedtuple(
    "Transition", ("state", "action", "reward", "next_state", "done")
)

PPOTransition = namedtuple(
    "PPOTransition", ("state", "action", "log_prob", "reward", "value", "done")
)


class Buffer:
    def __init__(
        self, capacity: int, batch_size: int, rng: np.random.Generator
    ) -> None:
        self.capacity = capacity
        self.batch_size = batch_size
        self.rng = rng
        self.buffer = deque(maxlen=capacity)

    def _make_transition(self, transition: Transition) -> Transition:
        return Transition(
            state=torch.tensor(transition.state, dtype=torch.float32),
            action=torch.tensor(transition.action, dtype=torch.float32),
            reward=torch.tensor(transition.reward, dtype=torch.float32),
            next_state=torch.tensor(transition.next_state, dtype=torch.float32),
            done=torch.tensor(np.asarray(transition.done), dtype=torch.float32),
        )

    def add(self, transition: Transition) -> None:
        self.buffer.append(self._make_transition(transition))

    def sample(self, batch_size: int = 32, latest: bool = False) -> list[Transition]:
        indices = np.arange(len(self.buffer))

        if latest:
            indices = np.arange(len(self.buffer) - batch_size, len(self.buffer))
        else:
            indices = self.rng.choice(len(self.buffer), batch_size, replace=False)

        batch = [self.buffer[i] for i in indices]

        return {
            "state": torch.stack([t.state for t in batch]),
            "action": torch.stack([t.action for t in batch]),
            "reward": torch.stack([t.reward for t in batch]).unsqueeze(-1),
            "next_state": torch.stack([t.next_state for t in batch]),
            "done": torch.stack([t.done for t in batch]).unsqueeze(-1),
        }

    def sample_latest(self, batch_size: int = None) -> list[Transition]:
        return self.sample(batch_size=batch_size, latest=True)

    def __len__(self) -> int:
        return len(self.buffer)


class RolloutBuffer:
    def __init__(self, capacity: int, device: torch.device) -> None:
        self.capacity = capacity
        self.device = device
        self.reset()

    def reset(self) -> None:
        self.states = []
        self.actions = []
        self.log_probs = []
        self.rewards = []
        self.values = []
        self.dones = []

    def add(self, transition: PPOTransition) -> None:
        self.states.append(torch.tensor(transition.state, dtype=torch.float32))
        self.actions.append(torch.tensor(transition.action, dtype=torch.float32))
        self.log_probs.append(torch.tensor(transition.log_prob, dtype=torch.float32))
        self.rewards.append(torch.tensor(transition.reward, dtype=torch.float32))
        self.values.append(torch.tensor(transition.value, dtype=torch.float32))
        self.dones.append(torch.tensor(np.asarray(transition.done), dtype=torch.float32))

    def compute_returns_and_advantages(self, last_value: float, gamma: float, gae_lambda: float) -> None:
        self.returns = []
        self.advantages = []

        gae = 0
        for step in reversed(range(len(self.rewards))):
            if step == len(self.rewards) - 1:
                next_non_terminal = 1.0
                next_value = last_value
            else:
                next_non_terminal = 1.0 - self.dones[step + 1]
                next_value = self.values[step + 1]

            delta = self.rewards[step] + gamma * next_value * next_non_terminal - self.values[step]
            gae = delta + gamma * gae_lambda * next_non_terminal * gae

            self.advantages.insert(0, gae)
            self.returns.insert(0, gae + self.values[step])

        self.states_t = torch.stack(self.states).to(self.device)
        self.actions_t = torch.stack(self.actions).to(self.device)
        self.log_probs_t = torch.stack(self.log_probs).to(self.device)
        self.returns_t = torch.stack(self.returns).to(self.device)
        self.advantages_t = torch.stack(self.advantages).to(self.device)

        # Normalize advantages
        self.advantages_t = (self.advantages_t - self.advantages_t.mean()) / (self.advantages_t.std() + 1e-8)

    def get_generator(self, minibatch_size: int):
        num_samples = len(self.states_t)
        indices = np.random.permutation(num_samples)

        for start in range(0, num_samples, minibatch_size):
            end = start + minibatch_size
            mb_indices = indices[start:end]

            yield {
                "state": self.states_t[mb_indices],
                "action": self.actions_t[mb_indices],
                "log_prob": self.log_probs_t[mb_indices],
                "return": self.returns_t[mb_indices],
                "advantage": self.advantages_t[mb_indices]
            }

    def __len__(self) -> int:
        return len(self.states)
