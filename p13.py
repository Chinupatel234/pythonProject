import random

AR = [20, 30, 40, 50, 60, 70]
lower = random.randint(1, 3)
upper = random.randint(2, 4)
for k in range(lower, upper + 1):
    print(AR[k], end="#")
