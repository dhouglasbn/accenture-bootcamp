import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5]
y = [10, 20, 25, 30, 32]

# plt.plot(x,y)
# plt.show()

numbers = np.array([1,2,3,4,5])
result = numbers * 2
print(result)

data = {
  "product": ["Notebook", "Mouse", "Teclado"],
  "price": [3500, 120, 200]
}

dataframe = pd.DataFrame(data)
dataframe.to_csv("data.csv", index=False)

dataframe = pd.read_csv("data.csv")
print(dataframe)