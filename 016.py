import pandas as pd
import pathhelper as path

# 多表查询

students = pd.read_excel(path.join_curr('Students4.xlsx'), sheet_name='Students')
scores = pd.read_excel(path.join_curr('Students4.xlsx'), sheet_name='Scores')

# 拿 ID 列 连接成一张表

# 使用 merge 函数
table = students.merge(scores,
                       how='left',  # 保留左表（左连接 ; 默认是 innerJoin

                       # 联合的列的指定

                       # on='ID',  # 以ID列 join
                       # 当作有两张表要联合的列名字不一样时，可以这样
                       left_on='ID', right_on='ID'
                       # 也可以指定这一列的数据
                       # left_on=students.index, right_on=scores.index
                       # 当你什么都不指定时，merge函数会自己找左右两张表名字一样的 Series
                       ).fillna(0)

# 也可以使用 join 函数，用法和 merge 相似
# join 函数默认 联合的列 就是 index 列
students = students.set_index('ID')
scores = scores.set_index('ID')
table = students.join(scores,
                      how='left',  # 保留左表（左连接 ; 默认是 innerJoin
                      # 也可以显示指定 on
                      # 但是没有 left_on 和 right_on
                      ).fillna(0)

# 指定 table 列的格式
table['Score2017'] = table['Score2017'].astype(int)
table['Score2018'] = table['Score2018'].astype(int)
print(table)
