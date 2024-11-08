class Fila:
  def __init__(self):
    self.itens = []

  def enqueue(self, item):
    self.itens.append(item)

  def dequeue(self):
    if not self.is_empty():
      return self.itens.pop(0)
    return None

  def is_empty(self):
    return len(self.itens) == 0
  
  def front(self):
    if not self.is_empty():
      return self.itens[0]
    return None
  
if __name__ == "__main__":
  fila = Fila()
  fila.enqueue(1)
  fila.enqueue(2)
  fila.enqueue(3)

  print(fila.dequeue())
  print(fila.front())
  print(fila.dequeue())
  print(fila.is_empty())
  print(fila.dequeue())
  print(fila.is_empty())