import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import pathhelper as path

# 线性回归

sales = pd.read_excel(path.join_curr('Sales.xlsx'), dtype={'Month': str})
print(sales)

# 回归方程
# slope 斜率  intercept y轴截距
slope, intercept, r, p, std_err = linregress(sales.index,
                                             sales['Revenue']
                                             )

exp = sales.index * slope + intercept

# 柱状图
plt.scatter(sales.index, sales['Revenue'])
plt.plot(sales.index, exp, color='orange')
plt.title(f"y={slope}*x+{intercept}")
plt.xticks(sales.index, sales['Month'], rotation=90)
plt.tight_layout()
plt.show()
