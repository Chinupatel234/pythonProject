import pickle

dic2 = {}
file = open("Emp.data", "rb")
try:
    print("This file stores these records!!!")
    while True:
        dic2 = pickle.load(file)
        print(dic2)
except EOFError:
    file.close()
