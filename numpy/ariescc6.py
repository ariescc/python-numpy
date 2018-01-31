"""
numpy array 的分割
"""

import numpy as np


A = np.arange(12).reshape( (3, 4) )
print(A)


# *** split 不能进行不等的分割 ***

# axis = 1, 纵向分割
# axis = 0, 横向分割

print(np.split(A, 2, axis=1))
print(np.hsplit(A, 2))

print(np.split(A, 3, axis=0))
print(np.vsplit(A, 3))

# *** array_split 进行不等的分割（第一个分割为多余部分） ***

print(np.array_split(A, 3, axis=1))

