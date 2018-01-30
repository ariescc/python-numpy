import numpy as np

a = np.arange(2, 14).reshape( (3, 4) )

print(a)

print(np.argmin(a)) # 获取所有元素的最小值的索引
print(np.argmax(a)) # 获取所有元素的最大值的索引

print(np.mean(a)) # 求所有元素的平均值, axis = 1对行计算平均值，axis=0对列计算
print(np.average(a)) # 求所有元素的平均值

print(np.median(a)) # 求所有元素的中位数

print(np.cumsum(a)) # 前面数累计

print(np.diff(a)) # 当前数和下一个数做差

print(np.nonzero(a)) # 找出非0的数(输出两个数组<第一个表示非0数的行数，第二个表示非0数的列数>)

b = np.arange(14, 2, -1)

print(b)
print(np.sort(b))

print(np.transpose(a)) # 矩阵的转置

print(np.clip(a, 5, 9)) # 所有小于5的数等于5， 所有大于9的数等于9， 5和9之间的数保持不变


