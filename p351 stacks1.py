def push(stack1, val1):
    stack1.append(val1)
    print(val1, "pushed successfully")


def pop(stack1):
    a = stack1.pop()
    print("Popped item is", a)


def peek(stack1):
    index = len(stack1) - 1
    print("Top most item is", stack1[index])


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
    ch = int(input("Enter your choice(1-5):"))
    if ch == 1:
        val = int(input("Enter the item: "))
        push(stack, val)
    elif ch == 2:
        if len(stack) == 0:
            print("Empty stack!!!")
        else:
            pop(stack)
    elif ch == 3:
        if len(stack) == 0:
            print("Empty stack!!!")
        else:
            peek(stack)
    elif ch == 4:
        if len(stack) == 0:
            print("Empty stack!!!")
        else:
            display(stack)
    elif ch == 5:
        print("Goodbye...")
        break
