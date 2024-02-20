def verificador_de_caracteres(item, quant):
    if len(item) < quant:
        print(f"O valor digitado {item} tem que ter pelo menos 4 caracteres.")
        return False
    return True

def verificador_nota(nota, min):
    if nota < min:
        print(f"Nota informada {nota} é inválida")
        return False
    return True

def verificador_quantidade_lista(notas):
    if len(notas) == 0:
        print("Lista de informações esta vazia...")
        return False
    return True