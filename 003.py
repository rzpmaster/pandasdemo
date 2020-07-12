import pandas as pd

# 行 列(Series,序列) 单元格(序列的交叉点) 入门

# # Dictionary
# d = {'x': 100, 'y': 200, 'z': 300}
# print(d.keys())
# print(d.values())
# print(d['x'])
#
# # 序列,由字典构造 index(key) data(value)
# s1 = pd.Series(d)
# print(s1)
# print(s1.index)
#
# # 序列,由index和data集合构造
# L1 = [100, 200, 300]
# L2 = ['x', 'y', 'z']
# s1 = pd.Series(L1, index=L2)
# print(s1)


# 开始将序列放入 DataFrame 中
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 4], name='C')
# Series 和 DataFrame 都有index,在构造 DataFrame 时,会将index对齐,空白的是NaN

# 将s1 s2 s3当成列,需要把他们当成dic添加
df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
print(df)

# 将s1 s2 s3当成行,需要把他们当成list添加
print('-' * 50)
df = pd.DataFrame([s1, s2, s3])
print(df)

print('Done!')
