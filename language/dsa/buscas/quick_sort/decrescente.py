import random

def quick_sort_des(lista):
  if len(lista) <= 1:
    return lista

  pivo = lista[random.randint(0, len(lista) - 1)]
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

  return quick_sort_des(maiores) + iguais + quick_sort_des(menores)

if __name__ == "__main__":
  lista = [34, 7, 23, 32, 5, 62]
  print("Lista antes da ordenação:", lista)
  lista_ordenada = quick_sort_des(lista)
  print("Lista depois da ordenação:", lista_ordenada)