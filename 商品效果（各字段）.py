import pandas as pd
import os
from datetime import datetime

#筛选的时间段设置，并将string转换成datetime类型
start = '2018年9月1日'
end = '2018年9月9日'
startTime = datetime.strptime(start,'%Y年%m月%d日')
endTime = datetime.strptime(end,'%Y年%m月%d日')

#列出重点商品
keyProducts = ['559155141183','536917158905','39260919615','570116625087','42606234510','567790305196','529377312437','540802675654','568294843384','521521689049','575385131461','574202469549','528245239236','575635931103','538764408904','558432378024','41789799664','559514943644','543998928260','538755563876','558449984111','564881442911','573724867803','540803663166','530280329613','524033984831','528041534335','549556531800','35139327428','560324316935','44979445487']

#筛选出在所设置的时间段内的表（文件名包含日期信息），然后将符合条件的文件名加入到列表li中
path_in = r"C:\Users\x\Desktop\商品效果"
list = os.listdir(path_in)
li = []
for filename in list:
    date = datetime.strptime(filename[11:21],'%Y-%m-%d')
    if os.path.splitext(filename)[1] == '.xls' and date>=startTime and date<=endTime:
        li.append(filename)

path_out = r"C:\Users\x\Desktop\concat.xlsx"
writer = pd.ExcelWriter(path_out)

#1、访客数
os.chdir(path_in)
l1 = []
for filename in li:
    df = pd.read_excel(filename,skiprows=3)
    df = df.query('商品id in @keyProducts')
    df = df[['商品id','访客数']]
    df.set_index('商品id',inplace=True)
    df.columns = [datetime.strptime(filename[11:21],'%Y-%m-%d').strftime('%m-%d')]
    l1.append(df)

df1 = pd.concat(l1, axis=1,sort=True)
df1.to_excel(writer,'访客数')


#2、平均停留时长
os.chdir(path_in)
l2 = []
for filename in li:
    df = pd.read_excel(filename,skiprows=3)
    df = df[['商品id','平均停留时长']]
    df = df.query('商品id in @keyProducts')
    df.set_index('商品id',inplace=True)
    df.columns = [datetime.strptime(filename[11:21],'%Y-%m-%d').strftime('%m-%d')]
    l2.append(df)

df2 = pd.concat(l2,axis=1,sort=True)
df2.to_excel(writer,'平均停留时长')

writer.save()






