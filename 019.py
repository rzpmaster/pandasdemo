import pandas as pd
import pathhelper as path

# 求和 统计

students = pd.read_excel(path.join_curr('Students6.xlsx'))
temp = students[['Test_1', 'Test_2', 'Test_3']]
print(temp)
print('-' * 50)

# 计算一列的合
result = temp.sum()
print(result)
# 他的类型是Series
print(type(result))

# 计算一行的合
row_sum = temp.sum(axis=1)
row_meam = temp.mean(axis=1)
print(row_sum)
print(row_meam)

students['Total'] = row_sum
students['Average'] = row_meam
col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
# append 追加一行
students = students.append(col_mean,
                           # 对齐列，不给会报错
                           ignore_index=True
                           )

print(students)
