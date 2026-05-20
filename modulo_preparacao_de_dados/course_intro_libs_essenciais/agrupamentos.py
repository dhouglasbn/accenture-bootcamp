import pandas as pd
import matplotlib.pyplot as plt

data = {
  "product": ["Notebook", "Mouse", "Teclado"],
  "sales": [15, 50, 30]
}

dataframe = pd.DataFrame(data)
print(dataframe.groupby("product").mean())

plt.bar(dataframe["product"],dataframe["sales"])
plt.show()