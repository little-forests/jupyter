import pandas as pd
import numpy as np

x = [2,5,1,3,4,1,5,3,4,2]
y = [50,57,41,54,54,38,63,48,59,46]
s1 = pd.Series(x)
s2 = pd.Series(y)
corr = s1.corr(s2)
print(corr)