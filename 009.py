import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path

# 柱状图 bar

students = pd.read_excel(path.join_curr('Students.xlsx'), index_col='ID')
students.sort_values(by='Score', inplace=True, ascending=False)
print(students)

# 使用 pandas 生成柱状图
# students.plot.bar(
#     # 横轴
#     x='Student',
#     # 纵轴
#     y='Score',
#     # 颜色
#     color=['orange', 'red'],
#     # 标题
#     title='it is title'
# )
# 紧凑型布局
# plt.tight_layout()
# 将制作好的图标 show 出来
# plt.show()

# 使用 plt 库 制图
plt.bar(
    # 横轴
    students['Student'],
    # 纵轴
    students['Score'],
    # 颜色
    color=['orange', 'red'],
)
# x轴标签旋转90度
plt.xticks(students['Student'], rotation=90)
# 轴名 标题名
plt.xlabel('Student')
plt.ylabel('Score')
plt.title('it is title', fontsize=16)

plt.tight_layout()
plt.show()
