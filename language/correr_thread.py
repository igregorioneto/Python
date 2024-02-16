import threading
import time
import random

# Cria a classe Corredor herdando o threading.Thread
class Corredor(threading.Thread):
    # inicializando as variáveis e chamando o init do Thread
    def __init__(self, nome, distancia_total):
        super().__init__()
        self.nome = nome
        self.distancia_total = distancia_total
        self.distancia_percorrida = 0
        self.valocidade_maxima = 5

    # Verifica a distância percorrida
    # Gera uma distância parcial com base na velocidade maxima
    # Incrementa a distância parcial a velocidade percorrida
    # Gera a informação e aguarda um tempo de 0,5 segundos para poder seguir.
    def correr(self):
        while self.distancia_percorrida < self.distancia_total:
            distancia_parcial = random.uniform(0, self.valocidade_maxima)
            self.distancia_percorrida += distancia_parcial
            print(f"{self.nome} correu {distancia_parcial:.2f} metros.\nDistância total percorrida: {self.distancia_percorrida:.2f} metros.\n")
            time.sleep(0.5)
    
    # Método run que é executado ao chamar o start do Thread
    def run(self):
        print(f"{self.nome} começou a corrida!")
        self.correr()
        print(f"{self.nome} terminou a corrida!")

# Criando objetos e executando os threads
if __name__ == "__main__":
    corredor1 = Corredor("João", 100)
    corredor2 = Corredor("Larissa", 100)
    corredor3 = Corredor("Maria", 100)

    corredor1.start()
    corredor2.start()
    corredor3.start()

    corredor1.join()
    corredor2.join()
    corredor3.join()

    print("Todos os corredores terminaram a corrida!")




