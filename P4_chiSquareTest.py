# 
#   P4_chiSquareTest.py
#   Chi Square Test
#
#   Created by Mohammed Ataa on 26/11/19.
#   Copyright © 2019 Ataago. All rights reserved.
# 
#   Write a program to show goodness of fit test using Chi-Square Test 
#   for the input set of random numbers. Assume significance value is equal to 0.05. 
#   Dcritical = 16.9
#

from random import random

# Random Digits
RD = [round(random(), 2) for i in range(int(input("Enter total number of random numbers to be generatted: ")))]
# RD = [0.67, 0.34, 0.90, 0.25, 0.89, 0.74, 0.83, 0.76, 0.79, 0.64, 0.02, 0.96, 0.99, 0.77, 0.67, 0.05, 0.47, 0.30, 0.17, 0.82, 0.42, 0.79, 0.71, 0.23, 0.19]
print("Random Digits:\n", RD)
# Total Class Intervals n
n = int(input("Enter Total Class intervals: "))

# Range of Classes for n as class interval
interval = [1/n] * n
ranges = []
for i in range(n):
    ranges.append(round(sum(interval[0:i + 1]),1))

# Observed Frequency = Oi (frequency in the ranges)
Oi = [0] * n
for num in RD:
    for i in range(n):
        if num <= ranges[i]:
            Oi[i] += 1
            break

# Eperimental values = Ei = N/n
Ei = len(RD)/n

# Chi Square X^2 = (Oi - Ei)^2 / Ei
X = []
for i in range(n):
    X.append(((Oi[i] - Ei) ** 2) / Ei)

# Printing the Table
print("\nClass\tRange\tOi\tEi\tX^2")
print('-' * 35)
for i in range(n):
    print("{}\t{}\t{}\t{}\t{}" .format(i + 1, ranges[i], Oi[i], Ei, X[i]))

print('\nChi Square: ', sum(X))
Dcritical = float(input("Enter D Critical Value: "))

if sum(X) <= Dcritical:
    print('Hypothesis H0 is Accepted')
else:
    print('Hypothesis H0 is Rejected')