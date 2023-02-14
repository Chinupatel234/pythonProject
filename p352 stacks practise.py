def push(stack1, val1):
    stack1.append(val1)
    print(val1, "appended successfully")


def pop(stack1):
    p = stack1.pop()
    print(p, "popped")


def peek(stack1):
    m = len(stack1) - 1
    print("The top most value is", stack1[m])


def display(stack1):
    for i in range(len(stack1) - 1, -1, -1):
        print(stack1[i])


stack = []
while True:
    print("-"*20)
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    ch = int(input("Enter your choice(1-4): "))
    if ch == 1:
        val = int(input("Enter the item you want to add: "))
        push(stack, val)
    elif ch == 2:
        pop(stack)
    elif ch == 3:
        peek(stack)
    elif ch == 4:
        display(stack)
    elif ch == 5:
        print("Goodbye!!!...")
        break
    else:
        print("Wrong option...")
