"""
pandas plot 画图

数据可视化
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# plot data


# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum() # 数据累加

# DataFrame

data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list('ABCD'))
data = data.cumsum()
print(data.head())

"""
plot method:

    bar
    hist
    box
    kde
    area
    scatter
    hexbin
    pie

"""

ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class one')
bx = data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class two', ax=ax)
data.plot.scatter(x='A', y='D', color='Yellow', label='Class three', ax=bx)
plt.show()

