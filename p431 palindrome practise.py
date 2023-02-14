n = input("Enter the name: ")
m = len(n) - 1
s = 0
for i in range(m // 2):
    if n[i] == n[i - 1 - i]:
        s += 1
if s == 0:
    print("Not a Palindrome...")
else:
    print("Palindrome!!!")
