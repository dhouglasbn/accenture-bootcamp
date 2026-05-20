import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dataframe = pd.read_csv(url)

print(dataframe.head())
print(dataframe.info())
print(dataframe.describe())