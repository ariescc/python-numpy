import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

c = a - b # a\b元素逐个相减
d = a + b

e = b**2 # 求b每个元素的平方

f = 10*np.sin(a) # 求a每个元素的sin值(其他三角函数同)

#print(b < 3) # 判断b中哪些元素小于3

#print(b == 3)

g = np.array([[10, 20],
              [11, 12]])
h = b.reshape( (2, 2) )

c1 = g*h # 元素逐个直接相乘
c_dot = np.dot(h, g) # 两个矩阵进行标准的矩阵乘法

#print(c1)
#print(c_dot)

arr = np.random.random( (2, 4) ) # 随机生成一个2行4列的矩阵，每个元素的值在(0, 1)之间
print(arr)

print(np.sum(arr)) # 矩阵所有元素相加求和
print(np.sum(arr, axis=1)) # axis=1 行求和， axis=0 列求和
print(np.max(arr)) # 矩阵所有元素的最大值， axis参数同上
print(np.min(arr)) # 矩阵所有元素的最小值， axis参数同上



