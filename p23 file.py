file = open("d:\\chinmay.txt", "a")
for i in range(2):
    print("Enter the information of", (i + 1), "student")
    roll_no = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    info = str(roll_no) + "," + name + "," + str(marks) + "\n"
    file.write(info)
file.close()
