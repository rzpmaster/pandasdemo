import pandas as pd
import pathhelper as path

# 创建文件

# 创建数据表 DateFrame 参数可以传 字典类型的参数
df = pd.DataFrame({'ID': [1, 2, 3, ], 'Name': ['zhangsan', 'lisi', 'wangwu']})
# 设置索引,set_index之后会产生一个新的df,同时可以消除第一列的默认生成的索引
df = df.set_index('ID')
print(df)
# 如果不设置索引,创建出来的excel会在第一列自动添加索引,设置索引后,则不会出现
# 默认是覆盖写入,如果文件不存在就创建一个
df.to_excel(path.join_desk('output.xlsx'))
# 但是如果路径不存在,再回报错
try:
    df.to_excel(path.join(path.desk_path, 'temp', 'output.xlsx'))
except Exception as e:
    print("报错啦~~~")
    print(e)
print('Done')
