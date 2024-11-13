def bubble_sort(lista):
  n = len(lista)
  for i in range(n - 1):
    trocou = False
    for j in range(n - 1 - i):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        trocou = True
    if not trocou:
      break

if __name__ == "__main__":
  lista = [64, 34, 25, 12, 22, 11, 90]
  print("Lista antes da ordenação:", lista)
  bubble_sort(lista)
  print("Lista depois da ordenação:", lista)