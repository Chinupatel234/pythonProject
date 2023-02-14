import threading


def square(m):
    d = m * m
    print(f"The square of {m} is {d}")


def cube(m):
    d1 = m * m * m
    print(f"The cube of {m} is {d1}")


def multiplication_table(m):
    for i in range(1, 11):
        print(m, "X", i, "=", m * i)


n = int(input("Enter the number: "))
# Initialising a thread
a = threading.Thread(target=square, args=(n,))
b = threading.Thread(target=cube, args=(n,))
c = threading.Thread(target=multiplication_table, args=(n,))

# Starting a thread
a.start()
b.start()
print("The table is: ")
c.start()


# Waiting to end a thread
a.join()
b.join()
c.join()
print("All the executions are completed!!!")
