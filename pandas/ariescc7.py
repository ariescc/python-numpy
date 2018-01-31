"""
pandas 合并 merge
"""

import pandas as pd

left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

print('----------------------------')

#res = pd.merge(left, right, on='key')

# how=['outer', 'inner', 'left', 'right']

res = pd.merge(left, right, on=['key1', 'key2'], how='inner') # how=inner两个key完全相同
print(res)

