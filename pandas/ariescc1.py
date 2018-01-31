"""
pandas 基本介绍
"""

import numpy as np
import pandas as pd

series = pd.Series([1, 3, 6, np.nan, 44, 1])
print(series)

dates = pd.date_range('20190101', periods=6)
print(dates)


# **** 定义一个DataFrame ****

# index 定义行标号，未指明的话默认为0， 1， 2 。。。
# columns 定义列名称，未指明的话默认同上

# DataFrame 可以直接存储一个字典，key为列名称

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

print(df.dtypes)

print(df.index) # 打印序列号
print(df.columns) # 打印列名称
print(df.values) # 打印DataFrame的值

# 计算一些方差，最大最小值等等
print(df.describe())

# DataFrame 转置
print(df.T)

# 按行标号排序, axis = 1, ascending = False为倒序，反之为正序
# 按列标号排序, axis = 0, ascending = False为倒序，反之为正序
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=0, ascending=False))

# 对某列的值进行排序
print(df.sort_values(by='a'))

