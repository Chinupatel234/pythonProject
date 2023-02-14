from matplotlib import pyplot as plt
roll_no = [1, 2, 3, 4, 5, 6, 7, 8, 9]
hindi = [11, 12, 19, 14, 13, 16, 13, 10, 19]
english = [15, 10, 18, 10, 13, 14, 15, 19, 12]
plt.scatter(hindi, roll_no, marker="*", color="red")
plt.scatter(english, roll_no, marker="s", color="blue")
plt.xlabel("Marks")
plt.ylabel("Roll_no")
plt.grid(True)
plt.show()
