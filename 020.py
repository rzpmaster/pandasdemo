import pandas as pd
import pathhelper as path

# 去除重复

students = pd.read_excel(path.join_curr('Students7.xlsx'))

# 1 找到那些重复的数据
dupe = students.duplicated(
    subset='Student',
)
print(dupe)
print(dupe.any())
print(type(dupe))
dupe = dupe[dupe == True]
print(dupe.index)
print(students.iloc[dupe.index])

# 2 去重
students.drop_duplicates(
    # 基于那一列去重
    subset='Student',
    inplace=True,
    # 如果有重复的，是保留前面的还是后面的，默认为前面的
    keep='last'
)
print('-' * 50)
print(students)
