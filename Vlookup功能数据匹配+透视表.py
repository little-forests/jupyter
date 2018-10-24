import os
import re
import pandas as pd
import numpy as np
from datetime import datetime

path_in = r"C:\Users\x\Desktop\小项目(知识点汇总)-利用vlookup匹配功能"
path_matchingTable = r"C:\Users\x\Desktop\型号-类目匹配(去重).xlsx"

regex = re.compile(r'[A-Z]*\d{4,6}[A-Z]*')

filenames = []
for filename in os.listdir(path_in):
    extension = os.path.splitext(filename)[1]
    if extension in ('.xlsx','.xls','.csv'):
        filenames.append(filename)


os.chdir(path_in)
li = []
for filename in filenames:
    extension = os.path.splitext(filename)[1]
    date = datetime.strptime(filename[3:9],'%Y%m').strftime('%Y/%m')

    #判断文件后缀，然后打开文件
    if extension in ('.xlsx','.xls'):
        df = pd.read_excel(filename)
        df['订单编号'] = df['订单编号'].map(lambda x:'="'+str(x)+'"')
    else:
        df = pd.read_csv(filename,engine='python')
    
    #插入一列，显示日期
    df.insert(1,'日期',date)
    li.append(df)

#合并多个表，并选取有用的字段
dfs = pd.concat(li,sort=False)
dfs = dfs[['订单编号', '日期', '买家会员名', '买家实际支付金额', '订单状态', '收货人姓名', '收货地址 ', '联系手机', '宝贝标题 ', '宝贝总数量', '订单关闭原因']]

#找出‘宝贝标题’中的‘产品型号’，并新增一列存放‘产品型号’
products = dfs['宝贝标题 '].map(lambda x:'+'.join(regex.findall(str(x))))
dfs.insert(9,'产品型号',products)

#匹配‘产品型号’（实现Vlookup功能）
matchingTable = pd.read_excel(path_matchingTable)
matchingTable['产品型号'] = matchingTable['产品型号'].astype(str)
result = pd.merge(dfs,matchingTable[['二级类目','三级类目','产品型号']],how='left',on=['产品型号'])

#透视表（假设有4个类目），求四级类目下的订单“总金额"及"平均金额"
pd.pivot_table(result, index=['一级类目','二级类目','三级类目','四级类目'],values=['买家实际支付金额'],aggfunc=[np.sum,np.mean])


os.chdir(path_in)
#result.to_csv('最终数据.csv',index=False,encoding='utf_8_sig')
result.to_excel('最终数据.xlsx',index=False)
    
