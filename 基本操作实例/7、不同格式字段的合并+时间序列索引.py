import numpy as np
import pandas as pd
from dateutil.parser import parse

path = r"C:\Users\x\Desktop\pandas操作原数据\7、不同格式字段的合并"
df = pd.read_csv(path+'//苏宁旗舰店汇总.csv',engine='python',encoding='utf_8_sig',skiprows=1)

df = df.reindex(columns=['订单编号','买家会员名','订单实付款','订单状态（头状态）','收货人姓名','收货地址','联系手机','订单下单时间','支付时间','商品名称','购买数量'])

# 注意，当inplace=True,df.rename()不需要赋值给新的df,直接df就已经是rename()后的字段名
df.rename(columns={'订单实付款':'买家实际支付金额',
                   '订单状态（头状态）':'订单状态',
                   '订单下单时间':'订单创建时间',
                   '支付时间':'订单付款时间 ',
                   '商品名称':'宝贝标题',
                   '购买数量':'宝贝总数量'},inplace=True)

df['店铺名称'] = '苏宁旗舰店'
df = df.query('订单编号!="订单编号"')

# 时间序列索引
period = df['订单创建时间'].map(lambda x: parse(x))
df.index = pd.Index(period,name='PeriodIndex')
df2 = df.to_period('M')

df2.to_excel(path+'//结果.xlsx',encoding='utf_8_sig')