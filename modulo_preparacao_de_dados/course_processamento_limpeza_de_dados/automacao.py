import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dataframe = pd.read_csv(url)

def limpar_dados(df):

  df["Age"] = df["Age"].fillna(df["Age"].mean())
  df["Age_log"] = df["Age"].apply(lambda x: x) # Copia da coluna Age

  df["Fare_normalized"] = (
    df["Fare"] - df["Fare"].min()
  ) / (df["Fare"].max() - df["Fare"].min())
  
  return df

limpar_dados(dataframe)
print(dataframe.head())

def validar_dataset(df):
  print("Linhas: ", df.shape[0])
  print("Colunas: ", df.shape[1])
  print("\nValores ausentes: \n", df.isnull().sum())

validar_dataset(dataframe)