def merge_sort_des(lista):
  if len(lista) > 1:
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    merge_sort_des(esquerda)
    merge_sort_des(direita)

    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
      if esquerda[i] > direita[j]:
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
  lista = [3, 9, 10, 27, 38, 43, 82]
  print("Lista antes da ordenação:", lista)
  merge_sort_des(lista)
  print("Lista depois da ordenação:", lista)