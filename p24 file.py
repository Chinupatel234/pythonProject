file = open("d:\\chinmay.txt", "w")
str1 = ""
while str1:
    str1 = file.readline()
    for i in str1.split():
        print(i, end="#")
    print("")
file.close()
