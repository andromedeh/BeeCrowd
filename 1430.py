jingle = input()
while jingle != '*':
  soma = 0
  contador = 0
  
  for char in jingle:
    if char == '/':
      if soma == 1:
        contador +=1
      soma = 0
    elif char == 'W':
      soma += 1
    elif char == 'H':
      soma += 1/2
    elif char == 'Q':
      soma += 1/4
    elif char == 'E':
      soma += 1/8
    elif char == 'S':
      soma += 1/16
    elif char == 'T':
      soma += 1/32
    elif char == 'X':
      soma += 1/64
      
  print(contador)
  jingle = input()