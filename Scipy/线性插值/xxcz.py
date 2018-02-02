"""
线性插值
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 2*np.pi + np.pi/4, 10)
y = np.sin(x)

x_new = np.linspace(0, 2*np.pi + np.pi/4, 100)
f_linear = interpolate.interp1d(x, y)
tck = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, tck)

plt.xlabel(u'安培/A')
plt.ylabel(u'电压/V')

plt.plot(x, y, marker='o', label=u'原始数据')
plt.plot(x_new, f_linear(x_new), label=u'线性插值')
plt.plot(x_new, y_bspline, label=u'B-spline插值')

plt.legend(loc='best')
plt.show()

