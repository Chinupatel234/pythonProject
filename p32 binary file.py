import pickle

string = "This is my first line and second line!!!"
with open("chinmay.data", "wb") as fh:
    pickle.dump(string, fh)
print("File successfully created.")
