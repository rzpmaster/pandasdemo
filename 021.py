import pandas as pd
import pathhelper as path

# 行列转换

pd.options.display.max_columns = 12
videos = pd.read_excel(path.join_curr('Videos.xlsx'), index_col='Mouth')
table = videos.transpose()
print(table)
