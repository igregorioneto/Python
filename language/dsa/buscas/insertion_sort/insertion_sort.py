def insertion_sort(lista):
  for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
      lista[j + 1] = lista[j]
      j -= 1
    lista[j + 1] = chave

if __name__ == "__main__":
  lista = [64, 34, 25, 12, 22, 11, 90]
  print("Lista antes da ordenação:", lista)
  insertion_sort(lista)
  print("Lista depois da ordenação:", lista)