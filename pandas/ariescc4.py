"""
pandas 处理丢失数据模块
"""

import numpy as np
import pandas as pd

dates = pd.date_range('20180101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A','B','C','D'])

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

# axis=0丢掉行，axis=1丢掉列
print(df.dropna(axis=0, how='all')) # how='any' 或者 'all'(all: 当前axis=0所有值均为nan才丢掉)

print(df.isnull())
print(np.any(df.isnull()) == True) # np.any() 矩阵里面至少有一个为True

print(df.fillna(value=0)) # 将nan赋值为0

