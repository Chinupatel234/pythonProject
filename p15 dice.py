import random
import time


min_no = 1
max_no = 6
answer = 'y'
while answer == 'y' or answer == 'Y':
    print("Rolling the dice...")
    value = random.randint(min_no, max_no)
    time.sleep(2)
    print("The number is...", value)
    roll_again = input("Do you want to continue? (y/n)...")
    if roll_again == 'n' or roll_again == 'N':
        print("Sorry breaking...")
        break
