"""
numpy array 的合并
"""

import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack( (A, B) ) # 两个矩阵水平合并，即上下合并
D = np.hstack( (A, B) ) # 两个矩阵垂直合并，即左右合并

# A 为一维矩阵，所以显示的shape显示的一个参数就是一维矩阵中元素的个数(3,)。
# C 为 A、B两个矩阵合并后的矩阵，合并后为2行3列矩阵，所以显示的shape为(2, 3)
print(A.shape, C.shape)
print(A.shape, D.shape)

print(A[np.newaxis, :]) # 将A行向增加一个维度
print(A[:, np.newaxis]) # 将A列向增加一个维度

print(A) # 不可以转置
print(A[np.newaxis, :].T) # 多了一维可以转置

AA = np.array([1, 1, 1])[:, np.newaxis]
BB = np.array([2, 2, 2])[:, np.newaxis]

print(AA, BB)

# axis = 0,矩阵进行上下合并。
# axis = 1,矩阵进行左右合并。
CC = np.concatenate( (AA, BB, BB, AA), axis=1 )
print(CC)

