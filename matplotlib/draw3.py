"""
坐标轴设置
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

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$very\ good$'])

plt.show()

