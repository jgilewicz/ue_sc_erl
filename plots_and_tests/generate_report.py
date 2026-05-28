import os
import re
import shutil


def parse_tex_table(filepath):
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} does not exist.")
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract rows between tabular environments
    tabular_match = re.search(
        r"\\begin{tabular}{.*?}(.*?)\\end{tabular}", content, re.DOTALL
    )
    if not tabular_match:
        print(f"Warning: Could not parse tabular block in {filepath}")
        return None

    tabular_content = tabular_match.group(1).strip()

    # Process lines
    lines = tabular_content.split("\n")
    rows = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Skip horizontal rules
        if (
            line.startswith("\\toprule")
            or line.startswith("\\midrule")
            or line.startswith("\\bottomrule")
            or line.startswith("\\hline")
        ):
            continue

        # Clean line endings
        clean_line = re.sub(r"\\\\(\s*\[.*?\])?", "", line).strip()
        # Unescape LaTeX characters
        clean_line = (
            clean_line.replace("\\%", "%")
            .replace("\\_", "_")
            .replace("\\&", "&")
            .replace("\\#", "#")
        )

        # Split columns
        cols = [c.strip() for c in clean_line.split("&")]
        if len(cols) > 0 and any(cols):
            rows.append(cols)

    if not rows:
        return ""

    headers = rows[0]
    data_rows = rows[1:]

    md_table = "| " + " | ".join(headers) + " |\n"
    md_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for r in data_rows:
        md_table += "| " + " | ".join(r) + " |\n"
    return md_table


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    results_dir = os.path.join(project_root, "results")

    environments = [
        "Ant-v5",
        "HalfCheetah-v5",
        "Hopper-v5",
        "Swimmer-v5",
        "Walker2d-v5",
    ]

    # Let's set up paths for workspace report
    workspace_report_path = os.path.join(results_dir, "full_report.md")

    # Let's set up paths for artifact report (brain directory)
    brain_dir = (
        "/Users/kuba/.gemini/antigravity-ide/brain/7050f68b-db2d-4da6-a245-3612cfba39bf"
    )
    brain_results_dir = os.path.join(brain_dir, "results")
    os.makedirs(brain_results_dir, exist_ok=True)
    brain_report_path = os.path.join(brain_dir, "full_report.md")

    # Header of the report
    md_content = """# Evolutionary Reinforcement Learning - Statistical & Performance Report
This report contains performance results, statistical significance tests, critic correlation tables, and experimental plots for five environments: Ant-v5, HalfCheetah-v5, Hopper-v5, Swimmer-v5, and Walker2d-v5.

---
"""

    for env in environments:
        env_dir = os.path.join(results_dir, env)
        print(f"Processing {env}...")

        md_content += f"\n## {env}\n\n"

        # 1. Summary Table
        summary_tex = os.path.join(env_dir, f"{env}_summary_table.tex")
        if os.path.exists(summary_tex):
            md_content += "### Performance Summary Table\n\n"
            summary_md = parse_tex_table(summary_tex)
            if summary_md:
                md_content += summary_md + "\n"

        # 2. Significance Table
        sig_tex = os.path.join(env_dir, f"{env}_significance_table.tex")
        if os.path.exists(sig_tex):
            md_content += "### Statistical Significance Table\n\n"
            sig_md = parse_tex_table(sig_tex)
            if sig_md:
                md_content += sig_md + "\n"

        # 3. Critic Correlation Table
        corr_tex = os.path.join(env_dir, f"{env}_critic_correlation.tex")
        if os.path.exists(corr_tex):
            md_content += "### Critic Correlation Analysis\n\n"
            corr_md = parse_tex_table(corr_tex)
            if corr_md:
                md_content += corr_md + "\n"

        # 4. Plots (Sample Efficiency, Surrogate Analysis, Critic Correlation)
        md_content += "### Performance & Analysis Plots\n\n"

        plot_names = [
            ("Sample Efficiency", f"{env}_sample_efficiency.png"),
            ("Surrogate Analysis", f"{env}_surrogate_analysis.png"),
            ("Critic Correlation", f"{env}_critic_correlation.png"),
        ]

        # For workspace report we use relative paths: ./Ant-v5/Ant-v5_sample_efficiency.png
        # For brain report we will copy images to brain folder and use absolute/relative paths

        # Let's ensure the folder exists in brain_results
        brain_env_dir = os.path.join(brain_results_dir, env)
        os.makedirs(brain_env_dir, exist_ok=True)

        for caption, filename in plot_names:
            src_img = os.path.join(env_dir, filename)
            if os.path.exists(src_img):
                # Copy to brain dir so it displays in Gemini Artifact
                dst_img = os.path.join(brain_env_dir, filename)
                shutil.copy2(src_img, dst_img)

                # We will write the workspace report with relative paths
                # But wait, we can just write the workspace report to disk, and the brain report to disk!
                # Actually, they can be identical if the images are copied.

        # Let's write the markdown image lines
        # In results/full_report.md, relative path is: ./{env}/{env}_sample_efficiency.png
        # In brain/full_report.md, relative path is: ./results/{env}/{env}_sample_efficiency.png

    # Write Workspace report
    workspace_md = md_content
    for env in environments:
        # replace placeholder/relative references
        pass

    # Let's write a custom generator for both files
    # Workspace file
    ws_content = md_content
    for env in environments:
        ws_content += f"\n### Plots - {env}\n"
        ws_content += (
            f"![Sample Efficiency - {env}](./{env}/{env}_sample_efficiency.png)\n"
        )
        ws_content += (
            f"![Surrogate Analysis - {env}](./{env}/{env}_surrogate_analysis.png)\n"
        )
        ws_content += (
            f"![Critic Correlation - {env}](./{env}/{env}_critic_correlation.png)\n"
        )
        ws_content += "\n---\n"

    with open(workspace_report_path, "w", encoding="utf-8") as f:
        f.write(ws_content)
    print(f"Saved workspace report to {workspace_report_path}")

    # Brain Artifact file
    brain_content = md_content
    for env in environments:
        brain_content += f"\n### Plots - {env}\n"
        brain_content += f"![Sample Efficiency - {env}](/Users/kuba/.gemini/antigravity-ide/brain/7050f68b-db2d-4da6-a245-3612cfba39bf/results/{env}/{env}_sample_efficiency.png)\n"
        brain_content += f"![Surrogate Analysis - {env}](/Users/kuba/.gemini/antigravity-ide/brain/7050f68b-db2d-4da6-a245-3612cfba39bf/results/{env}/{env}_surrogate_analysis.png)\n"
        brain_content += f"![Critic Correlation - {env}](/Users/kuba/.gemini/antigravity-ide/brain/7050f68b-db2d-4da6-a245-3612cfba39bf/results/{env}/{env}_critic_correlation.png)\n"
        brain_content += "\n---\n"

    with open(brain_report_path, "w", encoding="utf-8") as f:
        f.write(brain_content)
    print(f"Saved brain report to {brain_report_path}")


if __name__ == "__main__":
    main()
