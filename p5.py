def string_join(a, b):
    c = b.join(a)
    return c


m = input("Enter your name: ")
n = input("Enter some character: ")
s = string_join(m, n)
print("The new string is: ", s)
