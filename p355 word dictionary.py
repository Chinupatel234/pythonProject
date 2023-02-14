dic1 = {1: "Apple", 2: "Ami", 3: "Amir", 4: "Akash", 5: "Ball", 6: "Balloon", 7: "Bell", 8: "Cat", 9: "Cake",
        10: "Camel", 11: "Dog", 12: "Dan", 13: "Dad", 14: "Dare", 15: "Disha"}
print(dic1)
n = input("Enter the letter: ").strip().capitalize()
c = 0
for i, v in dic1.items():
    if v.startswith(n):
        print(v)
        c += 1
if c == 0:
    print("Sorry letter not found in dictionary...")
