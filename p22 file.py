count = int(input("Enter the limit? "))
file = open("d:\\chinmay.txt", "w")
for i in range(count):
    print("Enter the information of", (i + 1), "student")
    roll_no = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    info = str(roll_no) + "," + name + "," + str(marks) + "\n"
    file.write(info)
file.close()
