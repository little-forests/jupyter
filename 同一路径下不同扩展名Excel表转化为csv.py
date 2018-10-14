import pandas as pd
import numpy as np
import os

path_in = r"C:\Users\x\Desktop\同一路径下不同扩展名Excel表转化为csv-原数据"
path_csv = r"C:\Users\x\Desktop\Excel表转化为csv"
list = os.listdir(path_in)
os.chdir(path_in)
for filename in list:
    extension = os.path.splitext(filename)[1]
    if extension == '.xlsx' or extension == '.xls':
        df = pd.read_excel(filename)
        #订单编号中数字超过15位，直接用str()进行处理，末位会变成0
        df['订单编号'] = df['订单编号'].map(lambda x:'="'+str(x)+'"')
    elif extension == '.csv':
        df = pd.read_csv(filename, engine='python')
    #或者path_out = os.path.join(path_csv, os.path.splitext(filename)[0]+'.csv')
    df.to_csv(path_csv+'\\'+os.path.splitext(filename)[0]+'.csv',index=False,encoding='utf_8_sig')
