def selection_sort(lista):
  n = len(lista)
  for i in range(n - 1):
    menor_indice = i
    for j in range(i + 1, n):
      if lista[j] < lista[menor_indice]:
        menor_indice = j
    lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

if __name__ == "__main__":
  lista = [64, 34, 25, 12, 22, 11, 90]
  print("Lista antes da ordenação:", lista)
  selection_sort(lista)
  print("Lista depois da ordenação:", lista)