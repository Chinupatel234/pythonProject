import pandas as pd
import numpy as np

lst1 = [10000, 232240, 45600, 89100, np.NaN]
lst2 = [42544, 325353, 32535, 353532, 53535]
lst3 = [73243, 32325, 46745, 457475, 745754]
lst4 = [13423, 6346, 4643636, 46436, 34643]
dic1 = {"Mango": lst1, "Orange": lst2, "Apple": lst3, "Banana": lst4}
index1 = ["Chinmay", "Ameya", "Harnil", "Madhav", "Aryan"]
n = pd.DataFrame(data=dic1, index=index1)
print(n)
print("")
m = n.loc["Chinmay", :]
print(m)
print("")
k = n["Mango"].count()
print("Mango is sold by", k, "sellers")
print("")
j = n.loc["Chinmay": "Harnil", "Orange": "Apple"]
print(j)
print("")
i = n.iloc[1:3, 2:3]
print(i)
print("")
h = n.loc["Ameya": "Harnil", "Mango": "Apple"].cumsum()
print(h)
print("")
try:
    s = n["Chikoo"]
    print(s)
except KeyError:
    print("Such column is not present!!!")
print("")
p = n.loc["Ameya", : "Apple":]
print(p)
print("")
for k, v in n.iterrows():
    n = input("Enter the name whom you want to see: ")
    # print(k)
    if k == n:
        print(n, "sold", v["Apple"], "apples...")
    else:
        print("Sorry can't print other information!!!")


