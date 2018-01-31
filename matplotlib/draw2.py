"""
figure 设置
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)


# figsize 设置窗口大小（长：8， 宽：5）
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)

# linewidth 线宽，默认为1.0
# linestyle 线的样式
plt.plot(x, y1, linewidth=1.0, linestyle='--')

plt.show()

