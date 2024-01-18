def bubbleSort(list):
  n = len(list)
  for j in range(n-1):
    for i in range(n-1):
      if len(list[i]) < len(list[i+1]):
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
        
N = int(input())

for i in range(N):
  entrada = input().split()
  bubbleSort(entrada)
  print(' '.join(entrada))