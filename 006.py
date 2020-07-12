import pandas as pd
import pathhelper as path


# 函数填充,计算列

def add_two(x):
    return x + 2


# 打开Excel文件夹 (如果路径报错，先运行004)
books = pd.read_excel(path.join_desk('Books.xlsx'), index_col='ID')

# 这种遍历方式适合于,只计算序列中的一部分数据时
# for i in range(5, 10):
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# 需要全部计算时,可以直接出操作 Series ,一列数据乘一列数据
books['Price'] = books['ListPrice'] * books['Discount']
books['Price'] = books['Price'] + 2
books['Price'] = books['Price'].apply(add_two)
books['Price'] = books['Price'].apply(lambda x: x + 2)

print(books)
