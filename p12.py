import random


def random_no(n, m):
    f = random.randint(n, m)
    return f


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
h = random_no(a, b)
print("The answer is: ", h)
