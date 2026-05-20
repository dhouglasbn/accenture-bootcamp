import datetime

now = datetime.datetime.now()

print("Script executado em: ", now)

def executar_relatorio():

  now = datetime.datetime.now()
  print("Gerando relatório...")
  print("Horário: ", now)

executar_relatorio()