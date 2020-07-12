import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path


# 数据筛选 过滤

def age_18_to_30(a):
    return 18 <= a <= 30


def score_85_to_100(s):
    return 85 <= s <= 100


students = pd.read_excel(path.join_curr('Students.xlsx'), index_col='ID')

# 筛选数据
# 在使用 loc 特性(loc不是函数,要用[]) 之后,会产生一个新的 DataFrame
# 注意,这里使用 \ 可以将很长的代码分行显示
students = students.loc[students['Age'].apply(age_18_to_30)] \
    .loc[students['Score'].apply(score_85_to_100)]

# 介绍一种 python 特有的语法, ['Age']可以用 .Age 代替,代价是无法使用自动提示
students = students.loc[students.Age.apply(lambda a: 18 <= a <= 30)] \
    .loc[students.Score.apply(lambda s: 85 <= s <= 100)]

# 制图
students.plot.bar()
plt.show()

print(students)


