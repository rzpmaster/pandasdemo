import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path

# 散点图 直方图

# 显示最大列数
pd.options.display.max_columns = 10

homes = pd.read_excel(path.join_curr('Home_datas.xlsx'))
print(homes.head())

# 散点图
# homes.plot.scatter(x='price', y='sqft_living')
# plt.show()

# 直方图
# homes['sqft_living'].plot.hist(
# #     bins=100  # 桶的个数
# # )
# # # 设置横轴范围（从0到最大值，步长500）
# # plt.xticks(range(0, max(homes['sqft_living']), 500), fontsize=8, rotation=90)
# # plt.show()

# 密度图
homes['sqft_living'].plot.kde()
plt.xticks(range(0, max(homes['sqft_living']), 500), fontsize=8, rotation=90)
plt.show()


# 其他 pandas 的数据分析功能

# 两列的相关性
print('-' * 50)
print(homes.corr())
