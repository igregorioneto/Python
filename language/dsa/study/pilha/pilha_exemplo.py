class Pilha:
  def __init__(self):
    self.itens = []

  def push(self, item):
    self.itens.append(item)

  def pop(self):
    if not self.is_empty():
      return self.itens.pop()
    return -1

  def peek(self):
    if not self.is_empty():
      return self.itens[-1]
    return -1

  def is_empty(self):
    return len(self.itens) == 0
  
if __name__ == "__main__":
  pilha = Pilha()
  pilha.push(1)
  pilha.push(2)
  pilha.push(3)

  print("Topo da pilha: ", pilha.peek())
  print("Elemento removido: ", pilha.pop())
  print("Novo topo da pilha: ", pilha.peek())