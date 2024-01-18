def hash_function(key, table_size):
  return key % table_size

def insert(table, key, value):
  index = hash_function(key, len(table))
  if table[index] is None:
    table[index] = [value]
  else:
    table[index].append(value)

def print_table(table):
  for index, values in enumerate(table):
    print(f"{index} ->", end=" ")
    if values is not None:
      print(" -> ".join(map(str, values)), "->", end=" ")
    print("\\")

N = int(input())
for _ in range(N):
  M, C = map(int, input().split())

  # Inicializa a tabela como uma lista de listas vazias
  table = [None] * M

  # Leitura das chaves e inserção na tabela
  keys = list(map(int, input().split()))
  for key in keys:
    insert(table, key, key)

  print_table(table)
  if _ < N - 1:
    print()