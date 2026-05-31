from __future__ import annotations

import copy

import numpy as np
import torch

from modules.deep_modules import Actor, Critic
from common.utils import get_flat_params, set_flat_params


class EvolutionModule:
    def __init__(
        self,
        obs_size: int,
        act_size: int,
        net: Critic,
        device: torch.device,
    ) -> None:
        self.obs_size = obs_size
        self.act_size = act_size
        self.net = net
        self.device = device

    def _clone_and_mutate(
        self,
        parent: Actor,
        mutation_std: float,
        mutation_prob: float,
        rng: np.random.Generator,
    ) -> Actor:
        child = copy.deepcopy(parent).to(self.device)
        flat_params = get_flat_params(child)
        noise = torch.zeros_like(flat_params)
        
        # Sparse fractional mutation: only mutate mutation_prob fraction of the weights
        mask = torch.from_numpy(rng.random(flat_params.numel()) < mutation_prob).to(
            flat_params.device
        )
        
        if mask.any():
            mutated_size = int(mask.sum().item())
            rands = rng.random(mutated_size)
            noise_values = torch.zeros(mutated_size, device=flat_params.device, dtype=flat_params.dtype)
            flat_params_mutated = flat_params[mask]
            
            # Super mutation (5% of mutated weights), Reset (5%), Normal mutation (90%)
            super_mut_mask = rands < 0.05
            reset_mask = (rands >= 0.05) & (rands < 0.10)
            normal_mut_mask = rands >= 0.10
            
            # 1. Normal mutation: proportional to parameter magnitude W
            if np.any(normal_mut_mask):
                normal_noise = torch.from_numpy(
                    rng.normal(0.0, mutation_std, size=int(normal_mut_mask.sum()))
                ).to(flat_params.device, dtype=flat_params.dtype)
                noise_values[normal_mut_mask] = normal_noise * flat_params_mutated[normal_mut_mask]
                
            # 2. Super mutation: 10x strength, proportional to parameter magnitude W
            if np.any(super_mut_mask):
                super_noise = torch.from_numpy(
                    rng.normal(0.0, 10.0 * mutation_std, size=int(super_mut_mask.sum()))
                ).to(flat_params.device, dtype=flat_params.dtype)
                noise_values[super_mut_mask] = super_noise * flat_params_mutated[super_mut_mask]
                
            # 3. Reset mutation: reset parameter to standard normal N(0, 1)
            if np.any(reset_mask):
                reset_noise = torch.from_numpy(
                    rng.normal(0.0, 1.0, size=int(reset_mask.sum()))
                ).to(flat_params.device, dtype=flat_params.dtype)
                noise_values[reset_mask] = reset_noise - flat_params_mutated[reset_mask]
                
            # Clamping parameters within hard limits to avoid explosion [-1e6, 1e6]
            new_params = torch.clamp(flat_params + noise.index_copy(0, torch.where(mask)[0], noise_values), -1e6, 1e6)
            set_flat_params(child, new_params, device=self.device)
        else:
            set_flat_params(child, flat_params, device=self.device)
            
        return child

    def evolve(
        self,
        population: list[Actor],
        fitnesses: list[float],
        mutation_std: float,
        mutation_prob: float,
        elite_ratio: float,
        surrogate_evaluation: bool = False,
    ) -> list[Actor]:
        if not population:
            return population

        del surrogate_evaluation

        rng = np.random.default_rng()
        ranked_indices = sorted(
            range(len(population)), key=lambda index: fitnesses[index], reverse=True
        )
        elite_count = max(1, int(len(population) * elite_ratio))
        elite_indices = ranked_indices[:elite_count]
        elites = [
            copy.deepcopy(population[index]).to(self.device) for index in elite_indices
        ]

        new_population: list[Actor] = elites.copy()
        while len(new_population) < len(population):
            parent = elites[int(rng.integers(0, len(elites)))]
            new_population.append(
                self._clone_and_mutate(
                    parent=parent,
                    mutation_std=mutation_std,
                    mutation_prob=mutation_prob,
                    rng=rng,
                )
            )

        return new_population[: len(population)]

    def sync_rl_to_pop(
        self,
        actor: Actor,
        population: list[Actor],
        fitnesses: list[float],
    ) -> None:
        if not population:
            return

        # Overwrite the worst individual in the population with the RL actor to protect the elites
        worst_index = int(np.argmin(fitnesses)) if fitnesses else 0
        population[worst_index].load_state_dict(copy.deepcopy(actor.state_dict()))
