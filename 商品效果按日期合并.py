import pandas as pd
import os
from datetime import datetime

start = '2018年9月1日'
end = '2018年9月8日'
startTime = datetime.strptime(start,'%Y年%m月%d日')
endTime = datetime.strptime(end,'%Y年%m月%d日')

objectiveList=[
    '560324316935',
    '549556531800',
    '528041534335',
    '524033984831',
    '530280329613'
]

path_in = r'C:\Users\x\Desktop\商品效果'
list = os.listdir(path_in)
li=[]
for filename in list:
    date = datetime.strptime(filename[11:21],'%Y-%m-%d')
    if os.path.splitext(filename)[1] == '.xls' and date>=startTime and date<=endTime:
        li.append(filename)

os.chdir(path_in)
l=[]
for filename in li:
    df = pd.read_excel(filename,skiprows=3)
    df = df.query('商品id in @objectiveList')
    df = df[['商品id','访客数']]
    df.set_index('商品id',inplace=True)
    df.columns = [datetime.strptime(filename[11:21],'%Y-%m-%d').strftime('%m-%d')]
    l.append(df)

path_out = r'C:\Users\x\Desktop\test.xlsx'
writer = pd.ExcelWriter(path_out)

dfs = pd.concat(l,axis=1,sort=True)
dfs.to_excel(writer,'访客数')
writer.save()

