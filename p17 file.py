file = open("d:\\chinmay.txt", "r")
str1 = ""
s = 0
c = 0
while str1:
    file1 = file.readline()
    s = s + len(str1)
    c = c + len(str1.strip())
print("The original size of a file is: ", s)
print("The size of the file after removing spaces and EOL is: ", c)
