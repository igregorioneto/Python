def sum(n):
  if n <= 0:
    return 0
  return n + sum(n-1)

if __name__ == "__main__":
  soma = sum(10)
  print("Soma dos elementos do 1 ao 10: ", soma)