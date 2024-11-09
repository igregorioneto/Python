class Item:
  def __init__(self, valor, prioridade):
    self.valor = valor
    self.prioridade = prioridade

class Deque:
  def __init__(self):
    self.itens = []

  def append(self, item, prioridade):
    item = Item(valor=item, prioridade=prioridade)
    self.itens.append(item)

  def appendLeft(self, item, prioridade):
    item = Item(valor=item, prioridade=prioridade)
    self.itens.insert(0, item)

  def pop(self):
    max = -1
    item = None
    if not self.is_empty():
      for x in self.itens:
        if x.prioridade > max:
          max = x.prioridade
          item = x
      index = self.itens.index(item)
      item = self.itens.pop(index)
      return item.valor
    return None

  def is_empty(self):
    return len(self.itens) == 0

  def front(self):
    if not self.is_empty():
      item = self.itens[0]
      return item.valor
    return None

  def back(self):
    if not self.is_empty():
      item = self.itens[-1]
      return item.valor
    return None

  def show(self):
    arr = []
    for item in self.itens:
      arr.append((item.valor, item.prioridade))
    return arr

if __name__ == "__main__":
  deque = Deque()

  deque.append(10, 2)
  deque.append(20, 1)
  deque.appendLeft(5, 3)

  print(deque.front())

  print(deque.pop())

  print(deque.show())