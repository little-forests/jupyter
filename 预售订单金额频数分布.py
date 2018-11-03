import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif']=['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus']=False

path = r"C:\Users\x\Desktop\京东预售匹配表10.20-10.28.xlsx"
df = pd.read_excel(path)
df = df.query('订单预售状态 == "已付定金"')
grouped = df.groupby('下单时间2')[['预订金额（含运费）']]
df2 = grouped.sum()

df2['累计金额占比'] = df2['预订金额（含运费）'].cumsum()/df2['预订金额（含运费）'].sum()
df2 = df2.to_period('d')
df2.index = df2.index.astype('str')

df2['预订金额（含运费）'].plot(kind='bar',title='销售额走势帕累托图',rot=30,
                               color=['#6794a7','#014d64','#76c0c1','#01a2d9','#7ad2f6','#00887d','#76c0c1','#7bd3f6','#ee8f71'])
df2['累计预售金额占比'].plot(secondary_y=True,color='#c10534',marker='o',linestyle='--',rot=30,alpha=0.8)
plt.show()
