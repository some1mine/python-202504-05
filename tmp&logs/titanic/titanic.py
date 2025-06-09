import pandas as pd
import sklearn as sk

df = pd.read_csv('train.csv', index_col = 0, header = 0)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = df.drop('Name', axis = 1)

print('describe\n', df.describe())
print('describe\n', df.describe(include = 'all'))
print('head\n', df.head())

print(df.columns)
print(df['Survived'])


