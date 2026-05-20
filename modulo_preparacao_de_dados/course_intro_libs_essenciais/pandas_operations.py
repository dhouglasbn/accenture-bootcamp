import pandas as pd

data = {
  "product": ["Notebook", "Mouse", "Teclado"],
  "price": [3500, 120, 200]
}

dataframe = pd.DataFrame(data)
print(dataframe["price"]) # series

print(dataframe["price"].mean()) # series average

print(dataframe["product"].count()) # series count

print(dataframe.describe())
print(dataframe.product)