import pandas as pd
import numpy as np

lst = [10999917414, 8881583636, 8725832755, 8578325532]
lst1 = [189, 208, 149, 157]
lst2 = [7916, 8508, 7226, 7617]
dic1 = {"Population": lst, "Hospitals": lst1, "Schools": lst2}
d = pd.DataFrame(data=dic1, index=["Delhi", "Mumbai", "Kolkata", "Chennai"])
print(d)
print("====Delhi====")
print(d.loc["Delhi", :])
print(d.loc["Delhi": "Kolkata", :])
