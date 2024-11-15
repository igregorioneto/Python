def quick_sort(lista):
  if len(lista) <= 1:
    return lista
  pivo = lista[-1]
  menores = []
  maiores = []
  iguais = []

  for item in lista:
    if item < pivo:
      menores.append(item)
    elif item > pivo:
      maiores.append(item)
    else:
      iguais.append(item)

  return quick_sort(menores) + iguais + quick_sort(maiores)

if __name__ == "__main__":
  lista = [10, 7, 8, 9, 1, 5]
  print("Lista antes da ordenação:", lista)
  lista_ordenada = quick_sort(lista)
  print("Lista depois da ordenação:", lista_ordenada)