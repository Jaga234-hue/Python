import pandas as pd
#creating series

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'],dtype=float,name='numbers')

print(s)
print(type(s))

dict = {"name":['python', 'java', 'c#'], "year":[2018, 2019, 2020], "price":[1000, 2000, 3000]} 
s = pd.Series(dict)
print(s)

j = pd.Series(34, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
j2 = pd.Series(56, index=[0, 1, 2, 3])
print(j)
print(j2)
print(j + j2)