import math
import random as rd
import matplotlib.pyplot as plt

alpha = 0.05

a1 = sorted([rd.normalvariate(100, 5) for i in range(25)])
a2 = sorted([rd.normalvariate(100, 5) for i in range(25)])

x1 = {}
x2 = {}

for i in a1:
    x1[i] = a1.count(i)
for i in a2:
    x2[i] = a2.count(i)

mean1 = sum(a1)/len(a1)
mean2 = sum(a2)/len(a2)

sd1 = 0
sd2 = 0
for i in a1:
    sd1 += (i-mean1)**2
sd1 = math.sqrt(sd1/len(a1))
for i in a2:
    sd2 += (i-mean2)**2
sd2 = math.sqrt(sd2/len(a1))

se = math.sqrt(sd1**2/len(a1)+sd2**2/len(a2))
t = (mean1 - mean2)/se
df = len(a1)+len(a2) - 2
print(df, t)

fig, axe = plt.subplots()
axe.bar(x1.keys(), x1.values())
axe.bar(x2.keys(), x2.values())
