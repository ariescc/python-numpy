"""
pandas 给选定位置赋值
"""

import numpy as np
import pandas as pd

dates = pd.date_range('20180101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[2, 2] = 1111
df.loc['20180104', 'B'] = 2222


# 注意下面两种效果，第一个当前行所有数均被赋值为0
#df[df['A'] > 4] = 0
df['B'][df['A'] > 4] = 0
df.B[df.A > 4] = 0

df['F'] = np.nan

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20180101', periods=6))

print(df)

