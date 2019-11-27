# 
#   P5_autoCorrelationTest.py
#   Auto Correlation Test
#
#   Created by Mohammed Ataa on 26/11/19.
#   Copyright © 2019 Ataago. All rights reserved.
# 
#   Write a program to show goodness of fit test using Autocorrelation test for the input set of random numbers. 
#   Assume Zα/2=1.96
#

from math import floor, sqrt
from random import random

# Generaing the random Digits for testing he goodness of fit (Independance property)
R = [round(random(), 2) for i in range(int(input("Enter Total number of random digis to be generated: ")))]
R = [
    0.12, 0.01, 0.23, 0.28, 0.89, 
    0.31, 0.64, 0.28, 0.83, 0.93, 
    0.99, 0.15, 0.33, 0.35, 0.91, 
    0.41, 0.60, 0.27, 0.75, 0.88, 
    0.68, 0.49, 0.05, 0.43, 0.95, 
    0.58, 0.19, 0.36, 0.69, 0.87
]

# Inputing Starting point, i & gap, m
i = int(input("Enter starting point to test Independance Property: i = "))
m = int(input("Enter the gap for each test data sample: m = "))
N = len(R) # total number of Random Digits

# Calculating M, where: i + (M + 1) * m <= N
M = int((N - i) / m - 1)

# Calculaing Rho = (1 / (M + 1)) * SIGMA(R[i + km] * R[i + (k+1)m]) - 0.25 , where: 0 <= k <= M
sum_ = 0
for k in range(M + 1):
    sum_ += (R[i + k*m - 1] * R[i + (k+1)*m - 1])
rho = sum_ / (M + 1) - 0.25

# Calculating sigma = root(13M + 7) / (12(M + 1))
sigma = (((13 * M) + 7) ** 0.5) / (12 * (M + 1))
Z0 = rho / sigma        # Calculating Z0 = rho / sigma

# printing the values
print("M: {}\nrho: {}\nsigma: {}\nZ0: {}\n" .format(M, rho, sigma, Z0))

Zcritical = float(input("Enter Z Critical Value: "))
if Z0 <= Zcritical:
    print('Hypothesis H0 is Accepted')
else:
    print('Hypothesis H0 is Rejected')