# Evolutionary Reinforcement Learning - Statistical & Performance Report
This report contains performance results, statistical significance tests, critic correlation tables, and experimental plots for five environments: Ant-v5, HalfCheetah-v5, Hopper-v5, Swimmer-v5, and Walker2d-v5.

---

## Ant-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | -2929.695156 | 68.187998 | NaN | NaN |
| TD3 (Baseline) | 316.665515 | 565.056931 | NaN | NaN |
| ERL (Baseline) | -2685.618556 | 415.319470 | 1075.304213 | 70.291538 |
| SC-ERL (Random) | 571.475183 | 306.960046 | 1000.089054 | 12.897870 |
| SC-ERL (Ensemble) [Ours] | 918.116861 | 44.567152 | 731.246542 | 477.995604 |
| SC-ERL (Dropout) [Ours] | 871.528306 | 17.540499 | 981.652140 | 18.204854 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.6199, 0.3960) | Welch's t-test | 0.0011 | ** |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.6199, 0.1350) | Welch's t-test | 0.2992 | ns |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.6199, 0.3804) | Welch's t-test | 0.0041 | ** |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.6199, 0.4203) | Welch's t-test | 0.1879 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (N/A, 0.3960) | Mann-Whitney U | 0.2000 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (N/A, 0.1350) | Mann-Whitney U | 0.8000 | ns |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (N/A, 0.3804) | Mann-Whitney U | 0.2000 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (N/A, 0.4203) | Mann-Whitney U | 0.2000 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 4 | -0.6297 | -0.6000 | 6 |
| Ensemble Seed 3 | 0.4467 | 0.2143 | 7 |

### Performance & Analysis Plots


## HalfCheetah-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | -457.266219 | 264.761374 | NaN | NaN |
| TD3 (Baseline) | 7696.948604 | 1495.788210 | NaN | NaN |
| ERL (Baseline) | -593.861245 | 3.602062 | 885.797066 | 542.291115 |
| SC-ERL (Random) | -577.841875 | 23.893225 | 600.553601 | 609.848550 |
| SC-ERL (Ensemble) [Ours] | -567.266844 | 29.131802 | 85.037858 | 281.002658 |
| SC-ERL (Dropout) [Ours] | -166.905037 | 743.749035 | 377.004840 | 371.380051 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (N/A, 0.0218) | Mann-Whitney U | 0.8571 | ns |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (N/A, 0.3850) | Mann-Whitney U | 0.2000 | ns |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (N/A, N/A) | Mann-Whitney U | 0.3333 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (N/A, 0.4432) | Mann-Whitney U | 0.8000 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.0670, 0.0218) | Mann-Whitney U | 1.0000 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.0670, 0.3850) | Welch's t-test | 0.0018 | ** |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.0670, N/A) | Mann-Whitney U | 0.8000 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.0670, 0.4432) | Welch's t-test | 0.4396 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Dropout Seed 4 | 0.4299 | 0.6000 | 6 |

### Performance & Analysis Plots


## Hopper-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | 91.522345 | NaN | NaN | NaN |
| TD3 (Baseline) | 2143.328837 | 1519.513422 | NaN | NaN |
| ERL (Baseline) | 136.391958 | 54.753969 | 1027.966692 | 51.361614 |
| SC-ERL (Random) | 177.331425 | 6.363816 | 782.556184 | 364.330116 |
| SC-ERL (Ensemble) [Ours] | 277.720620 | 109.192367 | 221.485143 | 213.989166 |
| SC-ERL (Dropout) [Ours] | 207.291746 | 75.491578 | 1078.053495 | 65.630071 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.0979, 0.3313) | Welch's t-test | 0.0026 | ** |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.0979, 0.3038) | Welch's t-test | 0.1391 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.0979, 0.7374) | Welch's t-test | 0.2416 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.1810, 0.3313) | Welch's t-test | 0.0027 | ** |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.1810, 0.3038) | Welch's t-test | 0.2494 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.1810, 0.7374) | Welch's t-test | 0.5285 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 3 | 0.0316 | 0.2321 | 41 |
| Dropout Seed 4 | 0.2212 | 0.5165 | 31 |

### Performance & Analysis Plots


