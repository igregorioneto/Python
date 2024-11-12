def encontrar_valor(lista, valor):
  inicio = 0
  fim = len(lista) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == valor:
      return meio
    elif lista[meio] < valor:
      inicio = meio + 1
    elif lista[meio] > valor:
      fim = meio - 1
  return inicio

if __name__ == "__main__":
  lista = [1, 3, 5, 6]
  alvo = 5
  print(encontrar_valor(lista, alvo))
  lista = [1, 3, 5, 6]
  alvo = 2
  print(encontrar_valor(lista, alvo))
  lista = [1, 3, 5, 6]
  alvo = 7
  print(encontrar_valor(lista, alvo))