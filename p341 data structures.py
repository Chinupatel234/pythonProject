def cls():
    print("\n" * 50)


def isEmpty(stack):
    if stack == []:
        return True
    else:
        return False


def push(stack, item):
    stack.append(item)
    top = len(stack) - 1


def display(stack):
    if isEmpty(stack):
        print("Stack empty!!!")
    else:
        top = len(stack) - 1
        print(stack[top], "<-top")
        for a in range(top):
            print(stack[a])


stack = []
top = None
while True:
    cls()
    print("STACK OPERATIONS")
    print("1. Push")
    print("2. Display stack")
    print("3. Exit")
    ch = int(input("Enter your choice(1-3): "))
    if ch == 1:
        bno = int(input("Enter book no. to be inserted: "))
        bname = input("Enter the book name to be inserted: ")
        item = [bno, bname]
        push(stack, item)
        input()
    elif ch == 2:
        display(stack)
        input()
    elif ch == 3:
        break
    else:
        print("Invalid choice!!!")
        input()
