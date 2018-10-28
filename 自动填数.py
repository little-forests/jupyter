import pandas as pd
import numpy as np
import re
import os

path = r"C:\Users\x\Desktop"
df = pd.read_csv(path+'//自动填数-原数据//10月20日.csv',engine='python',encoding='utf_8_sig')

regex = re.compile(r'\d{5,6}[A-Z]*')
keyProductModels = ['102085','102085C','102272','102272A','120618','121806','121803','123502','120706']

#选取需求字段，截取“宝贝名称”中的商品型号
df = df[['日期','宝贝名称','花费(分)','点击量','展现量','总收藏数','总购物车数','总成交笔数','总成交金额(分)']]
ProductModels = df['宝贝名称'].map(lambda x: ''.join(regex.findall(str(x))))
df.insert(1,'商品型号',ProductModels)

#筛选出我们需统计的keyProductModels，进行透视表操作
df2 = df.query('商品型号 in @keyProductModels')
df3 = pd.pivot_table(df2,index=['日期','商品型号'],aggfunc=np.sum)

#求点击率和点击转化率，对另两个字段进行单位的变化，用于后面更名（分-->元）做准备
#用df已有列计算产生新列，默认放在最后（insert 插入到指定位置，可以考虑到字段的顺序）
df3['点击率'] = df3['点击量']/df3['展现量']
df3['点击转化率'] = df3['总成交笔数']/df3['点击量']
df3['总成交金额(分)'] = df3['总成交金额(分)']/100
df3['花费(分)'] = df3['花费(分)']/100
df3['平均点击花费(元)'] = df3['花费(分)']/df3['点击量']
df3['ROI'] = df3['总成交金额(分)']/df3['花费(分)']

#字段更名
df3.rename(columns={'花费(分)':'花费(元)','总成交金额(分)':'总成交金额(元)'},inplace=True)
#reindex方法，既可以选取列，还可以选择字段的顺序
df3 = df3.reindex(columns=['花费(元)','点击量','展现量','平均点击花费(元)','总收藏数','总购物车数','总成交笔数','总成交金额(元)','ROI','点击转化率'])


# df3.rename(columns={'花费(分)':'花费(元)','总成交金额(分)':'总成交金额(元)'},inplace=True)
# df3.reindex(columns=['花费(元)','点击量','展现量','总收藏数','总购物车数','总成交笔数','总成交金额(元)'])

# perClickCost = df3['花费(元)']/df3['点击量']
# df3.insert(3,'平均点击花费(元)',perClickCost)
# ROI  = df3['总成交金额(元)']/df3['花费(元)']
# df3.insert(8,'ROI',ROI)

df3.to_csv(path+'//结果.csv',encoding='utf_8_sig')