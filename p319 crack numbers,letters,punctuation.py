from string import ascii_letters, digits, punctuation
from itertools import product

for i in product(ascii_letters + digits + punctuation, repeat=8):
    print(*i)
