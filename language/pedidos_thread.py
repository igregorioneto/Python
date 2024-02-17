import threading
import time

class Pedido(threading.Thread):
    def __init__(self, nome, preco, pedido):
        super().__init__()
        self.nome = nome
        self.preco = preco
        self.pedido = pedido 

    def processar_pagamento(self):
        print(f'Processar pagamento do pedido {self.pedido}')
        time.sleep(1)
    
    def verificar_estoque(self):
        print(f'Verificando se tem o pedido: {self.pedido} no estoque.')
        time.sleep(1)
    
    def empacotar(self):
        print(f'Empacotando o pedido {self.pedido}')
        time.sleep(1)
    
    def enviar(self):
        print(f'Enviando o pedido {self.pedido}')
        time.sleep(1)

    def run(self):
        print(f'Iniciando o Pedido {self.pedido}')
        self.processar_pagamento()
        self.verificar_estoque()
        self.empacotar()
        self.enviar()
        print(f'Finalizando o Pedido ${self.pedido}')


if __name__=="__main__":

    pedido1 = Pedido('Macbook', 7000, '#1')
    pedido2 = Pedido('Geladeira', 4000, '#2')
    pedido3 = Pedido('Microondas', 700, '#3')
    pedido4 = Pedido('Fogão', 1000, '#4')
    pedido5 = Pedido('Monitor', 1200, '#5')
    pedido6 = Pedido('Forno Elétrico', 500, '#6')
    pedido7 = Pedido('Smartphone', 2000, '#7')

    pedido1.start()
    pedido2.start()
    pedido3.start()
    pedido4.start()
    pedido5.start()
    pedido6.start()
    pedido7.start()

    pedido1.join()
    pedido2.join()
    pedido3.join()
    pedido4.join()
    pedido5.join()
    pedido6.join()
    pedido7.join()

    print("Terminando processamento dos pedidos...")