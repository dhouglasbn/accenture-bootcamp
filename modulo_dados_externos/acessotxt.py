with open('hello_world.txt', 'w') as file:
  file.write('This is my first write file in python\n')
  file.write('Hello, World!')

with open('hello_world.txt', 'r') as file:
  content = file.read()

print(content)