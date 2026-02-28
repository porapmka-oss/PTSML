import math
data=[6,5,4,5,7,6,5,4]
n=len(data)
mu0=5
x_bar=sum(data)/n
variance=sum((x-x_bar)**2 for x in data)/(n-1)
s=math.sqrt(variance)
z=(x_bar-mu0)/(s/math.sqrt(n))
z_critical=1.96
if abs(z) < z_critical:
    print("Accept_H0")
else:
    print("Reject_H0")
margin_error=z_critical*(s/math.sqrt(n))
lower=x_bar-margin_error
upper=x_bar+margin_error
print("Sample Mean=",round(x_bar,4))
print("Sample_Standard_Deviation=",round(s,4))
print("Z_statistic=",round(z,4))
print("Confidence_interval=",round(lower,4),',',round(upper,4),')')
