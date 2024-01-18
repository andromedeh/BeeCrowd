from collections import deque

class No:
    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq

class Tree:
    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v):
        novo = No(v, None, None)
        if self.root is None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item:
                    atual = atual.esq
                    if atual is None:
                        anterior.esq = novo
                        return
                else:
                    atual = atual.dir
                    if atual is None:
                        anterior.dir = novo
                        return

def mostrarNosPorNivel(root):
    resultado = ""
    if root is None:
        return ""
    queue = deque()
    queue.append((root, 1))  # Tupla com o nó e o nível

    current_level = 1

    while queue:
        node, level = queue.popleft()

        if level > current_level:
            current_level = level

        resultado += str(node.item) + " "

        if node.esq:
            queue.append((node.esq, level + 1))
        if node.dir:
            queue.append((node.dir, level + 1))
    return resultado

C = int(input())
for n in range(C):
    arvore = Tree()
    N = int(input())
    nos = list(map(int, input().split()))
    print("Case %d:" % (n+1))
    for no in nos:
        arvore.inserir(no)
    saida = mostrarNosPorNivel(arvore.root)
    saida = saida.rstrip()  
    print(saida)
    print() 
