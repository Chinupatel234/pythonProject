import pickle

dic1 = {}
file = open("stu.data", "rb")
try:
    while True:
        dic1 = pickle.load(file)
        print(dic1)
except EOFError:
    file.close()
