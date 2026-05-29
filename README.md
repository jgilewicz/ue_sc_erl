# Uncertainty-Aware Surrogate Fitness in Evolutionary Reinforcement Learning
Research project for comparing reinforcement learning and evolutionary reinforcement learning algorithms.

The repository currently includes implementations of:

- `TD3`
- `ERL`
- `SC_ERL`
- `PPO`
- `DDPG`

## Project Goal

The goal of this project is to run and compare selected algorithms under a shared experimental setup.
The code uses `Hydra` for configuration management and optionally `Weights & Biases` for experiment logging.

## Requirements

- Python `3.12+`
- `uv`

## Installation

Install dependencies:

```bash
uv sync
```

Run commands inside the project environment:

```bash
uv run python entry_point.py
```

## Running Experiments

The default algorithm is defined in `configs/config.yaml`.

Run with `Makefile`:

```bash
make run
```

Run a specific algorithm:

```bash
make run ALGO=td3
make run ALGO=erl
make run ALGO=sc_erl
make run ALGO=ppo
```

Run with custom Hydra arguments:

```bash
make run ALGO=td3 ARGS="seed=0 env.id=Pendulum-v1"
```

Run all basic experiments from the `Makefile`:

```bash
make run-all
```

Run parallel experiment matrix with `Taskfile` (`task`):

You can run the full MuJoCo fallback experiment matrix (including seeds `0-4`, and algorithms `sc_erl` in dropout/ensemble/random modes, `td3`, `erl`, `ppo`, and `ddpg`) in parallel using:

```bash
task run-mujoco-parallel
```

Alternatively, to run **only the evolutionary algorithms** (ERL and SC-ERL dropout/ensemble/random, without other baselines), use:

```bash
task run-mujoco-parallel-evo
```

To run only the evolutionary algorithms **sequentially** (one by one, to prevent MacBook overheating/throttling):

```bash
task run-mujoco-sequential-evo
```

## Configuration

The main configuration file is:

- `configs/config.yaml`

Algorithm-specific configurations are stored in:

- `configs/algorithm/td3.yaml`
- `configs/algorithm/erl.yaml`
- `configs/algorithm/sc_erl.yaml`
- `configs/algorithm/ppo.yaml`
- `configs/algorithm/ddpg.yaml`

Example configuration parameters:

- `seed` - random seed
- `device` - compute device, for example `auto`
- `env.id` - training environment
- `eval_env.id` - evaluation environment
- `wandb.enabled` - enables Weights & Biases logging

## Experiment Logging

Logging to `wandb` is disabled by default.

To enable it, run:

```bash
make run ARGS="wandb.enabled=true wandb.name=test_run"
```

If you use a `.env` file, make sure `WANDB_API_KEY` is set.

## Project Structure

```text
.
├── configs/             # Hydra configuration
├── src/
│   ├── common/          # shared modules and utilities
│   ├── TD3/             # TD3 implementation
│   ├── ERL/             # ERL implementation
│   ├── SC_ERL/          # SC-ERL implementation
│   ├── PPO/             # PPO implementation
│   └── DDPG/            # DDPG implementation
├── entry_point.py       # main entry point
├── pyproject.toml       # project metadata and dependencies
├── Makefile             # Makefile helper commands
└── Taskfile.yml         # Task runner for parallel matrices and pipelines
```

## Outputs and Artifacts

Run artifacts are stored in the `outputs/` directory.
This directory is ignored by `.gitignore`.
