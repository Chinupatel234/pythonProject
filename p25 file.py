file = open("d:\\chinmay.txt", "r")
str1 = ""
v = 0
c = 0
while str1:
    str1 = file.read()
    if str1 == 'a' or str1 == 'e' or str1 == 'i' or str1 == 'o' or str1 == 'u':
        v = v + 1
    else:
        c = c + 1
print("Vowels: ", v)
print("Consonants: ", c)
file.close()
 