def seq(s1, arr1):
    if s1 not in arr1:
        arr1.append(s1)
        return "Number appended"
    return "Number already exists"


arr = [12, 14, 3, 5, 4, 6, 9]
s = int(input("Enter the number: "))
result = seq(s, arr)
print(result)
print(arr)
