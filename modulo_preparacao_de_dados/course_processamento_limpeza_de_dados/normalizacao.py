import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

dataframe = pd.read_csv(url)

# Transformação de variáveis

dataframe["Age"] = dataframe["Age"].fillna(dataframe["Age"].mean())
dataframe["Age_log"] = dataframe["Age"].apply(lambda x: x) # Copia da coluna Age
print(dataframe["Age_log"])

# Escala de dados (Normalização)
# Aqui normalizaremos a tarifa(Fare) passando de valor cobrado para percentual

dataframe["Fare_normalized"] = (dataframe["Fare"] - dataframe["Fare"].min()) / (dataframe["Fare"].max() - dataframe["Fare"].min())

print(dataframe.head())