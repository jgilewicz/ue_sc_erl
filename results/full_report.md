# Evolutionary Reinforcement Learning - Statistical & Performance Report
This report contains performance results, statistical significance tests, critic correlation tables, and experimental plots for five MuJoCo environments: HalfCheetah-v5, Hopper-v5, Walker2d-v5, Ant-v5, and Swimmer-v5.

---

## HalfCheetah-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | -457.266219 | 264.761374 | NaN | NaN |
| TD3 (Baseline) | 8605.390295 | 1518.866179 | NaN | NaN |
| DDPG (Baseline) | 3581.383093 | 1140.921777 | NaN | NaN |
| ERL (Baseline) | -592.583771 | 7.819637 | 717.419493 | 372.495983 |
| SC-ERL (Random) | -563.862256 | 37.487510 | 642.932279 | 536.578235 |
| SC-ERL (Ensemble) [Ours] | -148.034529 | 715.946410 | 19.415936 | 187.305613 |
| SC-ERL (Dropout) [Ours] | -284.378973 | 550.866854 | 415.020203 | 279.346387 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.0274, 0.0218) | Mann-Whitney U | 0.5556 | ns |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.0274, 0.8002) | Mann-Whitney U | 0.0286 | * |
| SC-ERL (Ensemble) [Ours] vs DDPG (Baseline) | (0.0274, 0.5070) | Mann-Whitney U | 0.0286 | * |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.0274, 0.7985) | Mann-Whitney U | 0.0571 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.0274, 0.4663) | Mann-Whitney U | 0.2857 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.0062, 0.0218) | Mann-Whitney U | 1.0000 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.0062, 0.8002) | Mann-Whitney U | 0.0159 | * |
| SC-ERL (Dropout) [Ours] vs DDPG (Baseline) | (0.0062, 0.5070) | Mann-Whitney U | 0.0159 | * |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.0062, 0.7985) | Mann-Whitney U | 0.1905 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.0062, 0.4663) | Mann-Whitney U | 0.3095 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 4 | 0.0882 | 0.2098 | 12 |
| Dropout Seed 4 | 0.4299 | 0.6000 | 6 |

### Performance & Analysis Plots


## Hopper-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | 353.559643 | 227.073417 | NaN | NaN |
| TD3 (Baseline) | 2143.328837 | 1519.513422 | NaN | NaN |
| DDPG (Baseline) | 1418.842284 | 860.844208 | NaN | NaN |
| ERL (Baseline) | 124.729524 | 54.116169 | 1008.271524 | 62.594008 |
| SC-ERL (Random) | 177.331425 | 6.363816 | 782.556184 | 364.330116 |
| SC-ERL (Ensemble) [Ours] | 263.433384 | 93.622375 | 224.079132 | 174.798428 |
| SC-ERL (Dropout) [Ours] | 207.291746 | 75.491578 | 1078.053495 | 65.630071 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.0067, 0.9908) | Mann-Whitney U | 0.1143 | ns |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.0067, 0.3313) | Mann-Whitney U | 0.0286 | * |
| SC-ERL (Ensemble) [Ours] vs DDPG (Baseline) | (0.0067, 0.5630) | Mann-Whitney U | 0.0159 | * |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.0067, 0.4396) | Mann-Whitney U | 0.0159 | * |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.0067, 0.7374) | Mann-Whitney U | 0.0571 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.1810, 0.9908) | Welch's t-test | 0.1283 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.1810, 0.3313) | Welch's t-test | 0.0027 | ** |
| SC-ERL (Dropout) [Ours] vs DDPG (Baseline) | (0.1810, 0.5630) | Welch's t-test | 4.9549e-04 | *** |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.1810, 0.4396) | Welch's t-test | 0.1888 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.1810, 0.7374) | Welch's t-test | 0.5285 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 3 | 0.0316 | 0.2321 | 41 |
| Dropout Seed 4 | 0.2212 | 0.5165 | 31 |

### Performance & Analysis Plots


