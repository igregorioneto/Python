def merge_sort(lista):
  if len(lista) > 1:
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    merge_sort(esquerda)
    merge_sort(direita)

    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        lista[k] = esquerda[i]
        i += 1
      else:
        lista[k] = direita[j]
        j += 1
      k += 1

    while i < len(esquerda):
      lista[k] = esquerda[i]
      i += 1
      k += 1

    while j < len(direita):
      lista[k] = direita[j]
      j += 1
      k += 1

if __name__ == "__main__":
  lista = [38, 27, 43, 3, 9, 82, 10]
  print("Lista antes da ordenação:", lista)
  merge_sort(lista)
  print("Lista depois da ordenação:", lista)