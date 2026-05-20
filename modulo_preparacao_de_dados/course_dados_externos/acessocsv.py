import csv

data = [
  ['id', 'name', 'age', 'address'],
  [1, 'Alice Silva', 28, 'Rua A, 123'],
  [2, 'Bob Santos', 35, 'Rua B, 456'],
  [3, 'Carlos Oliveira', 42, 'Rua C, 789'],
  [4, 'Diana Costa', 31, 'Rua D, 321'],
  [5, 'Eduardo Lima', 26, 'Rua E, 654'],
  [6, 'Fernanda Souza', 39, 'Rua F, 987'],
  [7, 'Gabriel Pereira', 33, 'Rua G, 111'],
  [8, 'Helena Martins', 29, 'Rua H, 222'],
  [9, 'Igor Gomes', 45, 'Rua I, 333'],
  [10, 'Juliana Ferreira', 27, 'Rua J, 444']
]

with open('data.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(data)

with open('data.csv', 'r') as file:
  reader = csv.reader(file)
  for line in reader:
    print(line)