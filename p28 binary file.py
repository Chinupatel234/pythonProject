import pickle
import time

dic1 = {}
file = open("stu.data", "wb")
ans = 'y'
while ans == 'y' or ans == 'Y':
    roll_no = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    marks = float(input("Enter the marks: "))
    dic1["Roll_number"] = roll_no
    dic1["Name"] = name
    dic1["Marks"] = marks
    pickle.dump(dic1, file)
    print(dic1)
    n = input("Do you want to continue(y/n)? ")
    if n == 'n' or n == 'N':
        time.sleep(2)
        print("Sorry breaking out!!!")
        break
file.close()
