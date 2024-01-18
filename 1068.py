#TAD da Pilha
class Pilha:

  #Construtor
  def __init__(self):
    self.itens = []

#isEmpty

  def isEmpty(self):
    return self.itens == []
    #return len(self.itens) == 0

#push

  def push(self, item):
    self.itens.append(item)

#pop

  def pop(self):
    return self.itens.pop()

#peek

  def peek(self):
    return self.itens[-1]


#size

  def size(self):
    return len(self.itens)

while True:
    try:
        p = Pilha()
        cont = 0
        string = input()
        certo = True
        for caracter in string:
            if (caracter == '('):
                p.push(caracter)
            elif caracter == ')':
                if p.isEmpty():
                    certo = False
                else:
                    p.pop()
    
        if p.size() != 0:
            certo = False
        
        if certo:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break