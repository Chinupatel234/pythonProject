i = 0


def global1():
    global i
    i = 10
    print("Inside ", end="")
    print(i)


global1()
print("Outside ", end="")
print(i)
