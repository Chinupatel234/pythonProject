dic1 = {1: "Chinmay", 2: "Mitul", 3: "Mia", 4: "Ami", 5: "Nishwa"}
print(dic1)
n = float(input("Enter the key: "))
c = 0
for i, v in dic1.items():
    if i == n:
        print(i, ":", v)
        c += 1
if c == 0:
    print("Key not found sorry...")
print("-"*20)
n = input("Enter the value: ").strip().capitalize()
for i, v in dic1.items():
    if v == n:
        print(v, ":", i)
        c += 1
if c == 0:
    print("Value not found sorry...")
