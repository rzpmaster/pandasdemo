import pandas as pd
import pathhelper as path

# 将一行数据分为两行

employees = pd.read_excel(path.join_curr('Employees.xlsx'))
# 分两列
df = employees['Full Name'].str.split(
    # 用什么字符串切割字符串,默认为空
    ' ',
    # 最多保留多少个切出来的子字符串(如果是-1 或 0 ，意思是全部保留)(本例就是只能切出两个)
    n=2,
    # 拆分的时候直接就分为两列，默认为False
    expand=True
)
print(df)
# 讲df加到 最初的表格中
employees['First Name'] = df[0]
employees['Last Name'] = df[1].str.upper()

print(employees)
