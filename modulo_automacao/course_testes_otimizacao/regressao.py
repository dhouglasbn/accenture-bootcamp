import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

df = df.dropna()

x = df.drop("median_house_value", axis=1)
x = pd.get_dummies(x) # transforma categorias em representações numéricas
y = df["median_house_value"]

x_train, x_test, y_train, y_test = train_test_split(
  x, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
residuos = y_test - y_pred

plt.figure(figsize=(6,5))
plt.scatter(y_pred, residuos)
plt.axhline(0, color="red")
plt.xlabel("Valores Preditos")
plt.ylabel("Resíduos")
plt.title("Resíduos vs Valores Preditos")
plt.show()

plt.figure(figsize=(6,5))
sns.histplot(residuos, kde=True)
plt.title("Distribuição dos resíduos")
plt.show()

# MAE (Mean Absolute Error)
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
print(mae)

# MSE (Mean Squared Error)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(mse)

# RMSE (Root Mean Squared Error)
rmse = np.sqrt(mse)
print(rmse)

# MAPE (Mean Absolute Percentage Error)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print(mape)

# Coeficiente de determinação
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(r2)

metrics = pd.DataFrame({
  "MAE":[mae],
  "MSE":[mse],
  "RMSE":[rmse],
  "R2":[r2],
})

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="red")
plt.xlabel("Valor Real")
plt.ylabel("Valor Predito")
plt.title("Valores Reais vs Preditos")
plt.show()