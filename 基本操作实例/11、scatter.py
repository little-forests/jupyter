import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\x\Desktop\pandas操作原数据\11、scatter\housing.csv"
housingV = pd.read_csv(path, engine='python', encoding='utf_8_sig')

sns.set(style='white')
# s-size, c-color, cmap-colormap
housingV.plot(kind='scatter', x='longitude', y = 'latitude', alpha=0.4,
              s=housingV.population/100, label='population',
              c='median_house_value', cmap=plt.get_cmap('jet'))
plt.show()