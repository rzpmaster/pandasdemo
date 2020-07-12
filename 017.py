import pandas as pd
import pathhelper as path


# 数据校验

def score_validation(row):
    """
    验证一行数据的乘成绩是否合格
    :param row:
    """

    # 使用assert语句
    # try:
    #     assert 0 <= row.Score <= 100
    # except:
    #     print(f'#{row.ID} student {row.Student} has as invalid score {row.Score}.')

    # 使用if语句
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID} student {row.Student} has as invalid score {row.Score}.')


students = pd.read_excel(path.join_curr('Students5.xlsx'))
print(students)

students.apply(score_validation,
               # DataFrame 有两个方向， 从上到下 轴是1 从左到右 轴是2
               axis=1
               )
