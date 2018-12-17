import pandas as pd
import numpy as np
import os

path = r"C:\Users\x\Desktop\pandas操作原数据\2、合并多个csv表"

li = []
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.csv':
        os.chdir(path)
        df = pd.read_csv(filename,engine='python')
        li.append(df)

#默认axis=0
dfs = pd.concat(li,sort=False)
dfs.to_csv(path+'//result.csv',index=False,encoding='utf_8_sig')

