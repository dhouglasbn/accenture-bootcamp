# Pipeline
# processo automatizado que executa várias etapas
# 1. coleta de dados
# 2. processamento
# 3. análise
# 4. geração de resultados

import pandas as pd

def pipeline_restaurante():
  url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

  df = pd.read_csv(url)
  total_tips = df["tip"].sum()
  # tips_per_day = df.groupby("day")["tip"].sum()
  report = pd.DataFrame({
    "total_gorjetas": [total_tips] })
  
  report.to_csv("relatorio_gorjetas.csv", index=False)

  print("Pipeline executado com sucesso")
  print("Total de gorjetas: ", total_tips)

pipeline_restaurante()