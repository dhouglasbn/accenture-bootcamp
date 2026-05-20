import logging

logging.basicConfig(level=logging.INFO)

def processar_dados():
  logging.info("Processamento iniciado")

  sales = [100, 200, 150]

  total = sum(sales)

  logging.info("Total calculado: %s", total)

processar_dados()