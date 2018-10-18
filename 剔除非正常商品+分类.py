import pandas as pd
import numpy as np

path_in = r"C:\Users\x\Desktop\result.csv"
path_out = r"C:\Users\x\Desktop\筛选后结果.csv"

df = pd.read_csv(path_in, engine='python', encoding='utf_8_sig')

keywords = '赠品|优惠券|换购|补拍专用链接'
dfs = df[df['宝贝标题 '].str.contains(keywords).map(lambda x: not x)]

# df_filtered = dfs[(dfs['买家实际支付金额']>0) & (dfs['订单状态'] == '交易成功')]
df_filtered = dfs.query('买家实际支付金额>0 & 订单状态 == "交易成功"')

cats1 = pd.cut(df_filtered['买家实际支付金额'], 4, precision=0)
print("按最大最小值划分4等分，各等分的个数：")
print(cats1.value_counts())

#各分组的总和
grouped1 = df_filtered['买家实际支付金额'].groupby(cats1).sum()
print(grouped1)

cats2 = pd.qcut(df_filtered['买家实际支付金额'], [0,0.6,0.8,1.0])
print("按照定义的分位数进行划分[0,0.6,0.8,1.0]，各区别的个数：")
print(cats2.value_counts())

#分组求和
grouped2 = df_filtered['买家实际支付金额'].groupby(cats2).sum()
print(grouped2)

# df_filtered.to_csv(path_out,index=False,encoding='utf_8_sig')


