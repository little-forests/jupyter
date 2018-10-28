import pandas as pd
import numpy as np
from dateutil.parser import parse

path = r"C:\Users\x\Desktop"
df = pd.read_csv(path+'//苏宁旗舰店汇总.csv',engine='python',encoding='utf_8_sig',skiprows=1)

df = df.reindex(columns=(['订单编号','买家会员名','订单实付款','订单状态（头状态）','收货人姓名','收货地址','联系手机','订单下单时间','支付时间','商品名称','购买数量']))
df.rename(columns={'订单实付款':'买家实际支付金额',
                        '订单状态（头状态）':'订单状态',
                        '订单下单时间':'订单创建时间',
                        '支付时间':'订单付款时间 ',
                        '商品名称':'宝贝标题',
                        '购买数量':'宝贝总数量'},inplace=True)

df['店铺名称'] = '苏宁旗舰店'

df = df.query('订单编号!="订单编号"')
period = df['订单创建时间'].map(lambda x: parse(x))
df.index = pd.Index(period,name='日期')
df2 = df.to_period('M')

df2.to_csv(path+'//统一字段.csv',encoding='utf_8_sig')