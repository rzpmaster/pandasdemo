import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path

# 饼图
students = pd.read_excel(path.join_curr('Students3.xlsx'), index_col='From')
print(students)
print(students.columns)

students['2017'].plot.pie(fontsize=8,
                          counterclock=False,  # 顺时针排
                          startangle=-270  # 开始角度
                          )
plt.title('Score of Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=16, fontweight='bold')
plt.show()
