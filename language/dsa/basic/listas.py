'''
Lista:
-- coleção ordenada e MUTÁVEL
-- pode ser de vários tipos de dados
-- os itens são acessados pelo index
'''

# Exemplo de lista de senhas comprometidas
senhas_comprometidas = ["senha123", "qwerty", "123456"]

# Verificar se uma senha esta na lista de senhas comprometidas
senha = input("Digite uma senha: ")
if senha in senhas_comprometidas:
    print("Senha comprometida! Por favor, escolher outra senha.")
else:
    print("Senha segura!")

# Caso eu queira digitar uma nova senha.
senhas_comprometidas.append("123789")
print(senhas_comprometidas)

# Buscando a index do elemento que encontra-se na lista
idx = senhas_comprometidas.index("123456")
print(idx)

# Caso queira limpar a lista
senhas_comprometidas.clear()
print(senhas_comprometidas)