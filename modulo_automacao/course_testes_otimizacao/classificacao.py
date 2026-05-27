import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

df_class = df.copy()
df_class["HighPrice"] =(
  df_class["median_house_value"] >
  df_class["median_house_value"].median()
).astype(int)

x = df_class.drop(["median_house_value", "HighPrice"], axis=1)
x = pd.get_dummies(x)
y = df_class["HighPrice"]

x_train, x_test, y_train, y_test = train_test_split(
  x, y, test_size=0.2, random_state=42
)

# Regressão Logística
# modela probabilidade de pertencimento a uma classe

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(max_iter=1000)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

# Matriz de Confusão
# compara valores reais com valores previstos
# True Positive, True Negative, False Positive, False Negative

plt.figure(figsize=(6,5))

sns.heatmap(
  cm,
  annot=True,
  fmt="d",
  cmap="Blues"
)
plt.xlabel("Classe Predita")
plt.ylabel("Classe Real")
plt.title("Matriz de Confusão")
plt.show()

# Acurácia
# proporção de previsões corretas
