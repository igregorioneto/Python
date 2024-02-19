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

try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+,-,*,/): ")

    if operacao not in ['+', '-', '*', '/']:
        print(f"O operador informado {operacao} é inválido.")

    print("Resultado da operação: " ,calculo(operacao, n1, n2))
except ZeroDivisionError:
    print("Error: Divisão por zero!")
except KeyboardInterrupt:
    print("Error: Encerrando a entrada de dados.")
except ValueError:
    print("Error: Valor inválido! Você deve digitar um número.")
finally:
    print("Finalizando...")



