import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

plt.scatter(df["total_bill"], df["tip"])
plt.xlabel("Conta total")
plt.ylabel("Vaor da gorjeta")
plt.title("Relação entre conta e gorjeta")

plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip")
plt.show()

fig = px.scatter(
  df,
  x="total_bill",
  y="tip",
  color="day",
  title="Relação entre conta e gorjeta"
)

fig.show()