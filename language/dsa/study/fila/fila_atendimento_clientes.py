class Fila:
  def __init__(self):
    self.clientes = []

  def enqueue(self, client):
    self.clientes.append(client)

  def dequeue(self):
    if not self.is_empty():
      return self.clientes.pop(0)
    return None

  def is_empty(self):
    return len(self.clientes) == 0
  
  def front(self):
    if not self.is_empty():
      return self.clientes[0]
    return None
  
  def fila(self):
    return self.clientes;
  
if __name__ == "__main__":
  filaClientes = Fila()
  opcao = ""
  while (opcao != "4"):
    print("Opções:")
    print("1. Adicionar pessoa na fila")
    print("2. Atender pessoa")
    print("3. Mostrar fila atual")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")   

    if opcao == "1":
      nomePessoa = input("Digite o nome da pessoa: ")
      filaClientes.enqueue(nomePessoa)
    elif opcao == "2":
      print("\nAtendendo: ", filaClientes.dequeue())
    elif opcao == "3":
      print("\nFila atual: ", filaClientes.fila())