## Walker2d-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | 27.069259 | 31.925635 | NaN | NaN |
| TD3 (Baseline) | 2851.569249 | 709.594877 | NaN | NaN |
| DDPG (Baseline) | 917.095678 | 791.538810 | NaN | NaN |
| ERL (Baseline) | 34.054841 | 33.425274 | 1020.933675 | 31.085440 |
| SC-ERL (Random) | 82.611756 | 8.082211 | -13.316697 | 8.671392 |
| SC-ERL (Ensemble) [Ours] | 104.380831 | 185.219505 | 672.414275 | 469.141303 |
| SC-ERL (Dropout) [Ours] | 165.628606 | 140.177565 | 706.746779 | 460.366561 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.1273, 0.8420) | Welch's t-test | 0.8821 | ns |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.1273, 0.6017) | Welch's t-test | 0.0021 | ** |
| SC-ERL (Ensemble) [Ours] vs DDPG (Baseline) | (0.1273, 0.4326) | Welch's t-test | 0.0692 | ns |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.1273, 0.1694) | Welch's t-test | 0.5103 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.1273, N/A) | Mann-Whitney U | 0.8000 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.8767, 0.8420) | Welch's t-test | 0.6504 | ns |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.8767, 0.6017) | Welch's t-test | 0.0036 | ** |
| SC-ERL (Dropout) [Ours] vs DDPG (Baseline) | (0.8767, 0.4326) | Welch's t-test | 0.0917 | ns |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.8767, 0.1694) | Welch's t-test | 0.1038 | ns |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.8767, N/A) | Mann-Whitney U | 0.8571 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 4 | -0.2384 | -0.0788 | 10 |
| Ensemble Seed 3 | -0.0418 | 0.2357 | 15 |
| Dropout Seed 4 | 0.7327 | 0.7455 | 10 |

### Performance & Analysis Plots


## Ant-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | -2729.268154 | 404.701950 | NaN | NaN |
| TD3 (Baseline) | 763.111900 | 779.365361 | NaN | NaN |
| DDPG (Baseline) | -798.391148 | 956.400760 | NaN | NaN |
| ERL (Baseline) | -2765.602147 | 374.944006 | 1061.007347 | 64.121252 |
| SC-ERL (Random) | 576.567754 | 250.838694 | 1004.289986 | 13.471997 |
| SC-ERL (Ensemble) [Ours] | 923.364248 | 40.340409 | 773.379149 | 424.541672 |
| SC-ERL (Dropout) [Ours] | 882.987292 | 19.404816 | 981.567389 | 10.987957 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.2365, 0.5235) | Welch's t-test | 4.2463e-04 | *** |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.2365, 0.4640) | Welch's t-test | 0.6781 | ns |
| SC-ERL (Ensemble) [Ours] vs DDPG (Baseline) | (0.2365, 0.0520) | Welch's t-test | 0.0112 | * |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.2365, 0.0597) | Welch's t-test | 2.5917e-04 | *** |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.2365, 0.5406) | Welch's t-test | 0.0684 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.7760, 0.5235) | Welch's t-test | 4.6278e-04 | *** |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.7760, 0.4640) | Welch's t-test | 0.7638 | ns |
| SC-ERL (Dropout) [Ours] vs DDPG (Baseline) | (0.7760, 0.0520) | Welch's t-test | 0.0124 | * |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.7760, 0.0597) | Welch's t-test | 2.8782e-04 | *** |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.7760, 0.5406) | Welch's t-test | 0.0918 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 4 | -0.6297 | -0.6000 | 6 |
| Ensemble Seed 3 | 0.4467 | 0.2143 | 7 |
| Dropout Seed 4 | 0.5463 | 0.4857 | 6 |

### Performance & Analysis Plots


## Swimmer-v5

### Performance Summary Table

