def calcuLarValorHash(casosDeTeste):
  valor_hash = 0
  for i, linha in enumerate(casosDeTeste):
    for j, char in enumerate(linha):
      posicao_no_alfabeto = ord(char) - ord('A')
      valor_hash += posicao_no_alfabeto + i + j
  return valor_hash

N = int(input())
for i in range (N):
  L = int(input())
  casos_de_teste = []
  for _ in range(L):
    linha = input().strip()
    casos_de_teste.append(linha)

  valor_hash = calcuLarValorHash(casos_de_teste)
  print(valor_hash)