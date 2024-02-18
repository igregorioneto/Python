#Solicite ao usuário que insira um número inteiro positivo maior que 1.
#Verifique se o número é divisível por algum número além de 1 e ele mesmo.
#Se o número for divisível por outro número além de 1 e ele mesmo, então ele não é primo.
#Caso contrário, se o número não for divisível por nenhum outro número além de 1 e ele mesmo, então ele é primo.
#Exiba uma mensagem indicando se o número é primo ou não.

def primo2(numero):
    count = 0
    if numero > 1:
        for n in range(1,numero + 1):
            if numero % n == 0:
                count += 1
                if count > 2:
                    return "Não é primo"
                
        if count == 2:
            return "Número primo"
    else:
        return "Não é primo"
    
# função formatada
def primo(numero):
    if numero <= 1:
        return "Não é primo"
    
    for n in range(2, numero // 2 + 1):
        if numero % n == 0:
            return "Não é primo"
        
    return "Número primo"

numero = int(input("Digite um número: "))
print(primo(numero))
