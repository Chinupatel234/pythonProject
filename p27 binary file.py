import pickle

dic1 = {"Emp_no": 1201, "Name": "Chinmay", "Age": 17, "Salary": 1000000000}
dic2 = {"Emp_no": 1202, "Name": "Mitul", "Age": 40, "Salary": 1000000001}
dic3 = {"Emp_no": 1203, "Name": "Amruta", "Age": 40, "Salary": 1000000002}

file = open("Emp.data", "wb")
pickle.dump(dic1, file)
pickle.dump(dic2, file)
pickle.dump(dic3, file)
print("Information transferred successfully!!!")
file.close()
