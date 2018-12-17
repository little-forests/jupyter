import pandas as pd
import numpy as np
import re

path_in = r"C:\Users\x\Desktop\测试\获取标题中的商品型号-原数据.xlsx"
path_out = r"C:\Users\x\Desktop\获取商品型号代码.xlsx"
df = pd.read_excel(path_in)
titleList = df['宝贝标题 ']

regex = re.compile(r'[A-Z]*\d{5}-?\d*[A-Z]?')
products = titleList.map(lambda x:'+'.join(regex.findall(str(x))))

df.insert(11,'商品型号',products)
df.to_excel(path_out,index=False)