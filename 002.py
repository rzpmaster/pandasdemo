import pandas as pd
import pathhelper as path

# 打开文件

# 读取excel数据 （如果路径报错，先运行001）
people = pd.read_excel(path.join_desk('output.xlsx'), header=0)
# 如果 header=None 直接读出来会在第一行和第一列加上默认的index
# 可以指定 header=1 属性确定列头是第1行的数据
# print(people)

# 表格的大小
print(people.shape)
# 表格的列名
print(people.columns)

# 打印前几行
# print(people.head(3))
# print('-' * 50)
# print(people.tail(3))


# 如果文件没有标题,可以自行设置,要提前让pandas不要读标题
print('-' * 50)
people = pd.read_excel(path.join_desk('output.xlsx'), header=None)
people.columns = ['序号', '姓名']
print(people)
# 这里第一列会有自动生成的索引,去除办法除了 set_index()之外,还可以
# people = people.set_index("序号")
people.set_index("序号", inplace=True)
# 副作用是,你设置完 index 参数之后, columns 中也就看不到 "序号" 了
print()
print(people.columns)
people.to_excel(path.join_desk('output2.xlsx'))

# 再次读取 发现 index 还在!!! "序号"又被当成普通列了
df = pd.read_excel(path.join_desk('output2.xlsx'))
print('-' * 50)
print(df.head())
df.to_excel(path.join_desk('output3.xlsx'))
# 解决办法,在读取的时候,直接就把index设置了
df = pd.read_excel(path.join_desk('output2.xlsx'), index_col=0)
print('-' * 50)
print(df.head())
df.to_excel(path.join_desk('output3.xlsx'))
print('Done!')
