def push(arr):
    s = []
    for x in range(0, len(arr)):
        if arr[x] % 5 == 0:
            s.append(arr[x])
    if len(s) == 0:
        print("Empty stack!!!")
    else:
        print(s)


arr1 = []
n = int(input("Enter the limit: "))
for i in range(n):
    m = int(input("Enter number" + str(i + 1) + ":"))
    arr1.append(m)
push(arr1)
