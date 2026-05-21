# Gemini AI Context

This project explores **Uncertainty-Aware Surrogate Fitness in Evolutionary Reinforcement Learning**.

## Architecture & Core Components

- **`entry_point.py`**: The main script for execution. It handles environment setup, Weights & Biases (wandb) initialization, and running the specified algorithm.
- **`src/`**: Contains the source code of the algorithms and shared utilities.
  - **`common/`**: Shared components like reply buffers, modules, wandb logger, surrogate controller, etc.
  - **`TD3/`, `ERL/`, `SC_ERL/`, `PPO/`**: Implementations of each algorithm.
- **`configs/`**: Configuration management using `Hydra`. 
  - The main configuration is `config.yaml`.
  - Algorithm-specific parameter files are under `configs/algorithm/`.
- **`outputs/`**: Generated outputs, logs, and artifacts (ignored by git).

## Tooling & Environment

- **Python**: Requires Python 3.12+.
- **Dependency Management**: Uses `uv`.
  - Install/Sync dependencies: `uv sync`
  - Run scripts: `uv run python <script>`
- **Task Runners**: 
  - `Taskfile.yml` (`task`) is preferred for complex, multi-environment or matrix runs (e.g., `run-fetch-matrix`).
  - `Makefile` (`make`) provides simpler commands (`make run`, `make run-all`, `make clean`).
- **Logging**: Supervised via `Weights & Biases` (`wandb`). Disabled by default. Can be enabled by overriding `wandb.enabled=true`.

## Conventions

1. Always use `uv run python` when executing Python scripts to ensure the environment dependencies are respected.
2. Configuration changes should be made carefully inside `configs/`. Use Hydra syntax for overrides (e.g., `env.id=Pendulum-v1 wandb.enabled=true`).
3. Add new experimental pipelines to `Taskfile.yml` since it handles bash loops and conditionals more gracefully than `Makefile`.
4. Do not alter the core architecture (`src/`) unless explicitly requested. 
5. When adding dependencies, keep `pyproject.toml` and `uv.lock` synchronized by using `uv add <package>`.

## Common Commands

- Run default algorithm (ERL): `uv run python entry_point.py`
- Run specific algorithm: `uv run python entry_point.py algorithm=td3`
- Run matrix on Fetch environments: `task run-fetch-matrix`
- Clean outputs: `task clean` or `make clean`
