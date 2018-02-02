"""
最小二乘拟合
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

# 设置中文字体，否则绘制的图中无法显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

#plt.figure(figsize=(9, 9))
x = np.linspace(0, 10, 1000)
X = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Y = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])
# 计算以p为参数的直线和原始数据之间的误差
def f(p):
    k, b = p
    return (Y - (k*X+b))


#Leastsq使得f的输出数组的平方和最小，参数初始值为[1,0]
r = leastsq(f, [1, 0])
#print(r)
k, b = r[0]
print('k = ', k, 'b = ', b)

plt.scatter(X, Y, s=100, alpha=1.0, marker='o', label=u'数据点')

y = k*x + b

# get current axis
ax = plt.gca()

# 设置坐标轴标签字体大小
ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)

plt.plot(x, y, color='r', linewidth=5, linestyle=':', markersize=20, label=u'拟合曲线')

plt.legend(loc=0, numpoints=1)

leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'安培/A')
plt.ylabel(u'伏特/V')

plt.xlim(0, x.max() * 1.1)
plt.xlim(0, y.max() * 1.1)

# 刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.legend(loc='best')

plt.show()

