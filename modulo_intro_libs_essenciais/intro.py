import numpy as np # computação numérica e arrays
import pandas as pd # manipulação de dados em tabelas
import matplotlib.pyplot as plt # gráficos

# Repare que o array do numpy exibe sem virgulas
array = np.array([1, 2, 3, 4, 5])
print(array)

data = {
  "name": ["Ana", "Carlos", "Maria"],
  "idade": [25, 30, 20]
}

dataframe = pd.DataFrame(data)
print(dataframe)