| Algorithm/Method | Eval_Reward_Mean | Eval_Reward_Std | Best_Pop_Fitness_Mean | Best_Pop_Fitness_Std |
| --- | --- | --- | --- | --- |
| PPO (Baseline) | 63.865830 | 21.952593 | NaN | NaN |
| TD3 (Baseline) | 64.048997 | 15.600046 | NaN | NaN |
| DDPG (Baseline) | 75.927082 | 52.793025 | NaN | NaN |
| ERL (Baseline) | 13.582796 | 3.995288 | 94.631790 | 65.266922 |
| SC-ERL (Random) | 8.019728 | 9.659124 | 32.397844 | 27.866070 |
| SC-ERL (Ensemble) [Ours] | 16.538803 | 5.563690 | 27.630996 | 27.408690 |
| SC-ERL (Dropout) [Ours] | 25.995011 | 5.964231 | 27.951570 | 27.364570 |

### Statistical Significance Table

| Zestawienie | Shapiro p-value (A, B) | Wybrany Test (T-test / M-W) | Stat p-value | Istotność (Significance) |
| --- | --- | --- | --- | --- |
| SC-ERL (Ensemble) [Ours] vs PPO (Baseline) | (0.7256, 0.5748) | Welch's t-test | 0.0044 | ** |
| SC-ERL (Ensemble) [Ours] vs TD3 (Baseline) | (0.7256, 0.1450) | Welch's t-test | 0.0391 | * |
| SC-ERL (Ensemble) [Ours] vs DDPG (Baseline) | (0.7256, 0.2821) | Welch's t-test | 0.0166 | * |
| SC-ERL (Ensemble) [Ours] vs ERL (Baseline) | (0.7256, 0.3191) | Welch's t-test | 0.4506 | ns |
| SC-ERL (Ensemble) [Ours] vs SC-ERL (Random) | (0.7256, 0.2329) | Welch's t-test | 0.2652 | ns |
| SC-ERL (Dropout) [Ours] vs PPO (Baseline) | (0.2781, 0.5748) | Welch's t-test | 0.0094 | ** |
| SC-ERL (Dropout) [Ours] vs TD3 (Baseline) | (0.2781, 0.1450) | Welch's t-test | 0.0630 | ns |
| SC-ERL (Dropout) [Ours] vs DDPG (Baseline) | (0.2781, 0.2821) | Welch's t-test | 0.0270 | * |
| SC-ERL (Dropout) [Ours] vs ERL (Baseline) | (0.2781, 0.3191) | Welch's t-test | 0.0159 | * |
| SC-ERL (Dropout) [Ours] vs SC-ERL (Random) | (0.2781, 0.2329) | Welch's t-test | 0.0584 | ns |

### Critic Correlation Analysis

| Algorithm/Method | Pearson Correlation | Spearman Correlation | Sample Size (N) |
| --- | --- | --- | --- |
| Ensemble Seed 4 | 0.1502 | 0.3846 | 12 |
| Dropout Seed 4 | -0.1736 | -0.1758 | 10 |

### Performance & Analysis Plots


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

### Plots - Walker2d-v5
![Sample Efficiency - Walker2d-v5](./Walker2d-v5/Walker2d-v5_sample_efficiency.png)
![Surrogate Analysis - Walker2d-v5](./Walker2d-v5/Walker2d-v5_surrogate_analysis.png)
![Critic Correlation - Walker2d-v5](./Walker2d-v5/Walker2d-v5_critic_correlation.png)

---

### Plots - Ant-v5
![Sample Efficiency - Ant-v5](./Ant-v5/Ant-v5_sample_efficiency.png)
![Surrogate Analysis - Ant-v5](./Ant-v5/Ant-v5_surrogate_analysis.png)
![Critic Correlation - Ant-v5](./Ant-v5/Ant-v5_critic_correlation.png)

---

### Plots - Swimmer-v5
![Sample Efficiency - Swimmer-v5](./Swimmer-v5/Swimmer-v5_sample_efficiency.png)
![Surrogate Analysis - Swimmer-v5](./Swimmer-v5/Swimmer-v5_surrogate_analysis.png)
![Critic Correlation - Swimmer-v5](./Swimmer-v5/Swimmer-v5_critic_correlation.png)

---
