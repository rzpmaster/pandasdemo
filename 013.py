import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path

# 折线图 叠加区域图
products = pd.read_excel(path.join_curr('Products.xlsx'), index_col='Week')
print(products)

products.plot.area(y=['Part1', 'Part2', 'Part3', 'Part4'])
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(products.index, fontsize=8)
plt.show()
