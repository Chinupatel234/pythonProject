import random


colors = ["VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"]
end = random.randrange(2) + 3
begin = random.randrange(end) + 1
for i in range(begin, end):
    print(colors[i], end="&")
