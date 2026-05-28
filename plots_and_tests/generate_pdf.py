import os
import re
from fpdf import FPDF


def translate_header_to_polish(header):
    header = header.strip()
    translations = {
        "Algorithm/Method": "Metoda / Algorytm",
        "Eval_Reward_Mean": "Średnia Nagroda Ew.",
        "Eval_Reward_Std": "Odch. Std Nagrody Ew.",
        "Best_Pop_Fitness_Mean": "Śr. Najlepsza Sprawność",
        "Best_Pop_Fitness_Std": "Odch. Std Sprawności",
        "Pearson Correlation": "Korelacja Persona",
        "Spearman Correlation": "Korelacja Spearmana",
        "Sample Size (N)": "Rozmiar Próbki (N)",
    }
    return translations.get(header, header)


def parse_tex_table_to_data(filepath):
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
            # Translate headers if first row
            if not rows:
                cols = [translate_header_to_polish(c) for c in cols]
            rows.append(cols)

    return rows


class ERLReportPDF(FPDF):
    def header(self):
        self.set_y(10)
        self.set_font("Arial", "B", 8)
        self.set_text_color(120, 120, 120)  # Soft Gray
        self.cell(
            0,
            5,
            "EWOLUCYJNE UCZENIE ZE WZMOCNIENIEM - RAPORT STATYSTYCZNY I WYNIKI",
            border=0,
            align="L",
        )
        self.set_x(15)
        self.cell(0, 5, "PODSUMOWANIE DOŚWIADCZEŃ", border=0, align="R")
        self.ln(5)
        self.set_draw_color(220, 220, 220)  # Very light divider line
        self.line(15, 16, 195, 16)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(160, 160, 160)
        self.cell(0, 10, f"Strona {self.page_no()}/{{nb}}", align="C")

    def section_title(self, label):
        self.set_font("Arial", "B", 15)
        self.set_text_color(0, 0, 0)  # Black
        self.cell(0, 10, label, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def subsection_title(self, label):
        self.set_font("Arial", "B", 10.5)
        self.set_text_color(80, 80, 80)  # Dark Gray
        self.cell(0, 8, label, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def draw_data_table(self, rows):
        if not rows:
            return

        self.set_font("Arial", size=8)
        self.set_text_color(0, 0, 0)

        with self.table(
            borders_layout="HORIZONTAL_LINES",
            cell_fill_color=(255, 255, 255),
            cell_fill_mode="ROWS",
            line_height=5.5,
        ) as table:
            # Header Row
            header_row = table.row()
            self.set_font("Arial", "B", 8)
            self.set_text_color(0, 0, 0)
            # No fill color (white header)
            for col in rows[0]:
                header_row.cell(col)

            # Data Rows
            self.set_font("Arial", size=7.5)
            self.set_text_color(50, 50, 50)
            for row in rows[1:]:
                data_row = table.row()
                for item in row:
                    data_row.cell(item)
        self.ln(4)


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

    pdf = ERLReportPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(15, 20, 15)

    # ------------------ ADD UNICODE FONTS ------------------
    pdf.add_font("Arial", "", "/System/Library/Fonts/Supplemental/Arial.ttf")
    pdf.add_font("Arial", "B", "/System/Library/Fonts/Supplemental/Arial Bold.ttf")
    pdf.add_font("Arial", "I", "/System/Library/Fonts/Supplemental/Arial Italic.ttf")
    pdf.add_font(
        "Arial", "BI", "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
    )

    pdf.alias_nb_pages()

    # ------------------ COVER PAGE ------------------
    pdf.add_page()
    pdf.ln(45)
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(
        0,
        12,
        "Ewolucyjne Uczenie ze Wzmocnieniem",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
    )
    pdf.cell(
        0,
        12,
        "Raport z Wyników Doświadczalnych",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
    )

    pdf.ln(10)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.5)
    pdf.line(55, pdf.get_y(), 155, pdf.get_y())

    pdf.ln(15)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(
        0,
        10,
        "Analiza Istotności Statystycznej i Metryk Wydajności",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
    )

    pdf.ln(50)
    pdf.set_font("Arial", "", 9.5)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 5, "Analizowane środowiska:", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("Arial", "B", 10.5)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, ", ".join(environments), new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.ln(30)
    pdf.set_font("Arial", "I", 8.5)
    pdf.set_text_color(140, 140, 140)
    pdf.cell(
        0,
        5,
        "Raport zawiera wyłącznie czyste dane i wykresy, bez wniosków i interpretacji.",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
    )

    # ------------------ ENVIRONMENT PAGES ------------------
    for env in environments:
        env_dir = os.path.join(results_dir, env)
        print(f"Dodawanie środowiska {env} do PDF...")

        # Page 1: Tables
        pdf.add_page()
        pdf.section_title(f"Środowisko: {env}")

        # 1. Performance Summary
        summary_tex = os.path.join(env_dir, f"{env}_summary_table.tex")
        if os.path.exists(summary_tex):
            pdf.subsection_title("Tabela Podsumowująca Wyniki")
            summary_data = parse_tex_table_to_data(summary_tex)
            if summary_data:
                pdf.draw_data_table(summary_data)

        # 2. Statistical Significance
        sig_tex = os.path.join(env_dir, f"{env}_significance_table.tex")
        if os.path.exists(sig_tex):
            pdf.subsection_title("Tabela Istotności Statystycznej")
            sig_data = parse_tex_table_to_data(sig_tex)
            if sig_data:
                pdf.draw_data_table(sig_data)

        # 3. Critic Correlation Analysis
        corr_tex = os.path.join(env_dir, f"{env}_critic_correlation.tex")
        if os.path.exists(corr_tex):
            pdf.subsection_title("Analiza Korelacji Krytyka")
            corr_data = parse_tex_table_to_data(corr_tex)
            if corr_data:
                pdf.draw_data_table(corr_data)

        # Page 2: Plots
        pdf.add_page()
        pdf.section_title(f"{env} - Wykresy Wyników i Analizy")
        pdf.ln(5)

        # 1. Sample Efficiency Curve (Centered, wide)
        eff_img = os.path.join(env_dir, f"{env}_sample_efficiency.png")
        if os.path.exists(eff_img):
            pdf.subsection_title("1. Krzywa Wydajności Próbkowej")
            y_before = pdf.get_y()
            pdf.image(eff_img, x=25, y=y_before, w=160, h=95)
            pdf.set_y(y_before + 98)
            pdf.ln(5)

        # 2. Surrogate Analysis & Critic Correlation side-by-side
        surr_img = os.path.join(env_dir, f"{env}_surrogate_analysis.png")
        corr_img = os.path.join(env_dir, f"{env}_critic_correlation.png")

        y_plots = pdf.get_y()
        if os.path.exists(surr_img):
            pdf.set_xy(15, y_plots)
            pdf.subsection_title("2. Analiza Niepewności Surogatu")
            pdf.image(surr_img, x=15, y=pdf.get_y(), w=85, h=55)

        if os.path.exists(corr_img):
            pdf.set_xy(110, y_plots)
            pdf.subsection_title("3. Wykres Korelacji Krytyka")
            pdf.image(corr_img, x=110, y=pdf.get_y(), w=85, h=55)

    pdf_output_path = os.path.join(project_root, "full_report.pdf")
    pdf.output(pdf_output_path)
    print(f"Pomyślnie wygenerowano raport PDF pod adresem: {pdf_output_path}")


if __name__ == "__main__":
    main()
