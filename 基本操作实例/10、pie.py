import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

path = r"C:\Users\x\Desktop\pandas操作原数据\10、pie + heatmap\tips.csv"
df = pd.read_csv(path, engine='python', encoding='utf_8_sig')

day = df.groupby('day').size()

sns.set()
day.plot(kind='pie', title='Number of parties on different days', autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*day.sum()))
plt.show()
