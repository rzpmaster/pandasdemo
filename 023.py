import pandas as pd
import numpy as np
import pathhelper as path

# 数据透视表

pd.options.display.max_columns = 999
orders = pd.read_excel(path.join_curr('Orders.xlsx'))
# 新增一列
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
print(orders)
print(orders['Date'].dtype)

# 透视表

# pivot_table
print('-' * 50)
pt1 = orders.pivot_table(index='Category',
                         columns='Year',
                         values='Total',
                         aggfunc=np.sum
                         )
print(pt1)

# group by
print('-'*50)
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()

pt2 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt2)
