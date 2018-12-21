from datetime import datetime
import pandas as pd
import numpy as np
import os
import re

path = r"C:\Users\x\Desktop\pandas操作原数据\5、多格式合并+插入年月+截取型号+Vlookup功能（merge）\原数据"
path_matchingTable = r"C:\Users\x\Desktop\pandas操作原数据\5、多格式合并+插入年月+截取型号+Vlookup功能（merge）"

regex = re.compile(r'[A-Z]*\d{4,6}[A-Z]*')

li = []
os.chdir(path)
for filename in os.listdir(path):
    extension = os.path.splitext(filename)[1]
    date = datetime.strptime(filename[3:9],'%Y%m').strftime('%Y/%m')

    #判断文件后缀，然后打开文件,不同后缀的“订单编码”的格式不一样，进行调整
    if extension in ('.xlsx','.xls'):
        df = pd.read_excel(filename)
        df['订单编号'] = df['订单编号'].map(lambda x:'="'+str(x)+'"')
    else:
        df = pd.read_csv(filename,engine='python')
    
    # 指定插入一列日期
    df.insert(1,'日期',date)
    li.append(df)

# 合并多个表，并选取有用的字段
dfs = pd.concat(li)
dfs = dfs[['订单编号', '日期', '买家会员名', '买家实际支付金额', '订单状态', '收货人姓名', '收货地址 ', '联系手机', '宝贝标题 ', '宝贝总数量', '订单关闭原因']]

# 找出‘宝贝标题’中的‘产品型号’，并新增一列存放‘产品型号’
products = dfs['宝贝标题 '].map(lambda x:'+'.join(regex.findall(str(x))))
dfs.insert(9,'产品型号',products)

# 匹配‘产品型号’（实现Vlookup功能）
df_match = pd.read_excel(path_matchingTable+'//型号-类目匹配(去重).xlsx')
df_match['产品型号'] = df_match['产品型号'].astype(str)
result = pd.merge(dfs,df_match[['二级类目','三级类目','产品型号']],how='left',on=['产品型号'])

writer = pd.ExcelWriter(path_matchingTable+'//result.xlsx')
result.to_excel(writer,'数据',index=False)

#透视表，求各类目下的订单“总金额"及"平均金额"
pivot = pd.pivot_table(result, index=['二级类目','三级类目'],values=['买家实际支付金额'],aggfunc=[np.sum,np.mean])
pivot.to_excel(writer,'透视表')

writer.save()
