import pandas as pd
import numpy as np
import os

path_in = r"C:\Users\x\Desktop\csvS"

list = os.listdir(path_in)
os.chdir(path_in)
li = []
for filename in list:
    if os.path.splitext(filename)[1] == '.csv':
        df = pd.read_csv(filename, engine='python')
        li.append(df)

#axis默认为0
dfs = pd.concat(li,sort=False)
dfs.to_csv(path_in+'\\合并.csv',index=False,encoding='utf_8_sig')

