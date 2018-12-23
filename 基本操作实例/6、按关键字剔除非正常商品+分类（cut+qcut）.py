import pandas as pd
import numpy as np

path = r"C:\Users\x\Desktop\pandas操作原数据\6、按关键字剔除非正常商品+分类（cut+qcut）"
df = pd.read_csv(path+'//原数据.csv',engine='python',encoding='utf_8_sig')

# 根据关键字删除非正常商品
keywords = '运费安装费补差|赠品|优惠券'
dfs = df[df['宝贝标题 '].str.contains(keywords).map(lambda x: not x)]

# 根据条件剔除非正常订单
# df_filtered = dfs[(dfs['买家实际支付金额']>0) & (dfs['订单状态'] == '交易成功')]
df_filtered = dfs.query('订单状态 == "交易成功" & 买家实际支付金额 > 0')

# 按照金额进行4等分划分（依据金额数）
#cats1 = pd.cut(df_filtered['买家实际支付金额'],[0,3000,5000,30000],precision=0)
cats1 = pd.cut(df_filtered['买家实际支付金额'],4,precision=0)
print(cats1.value_counts())

# 求上述各组的金额总数
grouped1 = df_filtered['买家实际支付金额'].groupby(cats1).sum()
print(grouped1)

# 等价于cats3 = pd.qcut(df_filtered['买家实际支付金额'],[0,0.25,0.5,0.75,1])
cats2 = pd.qcut(df_filtered['买家实际支付金额'],4)
print(cats2.value_counts())

df_filtered.to_csv(path+'//结果.csv',index=False,encoding='utf_8_sig')
