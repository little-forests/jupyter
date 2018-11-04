import pandas as pd
import numpy as np
import os
from datetime import datetime

#筛选的时间段设置，并将string转换成datetime类型
start = '2018年9月1日'
end = '2018年9月9日'
startTime = datetime.strptime(start,'%Y年%m月%d日')
endTime = datetime.strptime(end,'%Y年%m月%d日')

#列出重点商品
keyProducts = ['559155141183','536917158905','39260919615','570116625087','42606234510','567790305196','529377312437','540802675654','568294843384','521521689049','575385131461','574202469549','528245239236','575635931103','538764408904','558432378024','41789799664','559514943644','543998928260','538755563876','558449984111','564881442911','573724867803','540803663166','530280329613','524033984831','528041534335','549556531800','35139327428','560324316935','44979445487']

path = r"C:\Users\x\Desktop\pandas操作原数据\1、商品效果趋势（按指标统计）"

#多个sheet表保存时，用ExcelWriter()方法设置路径，然后用writer.save()保存；而只有一个表的时候，直接保存路径就行
writer = pd.ExcelWriter(path+'//result.xlsx')

#筛选出在所设置的时间段内的表（文件名包含日期信息），然后将符合条件的文件名加入到列表filenames中
filenames = []
for filename in os.listdir(path):
    os.chdir(path)
    date = datetime.strptime(filename[11:21],'%Y-%m-%d')
    if date>=startTime and date<=endTime:
        filenames.append(filename)

#访客数
l1 = []
for filename in filenames:
    df = pd.read_excel(filename,skiprows=3)
    df = df.query('商品id in @keyProducts')
    df = df[['商品id','访客数']]
    df.set_index('商品id',inplace=True)
    df.columns = [datetime.strptime(filename[11:21],'%Y-%m-%d').strftime('%m-%d')]
    l1.append(df)

#纵向合并,concat默认sort=True
dfs1 = pd.concat(l1,axis=1)
dfs1.to_excel(writer,'访客数')


#平均停留时长
l2 = []
for filename in filenames:
    df = pd.read_excel(filename,skiprows=3)
    df = df.query('商品id in @keyProducts')
    df = df[['商品id','平均停留时长']]
    df.set_index('商品id',inplace=True)
    df.columns = [datetime.strptime(filename[11:21],'%Y-%m-%d').strftime('%m-%d')]
    l2.append(df)

dfs2 = pd.concat(l2,axis=1)
dfs2.to_excel(writer,'平均停留时长')

writer.save()