import numpy as np
import pandas as pd
data = pd.read_excel("data.xlsx",engine='openpyxl', skiprows = 1)
coord_c = data.iloc[:,1:4]
coord_c.loc[:,"1"] = 1
coord_c = np.array(coord_c)
coord_c_30 = coord_c[:70]
coord_c_0 = coord_c[70:]
pi = np.pi
a = - pi/2
b = - pi * 2/3

tm_0 = np.array([[1, 0, 0, - 0.013],
                [0, np.cos(a), -np.sin(a), 0.175],
                [0, np.sin(a), np.cos(a), 0.39],
                [0, 0, 0, 1]])

tm_30 = np.array([[1, 0, 0, - 0.013],
                [0, np.cos(b), -np.sin(b), 0.1516],
                [0, np.sin(b), np.cos(b), 0.3025],
                [0, 0, 0, 1]])

result1 = []
result2 = []

for i in range(70):
    dot = np.dot(tm_30, coord_c_30[i].reshape(4, 1))
    dot = dot[:3].reshape(3)
    result1.append(dot)
result = pd.DataFrame(result1)
result.to_excel("30.xlsx")
for i in range(30):
    dot = np.dot(tm_0, coord_c_0[i].reshape(4, 1))
    dot = dot[:3].reshape(3)
    result2.append(dot)
result = pd.DataFrame(result2)
result.to_excel("0.xlsx")