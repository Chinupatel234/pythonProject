import random

st = []
ch = 0
while ch != 4:
    print("-"*20)
    print("1.Order your food")
    print("2.View the order id's")
    print("3.Order waiting")
    print("4.Exit")
    print("-"*20)
    ch = int(input("Enter the number(1-4): "))
    if ch == 1:
        m = random.randint(100, 999)
        st.append(m)
        print("Your order id is {}".format(m))
    elif ch == 2:
        for i in st:
            print(i, end=",")
        print("")
    elif ch == 3:
        a = st.pop(0)
        if len(st) == 0:
            print("No orders are there...")
        else:
            print("Order number {} is ready".format(a))
    elif ch == 4:
        print("Goodbye, have a nice day...")
        break
    else:
        print("Wrong option...")
