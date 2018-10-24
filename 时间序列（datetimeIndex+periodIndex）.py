import pandas as pd
import numpy as np
from datetime import datetime

path_in = r"C:\Users\x\Desktop\filtered.csv"
path_out = r"C:\Users\x\Desktop\filtered_x.csv"
df = pd.read_csv(path_in, engine='python',encoding='utf_8_sig')

#将“订单创建时间”字段的str转换成datetime
df_date = df['订单创建时间'].map(lambda x:datetime.strptime(str(x[:19]),"%Y-%m-%d %H:%M:%S"))
df.insert(1,'订单日期',df_date)
df.set_index('订单日期',inplace=True)

#更改切片内容以及频率
#dfs = df.to_period('Y')再进行透视，是按照年份求和及平均值
#dfs = df.to_period('M')再进行透视，是按照年月份求和及平均值
# dfs = df['2017':'2018'].to_period('M')
dfs = df['2016'].to_period('M')

pivot = pd.pivot_table(dfs,index=['订单日期'],values=['买家实际支付金额'],aggfunc=[np.sum,np.mean])
print(pivot)

# dfs.to_csv(path_out,index=False,encoding='utf_8_sig')
