"""
pandas 选择数据
"""

import numpy as np
import pandas as pd

dates = pd.date_range('20180101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df['A'], df.A)

# 选择0-3行
print(df[0:3], df['20180104': '20180106'])

# 通过标签来选择
print(df.loc['20180102'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20180102', ['A', 'B']])

# 通过位置来选择，选择3-5行，1-3列
print(df.iloc[3:5, 1:3])

# 混合选择
print(df.ix[:3, ['A', 'C']])

# 逻辑选择，是或否
# 筛选 A > 8的行（会将一整行数据打印出来）
print(df)
print(df[df['A'] > 8])

