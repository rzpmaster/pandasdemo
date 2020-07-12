import pandas as pd
from datetime import date, timedelta
import pathhelper as path


# 单元格 拖拽填充

def add_month(g_date, month_delta):
    """
    计算时间,计算给定时间加上指定月 (12进制)后的时间
    :param g_date:给定时间
    :param month_delta:要加上的月的个数
    :return:返回相加后的时间
    """
    # 要加上的月份是否超过1年
    year_delta = month_delta // 12

    # 月份要加上不足一年的部分,注意这里可能大于12,需要再判断一次
    month = g_date.month + month_delta % 12
    if month != 12:
        year_delta += month // 12
        month = month % 12

    return date(g_date.year + year_delta, month, g_date.day)


# 打开Excel文件夹
books = pd.read_excel(path.join_curr('Books.xlsx'),
                      # 跳过空行
                      skiprows=9,
                      # 取哪几列,不分大小写
                      usecols="j:p",
                      # index
                      index_col=None,
                      # 设置列数据的默认类型,大小写敏感
                      dtype={'ID': str, 'InStore': str, 'Date': str}
                      )

# 循环填充单元格

# 修改单元格数值的方法(实际上就是改 Series 中的值)
# books['ID'].at[0] = 100
# print(books['ID'])

# DataFrame 怎么迭代?
# books.index 可以获取 一个RangeIndex() ,他的大小正好等于 DataFrame 的行数
# 也可以自己自定义迭代某些行,比如 range(5,15)
# print(books.index)

# 定义开始的日期
start = date(2018, 1, 1)
# 循环填充列数据
for i in books.index:
    books['ID'].at[i] = i + 1  # 如果单元格中没有值,默认是NaN,类型是float64
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    # 日期 ,在days上加1 (timedelta有 毫秒ms 到 天day )
    books['Date'].at[i] = start + timedelta(days=i)
    # 日期加年 ,重新构造日期,使用start的月份和日
    books['Date'].at[i] = date(start.year + i, start.month, start.day)
    # 日期加月
    books['Date'].at[i] = add_month(start, i)
    # ListPrice
    books['ListPrice'].at[i] = books['ID'].at[i] * 10
    # Discount
    books['Discount'].at[i] = 0.5

# 最后,再提供以重修改单元格的办法(直接对 DataFrame 进行修改)
# for i in books.index:
#     # 直接修改,第i行,第几列的数据
#     books.at[i, 'ID'] = i + 100

# 输出Excel
books.set_index('ID', inplace=True)
books.to_excel(path.join_desk('Books.xlsx'))

print(books)
