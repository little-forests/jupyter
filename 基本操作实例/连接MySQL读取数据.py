import pymysql
import pandas as pd

# 打开数据库连接
db = pymysql.connect('localhost','root','hyx.5899360','xian')
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT*FROM class;"
df = pd.read_sql(sql,db)
# 保存到Excel
df.to_excel(r"C:\Users\x\Desktop\class.xlsx",index=False)

# 关闭数据库
db.close()

