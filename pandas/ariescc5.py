"""
pandas 导入导出
"""

import pandas as pd

"""
可以读取哪些类型的文件：
    read_csv
    read_excel
    read_hdf
    read_sql
    read_json
    read_msgpack
    read_html
    read_gbq
    read_stata
    read_sas
    read_clipboard
    read_pickle
"""

data = pd.read_excel('data.xls')

print(data)

# DataFrame 导出
data.to_csv('out.csv')

