import pandas as pd
import pathhelper as path

# 读取csv txt

students1 = pd.read_csv(path.join_curr('Students.csv'), index_col='ID')
print(students1)

# 无论是tsv,csv,txt 都用 read_csv 读取，但是要指定 分隔字符
students2 = pd.read_csv(path.join_curr('Students.txt'),
                        # 分隔字符
                        sep='\t',
                        index_col='ID'
                        )
print(students2)
