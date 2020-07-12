import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path

# 分组柱图
students = pd.read_excel(path.join_curr('Students2.xlsx'), index_col='ID')
students.sort_values(by='Score2018', inplace=True, ascending=False)
print(students)

students.plot.bar(
    x='Student',
    # 分组数据放在集合中
    y=['Score2017', 'Score2018'],
    # 2017orange 2018red
    color=['orange', 'red']
)

plt.title('StudentByScore', fontsize=16, fontweight='bold')
plt.xlabel('Student', fontweight='bold')
plt.ylabel('Score', fontweight='bold')

# 修改轴信息
ax = plt.gca()
ax.set_xticklabels(
    students['Student'],
    rotation=45,
    # 水平对齐
    ha='right'
)

# 修改图形信息
f = plt.gcf()
f.subplots_adjust(left=0.2, bottom=0.42)

plt.tight_layout()
plt.show()
