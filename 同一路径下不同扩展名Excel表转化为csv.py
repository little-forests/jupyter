import pandas as pd
import numpy as np
import os

path = r"C:\Users\x\Desktop\pandas操作原数据\3、同一路径下不同扩展名Excel表转化为csv-原数据"

l = ['.xlsx','.xls']
for filename in os.listdir(path):
    os.chdir(path)
    extension = os.path.splitext(filename)[1]
    if extension in l:
        df = pd.read_excel(filename)
        #订单编号中数字超过15位，直接用str()进行处理，末位会变成0
        df['订单编号'] = df['订单编号'].map(lambda x: '="'+str(x)+'"')
    elif extension == '.csv':
        df = pd.read_csv(filename,engine='python')
        
    df.to_csv(r"C:\Users\x\Desktop\新表"+'//'+os.path.splitext(filename)[0]+'.csv',index=False,encoding='utf_8_sig')
