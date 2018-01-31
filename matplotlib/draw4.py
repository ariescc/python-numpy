"""
坐标轴设置(修改坐标轴的位置)
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y1, linewidth=2.0, linestyle='--')
plt.plot(x, y2)

# x,y轴的取值范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

plt.xlabel('I am X.')
plt.ylabel('I am Y.')

#new_ticks = np.linspace(-1, 2, 5)
#plt.xticks(new_ticks)
#plt.yticks([-2, -1.8, -1, 1.22, 3],
#           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$very\ good$'])


# gca = 'get current axis'
ax = plt.gca()
# spines 为图的四个边框，上下左右
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0)) # x 轴放在y轴-1的位置
ax.spines['left'].set_position(('data', 0))

"""
标出点(x0, y0)的位置信息，画出一条垂直与x轴的虚线
"""
x0 = 1
y0 = x0**2
plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)

# 在(x0, y0)点处加一个蓝色的原点，原点大小为50
plt.scatter([x0,],[y0,], s=50, color='Red')

"""
对(x0, y0)点进行标注
"""
plt.annotate(r'x^2=%s' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

plt.title('draw test')

plt.show()

