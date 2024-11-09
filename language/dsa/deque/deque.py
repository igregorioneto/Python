class Deque:
  def __init__(self):
    self.itens = []

  def append(self, item):
    self.itens.append(item)

  def appendLeft(self, item):
    self.itens.insert(0, item)

  def pop(self):
    if not self.is_empty():
      return self.itens.pop()
    return None

  def popLeft(self):
    if not self.is_empty():
      return self.itens.pop(0)
    return None

  def is_empty(self):
    return len(self.itens) == 0

  def front(self):
    if not self.is_empty():
      return self.itens[0]
    return None

  def back(self):
    if not self.is_empty():
      return self.itens[-1]
    return None

  def size(self):
    return len(self.itens)

if __name__ == "__main__":
  deque = Deque()

  deque.append(10)
  deque.append(20)
  deque.appendLeft(5)

  print("Deque após inserções:", deque.itens)

  print("Pop:", deque.pop())
  print("Popleft:", deque.popLeft())

  print("Frente do deque:", deque.front())
  print("Fundo do deque:", deque.back())

  print("Tamanho do deque:", deque.size())

  print("Deque está vazio?", deque.is_empty())

  print("Pop:", deque.pop())

  print("Deque está vazio?", deque.is_empty())