import numpy as np

ls = [2, 23, 4]

# 创建numpy的一维array
#a = np.array([2, 23, 4], dtype=np.int32) #默认为int64(int32, float32)

#a = np.array([[2, 23, 4],
#             [2, 43, 5]])

# numpy 的 array 打印出来没有逗号，list的打印出来有逗号
#print(a.dtype)

# 创建全0矩阵
a = np.zeros( (3, 4) ) # 生成3行 4列 的全0数组
b = np.ones( (3, 4) ) # 生成3行 4列 的全1数组
c = np.empty( (3, 4) ) # 生成3行 4列 的empty数组，每个元素的值为很小的接近0的值
d = np.arange(10, 20, 2) # 生成一个有序数列，起始值为10， 最大值为20(开区间)，步长为2  => [10 12 14 16 18]

e = np.arange(12).reshape( (3, 4) ) # 将序列转换成3行4列矩阵
f = np.linspace(1, 10, 20).reshape( (4, 5) )
print(f)

