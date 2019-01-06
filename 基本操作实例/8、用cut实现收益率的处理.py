import numpy as np
import pandas as pd

path = r"C:\Users\x\Desktop\pandas操作原数据\8、用cut实现收益率的处理\12月测试交易记录大于1.95小于5.2.xlsx"
df = pd.read_excel(path)

def f(df):
    return {'交易笔数': df.count(),'总差价':df.sum()}

factor = pd.cut(df.earningRatePerDeal,[-0.05,-0.01,0,0.01,0.05])
grouped = df.groupby(factor)['balance']
result = grouped.apply(f).unstack()

result.insert(1,'交易笔数占比',result['交易笔数']/result['交易笔数'].sum())
result['交易笔数占比'] = result['交易笔数占比'].map(lambda x: format(x,'.2%'))

# 对结果按照‘总差价’降序排列，用inplace=True减少赋值的步骤
result.sort_values(by='交易笔数',ascending=False,inplace=True)
print(result)






