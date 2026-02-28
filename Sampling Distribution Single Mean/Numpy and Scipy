import numpy as np
from scipy import stats
data=np.array([6,5,4,5,7,6,5,4])
mu0=5
n=len(data)
x_bar=np.mean(data)
s=np.std(data.ddof=1)
z=(xbar-mu0)/(s/np.sqrt(n))
p_value=2*(1-stats.norm.cdf(abs(z)))
z_critical=stats.norm.ppf(0.975)
margin_error=z_critical*(s/np.sqrt(n))
lower=x_bar-margin_error
upper=x_bar+margin_error
alpha=0.5
if p_value<alpha:
    decision="Reject_H0"
else:
     decision="Accept_H0"
print("Sample_Mean=",round(x_bar,4))
