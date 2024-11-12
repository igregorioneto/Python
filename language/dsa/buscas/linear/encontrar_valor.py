def busca_valor(lista, valor):
  arr = []
  for i in range(len(lista)):
    if lista[i] == valor:
      arr.append(i)
  return arr

if __name__ == "__main__":
  lista = [4, 2, 7, 4, 8, 4, 9]
  alvo = 4
  print(busca_valor(lista, alvo))
  lista = [1, 2, 3, 4, 5]
  alvo = 6
  print(busca_valor(lista, alvo))