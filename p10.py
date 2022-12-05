import math


def formula(a):
    ans = (math.sqrt(3)/4) * (a**2)
    return ans


m = int(input("Enter the number: "))
n = formula(m)
print("The answer is: ", n)
