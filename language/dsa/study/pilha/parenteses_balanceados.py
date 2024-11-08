class Pilha:
  def __init__(self):
    self.itens = []

  def push(self, item):
    self.itens.append(item)

  def pop(self):
    if not self.is_empty():
      return self.itens.pop()
    return None

  def is_empty(self):
    return len(self.itens) == 0

if __name__ == "__main__":
  pilha = Pilha()
  expressao = input("expressão: ")

  for x in expressao:
    if x == "(":
      pilha.push(x)
    elif x == ")":
      if pilha.is_empty():
        print(False)
        exit()
      pilha.pop()

  if pilha.is_empty():
    print(True)
  else:
    print(False)