import threading
import time

# função que será executada na thread
def minha_funcao():
    for i in range(5):
        print("Executando na thread")
        time.sleep(1)

# Cria a instância da thread passando a função como argumento
minha_thread = threading.Thread(target=minha_funcao)

# Inicia a execução da thread
minha_thread.start()

# O programa principal continua executando enquanto a thread
# Continua em paralelo
for i in range(3):
    print("Executando o programa principal")
    time.sleep(1)

# Esperar a thread terminar a execução
minha_thread.join()

print("A thread terminou. O Programa principal também terminou.")