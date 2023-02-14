import mysql.connector
import random
import string

mydb = mysql.connector.connect(host="localhost", user="root", password="chinmaypatel@8383")
mycur = mydb.cursor()

m = input("What type of email you want to create(google/yahoo):").strip().lower()
while m not in ["google", "yahoo"]:
    print("You are entering wrong name please enter(google/yahoo)...")
    m = input("What type of email you want to create(google/yahoo):").strip().lower()
print("You have selected", m, "mail")

list1 = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
list2 = []

if m == "google":
    for letter in string.ascii_letters:
        list2.append(letter)

    list3 = list1 + list2
    print("Your password is:")
    print("*"*30)
    for d in range(12):
        rand_password = random.choice(list3)
        print(rand_password, end="")
    print("@gmail.com")
    print("*"*30)

elif m == "yahoo":
    for letter in string.ascii_letters:
        list2.append(letter)

    list3 = list1 + list2

    for d in range(12):
        rand_password = random.choice(list3)
        print(rand_password, end="")
        list2.append(rand_password)
    print("@yahoo.com")
    print(list2)

mycur.execute("use airlines1")

while True:
    print("======WELCOME TO CP AIRLINES======")
    print("\t\tAIRLINES")
    print("1)Emirates")
    print("2)Etihad")
    print("3)Singapore Airlines")
    print("4)Air India")
    print("5)Qatar")
    print("6)Exit")
    ch = int(input("Enter the flight which you want to choose(1/2/3/4/5/6):"))
    if ch == 1:
        print("===WELCOME TO EMIRATES===")
        n = int(input("Enter passengers: "))
        for i in range(n):
            id = str(input("Enter the id: "))
            name = str(input("Enter the name: ")).strip().upper()
            gender = str(input("Enter the gender(M/F): ")).strip().upper()
            while gender not in ["M", "F"]:
                print("Please correct(M/F)...")
                gender = str(input("Enter the gender(M/F): ")).strip().upper()
            print(gender)
            passport_number = str(input("Enter the passport number: ")).strip().upper()
            a = len(passport_number)
            while a > 12:
                print("Passport number should be only 12 digits...")
                passport_number = str(input("Enter the passport number: ")).strip().upper()
                if len(passport_number) <= 12:
                    print(passport_number)
                    break
            airlines1 = str(input("Enter your airline name: ")).strip().upper()
            while airlines1 not in ["EMIRATES"]:
                print("Please enter the correct airlines...")
                airlines1 = str(input("Enter your airline name: ")).strip().upper()
            column_table = "insert into airlines1 values ('" + id + "', '" + name + "', '" + gender + "', '" + passport_number + "', '" + airlines1 + "')"
            mycur.execute(column_table)
            mydb.commit()
            mycur.execute("select * from airlines1 where passport_number in ('"+passport_number+"')")
            result = mycur.fetchall()
            print("Your boarding pass is:")
            for x in result:
                print("*"*30)
                print(*x)
                print("*"*30)
            print("")
        a = int(n)
        b = 11000
        print("Your total: ", a * b)
        print("Thank you for choosing Emirates...")
        print("")
        mycur.execute("select * from airlines1")
        result = mycur.fetchall()
        print("="*40)
        for x in result:
            print(*x)
        print("")
        print("="*40)
        a = input("Do you want to continue(Y/N):").strip().upper()
        if a == "Y":
            continue
        else:
            print("Byeeee....")
            break

    elif ch == 2:
        print("===WELCOME TO ETIHAD===")
        mycur.execute("use airlines2")
        n = int(input("Enter passengers: "))
        for i in range(n):
            id = str(input("Enter the id: "))
            name = str(input("Enter the name: ")).strip().upper()
            gender = str(input("Enter the gender(M/F): ")).strip().upper()
            while gender not in ["M", "F"]:
                print("Please correct(M/F)...")
                gender = str(input("Enter the gender(M/F): ")).strip().upper()
            passport_number = str(input("Enter the passport number: ")).strip().upper()
            a = len(passport_number)
            while a > 12:
                print("Passport number should be only 12 digits...")
                passport_number = str(input("Enter the passport number: ")).strip().upper()
                if len(passport_number) <= 12:
                    print(passport_number)
                    break
            airlines1 = str(input("Enter your airline name: ")).strip().upper()
            while airlines1 not in ["ETIHAD"]:
                print("Please enter the correct airlines...")
                airlines1 = str(input("Enter your airline name: ")).strip().upper()
            column_table = "insert into airlines2 values ('" + id + "', '" + name + "', '" + gender + "', '" + passport_number + "', '" + airlines1 + "')"
            mycur.execute(column_table)
            mydb.commit()
            mycur.execute("select * from airlines2 where passport_number in ('" + passport_number + "')")
            result = mycur.fetchall()
            print("Your boarding pass is:")
            for x in result:
                print("*" * 30)
                print(*x)
                print("*" * 30)
            print("")
        a = int(n)
        b = 12000
        print("Your total: ", a * b)
        print("Thank you for choosing Etihad...")
        mycur.execute("select * from airlines2")
        result = mycur.fetchall()
        print("="*40)
        for x in result:
            print(*x)
        print("")
        print("="*40)
        a = input("Do you want to continue(Y/N):").strip().upper()
        if a == "Y":
            continue
        else:
            print("Byeeee....")
            break

    elif ch == 3:
        print("===WELCOME TO SINGAPORE AIRLINES===")
        mycur.execute("use airlines3")
        n = int(input("Enter passengers: "))
        for i in range(n):
            id = str(input("Enter the id: "))
            name = str(input("Enter the name: ")).strip().upper()
            gender = str(input("Enter the gender(M/F): ")).strip().upper()
            while gender not in ["M", "F"]:
                print("Please correct(M/F)...")
                gender = str(input("Enter the gender(M/F): ")).strip().upper()
            passport_number = str(input("Enter the passport number: ")).strip().upper()
            a = len(passport_number)
            while a > 12:
                print("Passport number should be only 12 digits...")
                passport_number = str(input("Enter the passport number: ")).strip().upper()
                if len(passport_number) <= 12:
                    print(passport_number)
                    break
            airlines1 = str(input("Enter your airline name: ")).strip().upper()
            while airlines1 not in ["SINGAPORE"]:
                print("Please enter the correct airlines...")
                airlines1 = str(input("Enter your airline name: ")).strip().upper()
            column_table = "insert into airlines3 values ('" + id + "', '" + name + "', '" + gender + "', '" + passport_number + "', '" + airlines1 + "')"
            mycur.execute(column_table)
            mydb.commit()
            mycur.execute("select * from airlines3 where passport_number in ('" + passport_number + "')")
            result = mycur.fetchall()
            print("Your boarding pass is:")
            for x in result:
                print("*"*30)
                print(*x)
                print("*"*30)
            print("")
        a = int(n)
        b = 9000
        print("Your total: ", a * b)
        print("Thank you for choosing Singapore Airlines...")
        mycur.execute("select * from airlines3")
        result = mycur.fetchall()
        print("="*40)
        for x in result:
            print(*x)
        print("")
        print("="*40)
        a = input("Do you want to continue(Y/N):").strip().upper()
        if a == "Y":
            continue
        else:
            print("Byeeee....")
            break

    elif ch == 4:
        print("===WELCOME TO AIR INDIA===")
        mycur.execute("use airlines4")
        n = int(input("Enter passengers: "))
        for i in range(n):
            id = str(input("Enter the id: "))
            name = str(input("Enter the name: ")).strip().upper()
            gender = str(input("Enter the gender(M/F): ")).strip().upper()
            while gender not in ["M", "F"]:
                print("Please correct(M/F)...")
                gender = str(input("Enter the gender(M/F): ")).strip().upper()
            passport_number = str(input("Enter the passport number: ")).strip().upper()
            a = len(passport_number)
            while a > 12:
                print("Passport number should be only 12 digits...")
                passport_number = str(input("Enter the passport number: ")).strip().upper()
                if len(passport_number) <= 12:
                    print(passport_number)
                    break
            airlines1 = str(input("Enter your airline name: ")).strip().upper()
            while airlines1 not in ["AIR INDIA", "AIRINDIA"]:
                print("Please enter the correct airlines...")
                airlines1 = str(input("Enter your airline name: ")).strip().upper()
            column_table = "insert into airlines4 values ('" + id + "', '" + name + "', '" + gender + "', '" + passport_number + "', '" + airlines1 + "')"
            mycur.execute(column_table)
            mydb.commit()
            mycur.execute("select * from airlines4 where passport_number in ('" + passport_number + "')")
            result = mycur.fetchall()
            print("Your boarding pass is:")
            for x in result:
                print("*"*30)
                print(*x)
                print("*"*30)
            print("")
        a = int(n)
        b = 9000
        print("Your total: ", a * b)
        print("Thank you for choosing Air India...")
        mycur.execute("select * from airlines4")
        result = mycur.fetchall()
        print("="*40)
        for x in result:
            print(*x)
        print("")
        print("="*40)
        a = input("Do you want to continue(Y/N):").strip().upper()
        if a == "Y":
            continue
        else:
            print("Byeeee....")
            break

    elif ch == 5:
        print("===WELCOME TO QATAR===")
        mycur.execute("use airlines5")
        n = int(input("Enter passengers: "))
        for i in range(n):
            id = str(input("Enter the id: "))
            name = str(input("Enter the name: ")).strip().upper()
            gender = str(input("Enter the gender(M/F): ")).strip().upper()
            while gender not in ["M", "F"]:
                print("Please correct(M/F)...")
                gender = str(input("Enter the gender(M/F): ")).strip().upper()
            passport_number = str(input("Enter the passport number: ")).strip().upper()
            a = len(passport_number)
            while a > 12:
                print("Passport number should be only 12 digits...")
                passport_number = str(input("Enter the passport number: ")).strip().upper()
                if len(passport_number) <= 12:
                    print(passport_number)
                    break
            airlines1 = str(input("Enter your airline name: ")).strip().upper()
            while airlines1 not in ["QATAR"]:
                print("Please enter the correct airlines...")
                airlines1 = str(input("Enter your airline name: ")).strip().upper()
            column_table = "insert into airlines5 values ('" + id + "', '" + name + "', '" + gender + "', '" + passport_number + "', '" + airlines1 + "')"
            mycur.execute(column_table)
            mydb.commit()
            mycur.execute("select * from airlines5 where passport_number in ('" + passport_number + "')")
            result = mycur.fetchall()
            print("Your boarding pass is:")
            for x in result:
                print("*"*30)
                print(*x)
                print("*"*30)
            print("")
        a = int(n)
        b = 10000
        print("Your total: ", a * b)
        print("Thank you for choosing Qatar...")
        mycur.execute("select * from airlines5")
        result = mycur.fetchall()
        print("="*40)
        for x in result:
            print(*x)
        print("")
        print("="*40)
        a = input("Do you want to continue(Y/N):").strip().upper()
        if a == "Y":
            continue
        else:
            print("Byeeee....")
            break

    elif ch == 6:
        print("Bye.....")
        break
