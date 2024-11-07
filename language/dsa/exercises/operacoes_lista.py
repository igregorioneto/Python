if __name__ == "__main__":
  lista = input("Digite uma lista de números separado por vírgula: ")
  lista = list(map(int, lista.split(',')))
  print("Maior número: ", max(lista))
  print("Menor número: ", min(lista))
  print("Soma dos elementos: ", sum(lista))
  listaNumerosPares = [x for x in lista if x % 2 ==0]
  print("Lista com números pares: ", listaNumerosPares)
  print("Lista ordenada: ", sorted(lista))
  print("Lista original sem o primeiro e último elemento: ", lista[1:-1])
