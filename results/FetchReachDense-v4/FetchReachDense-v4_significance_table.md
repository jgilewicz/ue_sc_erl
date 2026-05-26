# Statistical Significance Testing - FetchReachDense-v4

Normality check via Shapiro-Wilk (alpha=0.05). Comparison uses Welch's t-test (if normal) or Mann-Whitney U (if non-normal).

| Zestawienie                                 | Shapiro p-value (A, B)   | Wybrany Test (T-test / M-W)   |   Stat p-value | Istotność (Significance)   |
|:--------------------------------------------|:-------------------------|:------------------------------|---------------:|:---------------------------|
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline)  | (0.2599, 0.4846)         | Welch's t-test                |     0.00700304 | **                         |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline)  | (0.2599, 0.9741)         | Welch's t-test                |     0.00111954 | **                         |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline)  | (0.2599, 0.0256)         | Mann-Whitney U                |     0.4        | ns                         |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.2599, N/A)            | Mann-Whitney U                |     0.8        | ns                         |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline)   | (N/A, 0.4846)            | Mann-Whitney U                |     0.0952381  | ns                         |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline)   | (N/A, 0.9741)            | Mann-Whitney U                |     0.0952381  | ns                         |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline)   | (N/A, 0.0256)            | Mann-Whitney U                |     0.2        | ns                         |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random)  | (N/A, N/A)               | Mann-Whitney U                |     0.333333   | ns                         |
