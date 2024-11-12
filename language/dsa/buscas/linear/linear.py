def busca_linear(lista, valor):
  for i in range(len(lista)):
    if lista[i] == valor:
      return i
  return -1

if __name__ == "__main__":
  numeros = [10, 20, 30, 40, 50]
  print(busca_linear(numeros, 30))
  print(busca_linear(numeros, 60))