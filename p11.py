from math import *


def mathematics(n, s):
    area = (1/2) * n * sin((360/n) * pi/180) * (s**2)
    return area


m = int(input("Enter the number of side of polygon: "))
f = int(input("Enter the length from centre to corner: "))
c = mathematics(m, f)
print("The answer is: ", c)
