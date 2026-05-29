import torch
import torch.nn as nn
import numpy as np
import copy
import random

from .utils import get_flat_params, set_flat_params


class EvolutionModule:
    def __init__(
        self,
        obs_size: int,
        act_size: int,
        net: nn.Module,
        device: torch.device = "cpu",
    ) -> None:
        self.obs_size = obs_size
        self.act_size = act_size
        self.critic_net = net
        self.device = device

        self.best_actor = None
        self.best_fitness = float("-inf")

    def _crossover(
        self, p_a: nn.Module, p_b: nn.Module, crossover_rate: float = 0.5
    ) -> nn.Module:
        params_a = get_flat_params(p_a)
        params_b = get_flat_params(p_b)

        mask = torch.rand_like(params_a) < crossover_rate
        child_params = torch.where(mask, params_a, params_b)

        child = copy.deepcopy(p_a).to(self.device)
        set_flat_params(child, child_params, self.device)
        return child

    def _mutate(
        self, model: nn.Module, mutation_rate: float = 0.01, mutation_prob: float = 0.1
    ) -> nn.Module:
        with torch.no_grad():
            for param in model.parameters():
                mask = torch.rand_like(param) < mutation_prob
                noise = torch.randn_like(param) * mutation_rate
                param.add_(mask.float() * noise)
        return model

    def _crossover_blended(
        self, p_a: nn.Module, p_b: nn.Module, alpha: float = 0.5
    ) -> nn.Module:
        child = copy.deepcopy(p_a).to(self.device)
        with torch.no_grad():
            for param_c, param_b in zip(child.parameters(), p_b.parameters()):
                param_c.data.copy_(alpha * param_c.data + (1.0 - alpha) * param_b.data)
        return child

    def mutate(
        self, net: nn.Module, mutation_prob: float = 0.9, mutation_strength: float = 0.1
    ) -> nn.Module:
        with torch.no_grad():
            for param in net.parameters():
                if len(param.shape) == 1:
                    continue

                mask = (torch.rand_like(param) < mutation_prob).float()
                noise = torch.randn_like(param) * mutation_strength
                param.add_(mask * noise)
        return net

    def sync_rl_to_pop(self, rl_actor: nn.Module, population: list, fitnesses: list):
        if not population or not fitnesses:
            return

        worst_idx = np.argmin(fitnesses)
        population[worst_idx].load_state_dict(rl_actor.state_dict())

    def evolve(
        self,
        population: list[nn.Module],
        fitnesses: list[float],
        mutation_std: float = 0.05,
        mutation_prob: float = 0.5,
        elite_ratio: float = 0.5,
        surrogate_evaluation: bool = False,
    ) -> list[nn.Module]:
        if not fitnesses or not population:
            return population

        elite_count = max(1, int(len(population) * elite_ratio))
        ranked_indices = np.argsort(fitnesses)[::-1]
        elites = [population[i] for i in ranked_indices[:elite_count]]

        best_fitness = max(fitnesses)

        if best_fitness > self.best_fitness and not surrogate_evaluation:
            self.best_fitness = best_fitness
            self.best_actor = copy.deepcopy(elites[0]).to(self.device)

        protected_elites = []
        if surrogate_evaluation and self.best_actor is not None:
            protected_elites.append(copy.deepcopy(self.best_actor).to(self.device))
            for e in elites:
                if len(protected_elites) < elite_count:
                    protected_elites.append(copy.deepcopy(e).to(self.device))
        else:
            for e in elites:
                protected_elites.append(copy.deepcopy(e).to(self.device))

        new_population = protected_elites[:elite_count]

        crossover_pool = list(elites)
        if surrogate_evaluation and self.best_actor is not None:
            crossover_pool.append(self.best_actor)

        while len(new_population) < len(population):
            if len(crossover_pool) >= 2:
                parent_a, parent_b = random.sample(crossover_pool, 2)
            else:
                parent_a, parent_b = crossover_pool[0], crossover_pool[0]

            parent_a.to(self.device)
            parent_b.to(self.device)

            child = self._crossover_blended(parent_a, parent_b, alpha=0.5)
            child = self.mutate(
                child, mutation_prob=mutation_prob, mutation_strength=mutation_std
            )
            new_population.append(child)

        return new_population
