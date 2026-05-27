import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

plt.figure(figsize=(8, 5))

plt.bar(df["day"], df["tip"], color="green")
plt.title("Gorjetas por dia")

plt.xlabel("Dia")
plt.ylabel("Gorjeta")

plt.show()

fig, ax = plt.subplots(1,2, figsize=(10,4))

sns.histplot(df["total_bill"], ax=ax[0])
ax[0].set_title("Distribuição da Conta")

sns.boxplot(data=df, x="day", y="tip", ax=ax[1])
ax[1].set_title("Gorjetas por dia")

plt.show()