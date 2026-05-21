.DEFAULT_GOAL := help
ALGO ?= erl

.PHONY: help run clean run run-all clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

run: ## Run algorithm (ALGO=erl by default, e.g. make run ALGO=td3)
	uv run python entry_point.py algorithm=$(ALGO) $(ARGS)


run-all: ## Run TD3, ERL, SC-ERL and PPO for seeds 0,1,2
	for seed in 0 1 2; do \
		uv run python entry_point.py algorithm=td3 seed=$$seed wandb.name=td3_seed$$seed wandb.tags=[Pendulum,TD3,baseline]; \
		uv run python entry_point.py algorithm=erl seed=$$seed wandb.name=erl_seed$$seed wandb.tags=[Pendulum,ERL,baseline]; \
		uv run python entry_point.py algorithm=sc_erl seed=$$seed wandb.name=sc_erl_seed$$seed wandb.tags=[Pendulum,SC_ERL,baseline]; \
		uv run python entry_point.py algorithm=ppo seed=$$seed wandb.name=ppo_seed$$seed wandb.tags=[Pendulum,PPO,baseline]; \
	done

clean: ## Clean outputs and Hydra logs
	rm -rf outputs .hydra