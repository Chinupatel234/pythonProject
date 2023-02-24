lst1 = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
t = 1
while t <= 10:
    if t % 2 == 0:
        n = int(input("Player 2 enter your move (X): "))
        if lst1[n - 1] == "_":
            lst1[n - 1] = "X"
        else:
            print("Already there!!!")
            t -= 1
    else:
        m = int(input("Player 1 enter your move (O): "))
        if lst1[m - 1] == "_":
            lst1[m - 1] = "O"
        else:
            print("Already there!!!")
            t -= 1

    print(lst1[0], "|", lst1[1], "|", lst1[2])
    print(lst1[3], "|", lst1[4], "|", lst1[5])
    print(lst1[6], "|", lst1[7], "|", lst1[8])

    if lst1[0] == lst1[4] == lst1[8] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[0] == lst1[1] == lst1[2] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[0] == lst1[3] == lst1[6] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[1] == lst1[4] == lst1[7] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[2] == lst1[5] == lst1[8] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[3] == lst1[4] == lst1[7] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[6] == lst1[7] == lst1[8] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[2] == lst1[4] == lst1[6] == "X":
        print("Player 1 is the winner!!!")
        break
    elif lst1[0] == lst1[4] == lst1[8] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[0] == lst1[1] == lst1[2] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[0] == lst1[3] == lst1[6] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[1] == lst1[4] == lst1[7] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[2] == lst1[5] == lst1[8] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[3] == lst1[4] == lst1[7] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[6] == lst1[7] == lst1[8] == "O":
        print("Player 2 is the winner!!!")
        break
    elif lst1[2] == lst1[4] == lst1[6] == "O":
        print("Player 2 is the winner!!!")
        break
    t += 1
    if t == 10:
        print("It's an tie...")
