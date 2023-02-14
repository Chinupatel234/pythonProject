import random


def enqueue(stack1, item1):
    stack1.append(item1)
    print(item1, "added to your cart")


def dequeue(stack1):
    if len(stack1) == 0:
        print("Stack is empty...")
    else:
        a = stack1.pop(0)
        print(a, "order done")


def peek(stack1):
    if len(stack1) == 0:
        print("Stack is empty...")
    else:
        p = 0
        print(stack1[p], "your order is waiting")


def display(stack1):
    if len(stack1) == 0:
        print("Stack is empty...")
    else:
        for i in range(len(stack1)):
            print(stack1[i])


stack = []
while True:
    print("-"*20)
    print("1.Give Order")
    print("2.Order done")
    print("3.Waiting order")
    print("4.View all the orders")
    print("5.Exit")
    ch = int(input("Enter your choice(1-4): "))
    if ch == 1:
        r = random.randint(100, 999)
        f = input("Enter the item: ")
        q = int(input("Enter the quantity: "))
        d = input("Enter the dessert: ")
        item = [r, f, q, d]
        enqueue(stack, item)
    elif ch == 2:
        dequeue(stack)
    elif ch == 3:
        peek(stack)
    elif ch == 4:
        display(stack)
    elif ch == 5:
        print("Goodbye...have a nice day!!!")
        break
    else:
        print("Wrong option...")
