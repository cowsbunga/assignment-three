import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm
import seaborn as sns

finals = []
samples = 1 0000

rng = np.random.default_rng()

for i in range(samples):
    hat = list(range(1, 2025))
    for j in range(2024, 1, -1):
        a = rng.integers(0, j)
        a_val = hat[a]
        hat.pop(a)
        b = rng.integers(0, j-1)
        b_val = hat[b]
        hat.pop(b)
        hat.append(abs(a_val - b_val))
    finals.append(hat[0])
        


x1 = np.linspace(0, 2025)

sns.histplot(data = finals, bins=25)

plt.xlabel("Number on final piece of paper")

plt.show()

