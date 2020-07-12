import pandas as pd
import matplotlib.pyplot as plt
import pathhelper as path

# 叠加柱状图 横向柱状图
users = pd.read_excel(path.join_curr('Users.xlsx'), index_col='ID')
# 排序，用增加一列（三个月之和）的数据
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=True)
print(users)

users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'],
                stacked=True,  # 叠加柱状图
                title='User Behavior'
                )

plt.tight_layout()
plt.show()
