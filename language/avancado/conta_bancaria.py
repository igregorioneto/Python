class ContaBancaria:
    def __init__(self,numero_conta, saldo):
        self._numero_conta = numero_conta
        self._saldo = int(saldo)

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self._numero_conta = numero_conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    def deposito(self, valor):
        if (valor > 0):
            self._saldo += int(valor)
    
    def saque(self, valor):
        if valor > 0 and self.saldo > 0 and valor <= self.saldo:
            self._saldo -= int(valor)
    
    def verificar_saldo(self):
        return f"Seu saldo atual é R$ {self.saldo}"
    
    def bem_vindo(self):
        return f"Bem vindo {self.numero_conta}, saldo atual é {self.saldo}"
    

if __name__=="__main__":   
    print("Entre com os dados da conta")
    numero = input("Digite o número da conta: ")
    saldo = input("Digite o saldo da conta: ") 
    
    if (numero != "" and saldo != ""):
        conta = ContaBancaria(numero, saldo)
        print(conta.bem_vindo())
        while True:            
            print("1 - Verificar saldo")
            print("2 - Depositar valor")
            print("3 - Saque de valor")
            print("4 - Sair")
            opcao = input("Digite uma opção: ")
            if opcao == '1':
                print(conta.verificar_saldo())
            elif opcao == '2':
                opcao = int(input("Digite valor para depósito: R$"))
                conta.deposito(opcao)
                print(conta.verificar_saldo())
            elif opcao == '3':
                opcao = int(input("Digite valor para saque: -R$"))
                if (opcao > conta.saldo):
                    print(f"O valor R${opcao} acima do saldo atual R${conta.saldo}.")
                    continue
                conta.saque(opcao)
                print(conta.verificar_saldo())
            elif opcao == '4':
                break  
            else:
                print(f"Opção informada {opcao} não consta no Menu.")
                continue    
        print("Até mais!")
    else:
        print("Informações digitadas incorretas...")
    
        