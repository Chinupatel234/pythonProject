ans = 0
lst = []
lst1 = []
lst2 = []
lst3 = []
while ans != 4:
    print("=============")
    print("\tMENU")
    print("=============")
    print("1.Apply for school post")
    print("2.View all the names")
    print("3.Correct the errors")
    print("4.Exit")
    ans = int(input("Enter the option(1-4): "))
    if ans == 1:
        n = input("Enter your name: ")
        lst.append(n)
    elif ans == 2:
        print("All the students name are: ")
        print(lst)
    elif ans == 3:
        for i in lst:
            m = i.split()
            name = m[0]
            surname = m[1]
            if name[0].islower() or surname[0].islower():
                lst1.append(i)
        print("Incorrect list:", lst1)
        for j in lst:
            m = j.split()
            name = m[0]
            surname = m[1]
            if not name[0].islower() and not surname[0].islower():
                lst2.append(j)
        print("Correct list:", lst2)
        for x in lst:
            m = x.split()
            name = m[0]
            surname = m[1]
            lst3.append(name.capitalize() + " " + surname.capitalize())
        print("Corrected list:", lst3)
    elif ans == 4:
        print("Bye.....")
else:
    print("Thank you!!!")
