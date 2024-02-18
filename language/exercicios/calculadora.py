#Solicite ao usuário que insira o primeiro número.
#Solicite ao usuário que insira o segundo número.
#Solicite ao usuário que escolha a operação desejada (adição, subtração, multiplicação ou divisão).
#Com base na operação escolhida, execute a operação apropriada nos dois números.
#Exiba o resultado da operação.

def calculo(operacao, n1, n2):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao == '/':
        return n1 / n2
    else:
        return 0

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+,-,*,/): ")

print("Resultado da operação: " ,calculo(operacao, n1, n2))