## Swimmer-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | 67.552439 | 23.493572 | NaN | NaN |
| TD3 (Baseline) | 67.891330 | 16.627117 | NaN | NaN |
| ERL (Baseline) | 13.582796 | 3.995288 | 94.631790 | 65.266922 |
| SC-ERL (Random) | 13.554995 | 1.662000 | 22.146178 | 30.371955 |
| SC-ERL (Ensemble) [Ours] | 18.849139 | 7.275829 | 26.707851 | 35.529032 |
| SC-ERL (Dropout) [Ours] | 24.316088 | 6.036999 | 19.863029 | 27.031141 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (N/A, 0.3959) | Mann-Whitney U | 0.1333 | ns |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (N/A, 0.5376) | Mann-Whitney U | 0.2000 | ns |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (N/A, 0.3191) | Mann-Whitney U | 0.8000 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (N/A, N/A) | Mann-Whitney U | 0.6667 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.9894, 0.3959) | Welch's t-test | 0.0357 | * |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.9894, 0.5376) | Welch's t-test | 0.1158 | ns |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.9894, 0.3191) | Welch's t-test | 0.0555 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.9894, N/A) | Mann-Whitney U | 0.2000 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Dropout Seed 4 | -0.1736 | -0.1758 | 10 |

### Performance & Analysis Plots


## Walker2d-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | 40.090607 | 31.955583 | NaN | NaN |
| TD3 (Baseline) | 1857.080942 | 1057.060374 | NaN | NaN |
| ERL (Baseline) | 34.054841 | 33.425274 | 1020.933675 | 31.085440 |
| SC-ERL (Random) | 51.673667 | 53.890233 | 293.549617 | 531.543415 |
| SC-ERL (Ensemble) [Ours] | 104.380831 | 185.219505 | 672.414275 | 469.141303 |
| SC-ERL (Dropout) [Ours] | 165.628606 | 140.177565 | 706.746779 | 460.366561 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.1273, N/A) | Mann-Whitney U | 0.5333 | ns |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.1273, 0.4586) | Welch's t-test | 0.1362 | ns |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.1273, 0.1694) | Welch's t-test | 0.5103 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.1273, 0.2029) | Welch's t-test | 0.6253 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.8767, N/A) | Mann-Whitney U | 0.8571 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.8767, 0.4586) | Welch's t-test | 0.1425 | ns |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.8767, 0.1694) | Welch's t-test | 0.1038 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.8767, 0.2029) | Welch's t-test | 0.1587 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 4 | -0.2384 | -0.0788 | 10 |
| Ensemble Seed 3 | -0.0418 | 0.2357 | 15 |
| Dropout Seed 4 | 0.7327 | 0.7455 | 10 |

### Performance & Analysis Plots


### Plots - Ant-v5
![Sample Efficiency - Ant-v5](./Ant-v5/Ant-v5_sample_efficiency.png)
![Surrogate Analysis - Ant-v5](./Ant-v5/Ant-v5_surrogate_analysis.png)
![Critic Correlation - Ant-v5](./Ant-v5/Ant-v5_critic_correlation.png)

---

### Plots - HalfCheetah-v5
![Sample Efficiency - HalfCheetah-v5](./HalfCheetah-v5/HalfCheetah-v5_sample_efficiency.png)
![Surrogate Analysis - HalfCheetah-v5](./HalfCheetah-v5/HalfCheetah-v5_surrogate_analysis.png)
![Critic Correlation - HalfCheetah-v5](./HalfCheetah-v5/HalfCheetah-v5_critic_correlation.png)

---

### Plots - Hopper-v5
![Sample Efficiency - Hopper-v5](./Hopper-v5/Hopper-v5_sample_efficiency.png)
![Surrogate Analysis - Hopper-v5](./Hopper-v5/Hopper-v5_surrogate_analysis.png)
![Critic Correlation - Hopper-v5](./Hopper-v5/Hopper-v5_critic_correlation.png)

---

### Plots - Swimmer-v5
![Sample Efficiency - Swimmer-v5](./Swimmer-v5/Swimmer-v5_sample_efficiency.png)
![Surrogate Analysis - Swimmer-v5](./Swimmer-v5/Swimmer-v5_surrogate_analysis.png)
![Critic Correlation - Swimmer-v5](./Swimmer-v5/Swimmer-v5_critic_correlation.png)

---

### Plots - Walker2d-v5
![Sample Efficiency - Walker2d-v5](./Walker2d-v5/Walker2d-v5_sample_efficiency.png)
![Surrogate Analysis - Walker2d-v5](./Walker2d-v5/Walker2d-v5_surrogate_analysis.png)
![Critic Correlation - Walker2d-v5](./Walker2d-v5/Walker2d-v5_critic_correlation.png)

---
