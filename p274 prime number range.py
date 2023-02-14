m = int(input("Enter the number: "))
n = int(input("Enter the number: "))

for i in range(m, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, "is a prime number")
