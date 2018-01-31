import numpy as np

A = np.arange(4)
print(A)

# 传址
b = A
c = A
d = b

# 传值
bb = np.copy(A)

A[0] = 99

d[1: 3] = [22, 33]

print('bb', bb)
print(A)

print(b is A)
print(c is A)
print(b is c)
print(d is A)


