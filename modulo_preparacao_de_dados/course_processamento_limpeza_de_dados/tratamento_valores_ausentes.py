import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dataframe = pd.read_csv(url)

print(dataframe.isnull().sum())

# Estratégia 1: Remoção dos valores ausentes

dataframe_clean = dataframe.dropna()

print(dataframe_clean.head())

# Estratégia 2: Preenchimento de valores ausentes

dataframe["Age"] = dataframe["Age"].fillna(dataframe["Age"].mean())
print(dataframe["Age"].isnull().sum())