import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('your_file.csv')

# 计算每行中 NA 值的比例
na_percentage = df.isna().sum(axis=1) / df.shape[1]

# 选择 NA 值比例小于 20% 的行
selected_rows = df.loc[na_percentage < 0.2]

# 打印选定的行
print(selected_rows)
