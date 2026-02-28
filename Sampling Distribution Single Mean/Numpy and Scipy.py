import numpy as np
from scipy import stats

data = np.array([6,5,4,5,7,6,5,4])
mu0 = 5
alpha = 0.05

n = len(data)
x_bar = np.mean(data)
s = np.std(data, ddof=1)

t = (x_bar - mu0) / (s / np.sqrt(n))
p_value = 2 * (1 - stats.t.cdf(abs(t), df=n-1))

t_critical = stats.t.ppf(0.975, df=n-1)
margin_error = t_critical * (s / np.sqrt(n))
lower = x_bar - margin_error
upper = x_bar + margin_error

if p_value < alpha:
    decision = "Reject_H0"
else:
    decision = "Fail_to_Reject_H0"

print("Sample Mean =", round(x_bar,4))
print("Sample Standard Deviation =", round(s,4))
print("t-Statistic =", round(t,4))
print("P-Value =", round(p_value,4))
print("Decision:", decision)
print("Confidence Interval = (", round(lower,4), ",", round(upper,4), ")")
