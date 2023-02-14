str1 = "Chinmay    Patelist he  greateso      falltime"
lst = []
str2 = ""
for i in str1:
    if i == " ":
        continue
    else:
        str2 += i
print(str2)
