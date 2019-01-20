import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\x\Desktop\pandas操作原数据\10、pie + heatmap\tips.csv"

df = pd.read_csv(path, engine='python', encoding='utf_8_sig')

sns.heatmap(df.corr(),annot=True)
plt.title('heatmap of df.corr()')
plt.show()

