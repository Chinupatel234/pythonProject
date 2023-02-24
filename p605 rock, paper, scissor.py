import random

lst1 = ["Rock", "Paper", "Scissor"]
p1 = 0
c = 0
player_1 = input("Player1 enter your name: ")
while True:
    n = input("Player1 please select (Rock, Paper, Scissor): ")
    print(player_1, "your move is: ", n)
    m = random.choice(lst1)
    print("Computer's move is: ", m)
    if n == m:
        continue
    elif n == "Rock" and m == "Scissor":
        p1 += 1
    elif n == "Rock" and m == "Paper":
        p1 += 1
    elif n == "Paper" and m == "Scissor":
        c += 1
    elif n == "Paper" and m == "Rock":
        c += 1
    elif n == "Scissor" and m == "Paper":
        p1 += 1
    elif n == "Scissor" and m == "Rock":
        c += 1
    print("Score: ", p1, "-", c)
    if p1 == 3:
        print(player_1, "wins!!!")
        break
    elif c == 3:
        print("Computer wins!!!")
        break
