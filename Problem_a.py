import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Define the parameters for the normal distributions
mu1, sigma1 = 0, 1
mu2, sigma2 = 175, 3

# Define the range of the x values
x_values = np.linspace(-10, 200, 1000)

# Calculate the probabilities
# P(x < 1 | N(0,1))
prob_x_lt_1 = stats.norm.cdf(1, loc=mu1, scale=sigma1)

# P(x > μ + 2σ | N(175, 3))
prob_x_gt_mu_plus_2sigma = 1 - stats.norm.cdf(mu2 + 2 * sigma2, loc=mu2, scale=sigma2)

# Plotting
plt.figure(figsize=(10, 8))

# Plot for PDF and CDF P(x < 1 | N(0,1))
plt.subplot(2, 2, 1)
plt.plot(x_values, stats.norm.pdf(x_values, loc=mu1, scale=sigma1), label='PDF: N(0,1)')
plt.fill_between(x_values, 0, stats.norm.pdf(x_values, loc=mu1, scale=sigma1), where=(x_values < 1), alpha=0.5, color='skyblue')
plt.axvline(x=1, color='r', linestyle='--', label='x=1')
plt.title('Probability Density Function')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x_values, stats.norm.cdf(x_values, loc=mu1, scale=sigma1), label='CDF: N(0,1)', color='orange')
plt.axvline(x=1, color='r', linestyle='--', label='x=1')
plt.title('Cumulative Distribution Function')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()

# Plot for PDF and CDF P(x > μ + 2σ | N(175, 3))
plt.subplot(2, 2, 2)
plt.plot(x_values, stats.norm.pdf(x_values, loc=mu2, scale=sigma2), label='PDF: N(175, 3)')
plt.fill_between(x_values, 0, stats.norm.pdf(x_values, loc=mu2, scale=sigma2), where=(x_values > mu2 + 2 * sigma2), alpha=0.5, color='lightgreen')
plt.axvline(x=mu2 + 2 * sigma2, color='r', linestyle='--', label='μ + 2σ')
plt.title('Probability Density Function')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_values, stats.norm.cdf(x_values, loc=mu2, scale=sigma2), label='CDF: N(175, 3)', color='orange')
plt.axvline(x=mu2 + 2 * sigma2, color='r', linestyle='--', label='μ + 2σ')
plt.title('Cumulative Distribution Function')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()

plt.tight_layout()
plt.show()

print("P(x < 1 | N(0,1)): ", prob_x_lt_1)
print("P(x > μ + 2σ | N(175, 3)): ", prob_x_gt_mu_plus_2sigma)
