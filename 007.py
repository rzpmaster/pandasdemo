import pandas as pd
import pathhelper as path

# 排序 多重排序

products = pd.read_excel(path.join_curr('List.xlsx'), index_col='ID')

# 按价格排序
products.sort_values(
    # 需要排序的列名
    by='Price',
    # 为True时,仅在当前 DataFrame 中排序,不会生成新的
    inplace=True,
    # 默认为True,表示小到大 (boolean类型,给0 1 也行)
    ascending=False
)

# 如果需要同时以两个维度排序,不能连续用两次 sort_values
# 只能在一次 sort_values 按两个维度排
products.sort_values(
    # 先按值不值排序,再按价格排序
    by=['Worthy', 'Price'],
    inplace=True,
    # ascending 参数与上面 by 对应
    ascending=[True, False])

print(products)
