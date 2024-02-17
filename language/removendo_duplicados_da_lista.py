
def removendo_numeros_duplicados(lista):
    lista = list(lista)
    nova_lista = list()
    for e in lista:
       if e != ' ' and (e not in nova_lista):
           nova_lista.append(e)
                
    return nova_lista

def removendo_duplicados(lista):
    lista = lista.split()
    nova_lista = []
    for e in lista:
        if e not in nova_lista:
            nova_lista.append(e)
    return nova_lista

lista = input("Digite uma lista de números separados por espaço (Ex. 1 2 3): ")

print(removendo_duplicados(lista))