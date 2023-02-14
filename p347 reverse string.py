n = "Chinmay"
stack = []

for i in n:
    stack.append(i)
m = ""
while len(stack):
    k = stack.pop()
    m += k
print(m)
