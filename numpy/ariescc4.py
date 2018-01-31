import numpy as np

a = np.arange(3, 15).reshape( (3, 4) )

print(a)

# 下面两种索引相同
print(a[1][1])
print(a[2, 1])

# 第二行的所有数
print(a[2][:])

# 第二行的第一列到第二列的数
print(a[2][1:3])

# 对列进行迭代，将矩阵a进行转置为a.T
for col in a.T:
    print(col)

# 将a化为一个列表
print(a.flatten())

# 遍历 矩阵a 的每一个元素值
for item in a.flat:
    print(item)

