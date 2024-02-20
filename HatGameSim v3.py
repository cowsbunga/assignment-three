import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns

finals = []
samples = 10000

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
        
c, loc, scale = st.weibull_min.fit(finals)

x1 = np.linspace(0, 2025)
plt.subplot(1, 1, 1)
sns.histplot(data = finals, bins=25, stat = "density")
plt.plot(x1, st.weibull_min.pdf(x1, c, loc, scale), 'r-', lw=5, alpha=0.6, label='weibull_min pdf')
plt.xlabel("Number on final piece of paper")

plt.show()

