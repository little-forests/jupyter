import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\x\Desktop\pandas操作原数据\9、bar（two subplots）\11.19.csv"

df = pd.read_csv(path,engine='python', encoding='utf_8_sig', usecols=[0,1,2,3,4,5,6],index_col=0,parse_dates=True)

sns.set(style='whitegrid')
fig, axes = plt.subplots(2,1)
df[df.columns[:4]].plot(ax=axes[0], figsize=[12,9])
df[df.columns[4:]].plot(ax=axes[1])

plt.show()