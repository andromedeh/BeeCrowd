class NodoArvore:

  def __init__(self, chave=None, esq=None, dir=None):
    self.chave = chave
    self.esq = esq
    self.dir = dir


def inserirABB(raiz, item):
  if raiz is None:
    raiz = item

  elif raiz.chave < item.chave:
    if raiz.dir is None:
      raiz.dir = item
    else:
      inserirABB(raiz.dir, item)

  else:
    if raiz.esq is None:
      raiz.esq = item
    else:
      inserirABB(raiz.esq, item)

def pre_ordem(raiz):
  if not raiz:
      return ""
  result = str(raiz.chave)
  if raiz.esq:
      result += " " + pre_ordem(raiz.esq)
  if raiz.dir:
      result += " " + pre_ordem(raiz.dir)
  return result

def em_ordem(raiz):
  if not raiz:
      return ""
  result = ""
  if raiz.esq:
      result += em_ordem(raiz.esq) + " "
  result += str(raiz.chave)
  if raiz.dir:
      result += " " + em_ordem(raiz.dir)
  return result

def pos_ordem(raiz):
  if not raiz:
      return ""
  result = ""
  if raiz.esq:
      result += pos_ordem(raiz.esq) + " "
  if raiz.dir:
      result += pos_ordem(raiz.dir) + " "
  result += str(raiz.chave)
  return result

C = int(input())  # le o numero de casos de teste
for n in range(C):
  N = int(input())  # qtd de nos da arvore
  nos = list(map(int, input().split()))  #le elementos
  raiz = NodoArvore(nos[0])
  for i in range(1, len(nos)):
    no = NodoArvore(nos[i])
    inserirABB(raiz, no)

  print("Case %d:" % (n+1))

  s = pre_ordem(raiz)
  print("Pre.:", s.rstrip())

  s = em_ordem(raiz)
  print("In..:", s.rstrip())

  s = pos_ordem(raiz)
  print("Post:", s.rstrip())

  print()  #pula linha entre casos de teste
