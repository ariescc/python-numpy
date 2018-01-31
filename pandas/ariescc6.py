"""
pandas 合并多个DataFrame
"""

import numpy as np
import pandas as pd


# concatenating

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

#print(df1, df2, df3)

# axis=0上下合并，axis=1左右合并
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True) # ignore_index 将原来的序号忽略进行重新排号
print(res)


# join, ['inner', 'outer']

df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

print(df4, df5)
print(pd.concat([df4, df5], join='outer', ignore_index=True)) # 列不同，则将缺少的用nan补充(此时为默认情况outer)
print(pd.concat([df4, df5], join='inner', ignore_index=True)) # 列不同，则只保留两者共有的(此时为默认情况outer)

# 忘记就试试吧
print(pd.concat([df4, df5], axis=1, join_axes=[df4.index])) # 左右合并，并且以df4.index为基准，将df5多出来的行丢弃,多出来的列填充为nan


# append 竖向尾部添加数据

#print(df1.append(df2, ignore_index=True))
print(df1.append([df2, df3], ignore_index=True))

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(df1.append(s, ignore_index=True))

