import glob
import os
import re

import numpy as np
import pandas as pd
import scipy.stats as stats
from process_results import METHOD_LABELS, load_environment_data


def get_stable_final_values(env_id, merged_data):
    """
    Extracts the average of the last 10% of steps (from 900k to 1M total_steps)
    for each seed of each method.
    Returns: dict[method] = list of float values (one per seed)
    """
    stable_values = {}

    for method in merged_data:
        stable_values[method] = []
        for seed, df in merged_data[method].items():
            if "total_steps" not in df.columns:
                continue

            if "rl_reward" in df.columns and not df["rl_reward"].isna().all():
                y_metric = "rl_reward"
            elif "eval_reward" in df.columns and not df["eval_reward"].isna().all():
                y_metric = "eval_reward"
            else:
                continue

            max_steps = df["total_steps"].max()
            df_last_10 = df[df["total_steps"] >= max_steps * 0.9].dropna(
                subset=[y_metric]
            )

            if not df_last_10.empty:
                mean_val = df_last_10[y_metric].mean()
                stable_values[method].append(mean_val)

    return stable_values


def run_significance_tests(env_id, stable_values, base_dir="results"):
    """
    Implements Shapiro-Wilk test and Welch's t-test / Mann-Whitney U test significance pipeline.
    Saves GECCO-style LaTeX and CSV tables.
    """
    proposed_methods = ["sc_erl_ensemble", "sc_erl_dropout"]
    baselines = ["ppo", "td3", "ddpg", "erl", "sc_erl_random"]

    rows = []

    for ours in proposed_methods:
        group_A = stable_values.get(ours, [])
        if len(group_A) < 2:
            continue

        label_A = METHOD_LABELS.get(ours, ours)

        for base in baselines:
            group_B = stable_values.get(base, [])
            if len(group_B) < 2:
                continue

            label_B = METHOD_LABELS.get(base, base)
            comparison = f"{label_A} vs {label_B}"

            # 1. Shapiro-Wilk Normality Test (requires N >= 3)
            p_shapiro_A = np.nan
            p_shapiro_B = np.nan

            if len(group_A) >= 3:
                _, p_shapiro_A = stats.shapiro(group_A)
            if len(group_B) >= 3:
                _, p_shapiro_B = stats.shapiro(group_B)

            # If both are normal (p >= 0.05), use Welch's t-test, else use Mann-Whitney U
            # (If sample size < 3, we cannot test normality, so we safely default to non-parametric Mann-Whitney U)
            is_normal_A = pd.notna(p_shapiro_A) and (p_shapiro_A >= 0.05)
            is_normal_B = pd.notna(p_shapiro_B) and (p_shapiro_B >= 0.05)

            if is_normal_A and is_normal_B:
                test_name = "Welch's t-test"
                _, p_val = stats.ttest_ind(group_A, group_B, equal_var=False)
            else:
                test_name = "Mann-Whitney U"
                _, p_val = stats.mannwhitneyu(group_A, group_B, alternative="two-sided")

            # 2. Significance Asterisks Mapping
            if p_val < 0.001:
                sig = "***"
            elif p_val < 0.01:
                sig = "**"
            elif p_val < 0.05:
                sig = "*"
            else:
                sig = "ns"

            # Format Shapiro string
            shapiro_A_str = f"{p_shapiro_A:.4f}" if pd.notna(p_shapiro_A) else "N/A"
            shapiro_B_str = f"{p_shapiro_B:.4f}" if pd.notna(p_shapiro_B) else "N/A"
            shapiro_str = f"({shapiro_A_str}, {shapiro_B_str})"

            rows.append(
                {
                    "Zestawienie": comparison,
                    "Shapiro p-value (A, B)": shapiro_str,
                    "Wybrany Test (T-test / M-W)": test_name,
                    "Stat p-value": p_val,
                    "Istotność (Significance)": sig,
                }
            )

    df_tests = pd.DataFrame(rows)
    if df_tests.empty:
        return

    # Save CSV
    out_dir = os.path.join(base_dir, env_id)
    os.makedirs(out_dir, exist_ok=True)
    csv_out = os.path.join(out_dir, f"{env_id}_significance_table.csv")
    df_tests.to_csv(csv_out, index=False)

    # Save LaTeX Table (GECCO publication ready)
    latex_out = os.path.join(out_dir, f"{env_id}_significance_table.tex")
    # Format p-value float column beautifully in LaTeX
    df_latex = df_tests.copy()
    df_latex["Stat p-value"] = df_latex["Stat p-value"].apply(
        lambda x: f"{x:.4e}" if x < 1e-3 else f"{x:.4f}"
    )

    with open(latex_out, "w") as f:
        f.write(
            df_latex.to_latex(
                index=False,
                column_format="lcccc",
                caption=f"Statistical Significance testing for {env_id} based on Shapiro-Wilk normality checking and subsequent Welch's t-test / Mann-Whitney U test.",
                label=f"tab:sig_{env_id}",
            )
        )




def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = script_dir

    project_root = os.path.dirname(script_dir)
    output_base_dir = os.path.join(project_root, "results")

    eval_reward_dir = os.path.join(base_dir, "eval_reward")
    if not os.path.exists(eval_reward_dir):
        return

    env_files = glob.glob(os.path.join(eval_reward_dir, "*.csv"))
    if not env_files:
        return

    environments = [os.path.basename(f).replace(".csv", "") for f in env_files]

    for env_id in environments:
        merged_data = load_environment_data(env_id, base_dir)
        stable_values = get_stable_final_values(env_id, merged_data)
        run_significance_tests(env_id, stable_values, output_base_dir)


if __name__ == "__main__":
    main()
