def media(lista):
    lista = lista.split()
    if not lista:
        return 0
    sum = 0
    for e in lista:
        sum += int(e)
    return sum / len(lista)

lista = input("Digite a sequência numérica (Ex 1 2 3): ")
print(f"A média da sequência {lista} é: {media(lista)}")