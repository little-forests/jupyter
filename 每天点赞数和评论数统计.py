from dateutil.parser import parse
import pandas as pd
import numpy as np
import os

path = r"C:\Users\x\Desktop\点赞评论数统计"

li = []
for filename in os.listdir(path):
    os.chdir(path)
    #index_col=2,将第3（发布日期）列设置为索引，parse_dates=True，解析index，现在发布日期变成了可以加减操作的日期格式
    df = pd.read_excel(filename,index_col=2,parse_dates=True)
    li.append(df)

dfs = pd.concat(li,sort=False)
dfs = dfs.to_period('D')

#当索引是重复的时候（即日期可能是重复的），level=0将索引是一样的分开
grouped = dfs.groupby(level=0)['点赞数','评论数']
# df2 = grouped.sum()
df2 = grouped.agg('sum')

# df2 = pd.pivot_table(dfs,index=['发布日期'],values=['点赞数','评论数'],aggfunc=np.sum)

df2.to_excel(path+'//合并.xlsx')


