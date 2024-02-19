import csv
# Calcular total de vendas
# Calcular total de vendas para cada produto
# Calcular o total de vendas por dia

diretorio = "diretorio_completo/venda_produtos.csv"

total_vendas = 0.0
total_vendas_dia = {}
total_vendas_produto = {}
with open(diretorio, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)
    for linha in leitor_csv:
        print(linha)
        data = linha[0]
        produto = linha[1]
        quantidade_produtos = float(linha[2])
        preco_unitario = float(linha[3])
        
        total_vendas += (quantidade_produtos * preco_unitario)
        total_vendas_produto[produto] = total_vendas_produto.get(produto, 0) + (quantidade_produtos * preco_unitario)
        total_vendas_dia[data] = total_vendas_dia.get(data, 0) + (quantidade_produtos * preco_unitario)

print(f"Total de vendas é R${total_vendas}")
print(f"Total de vendas por produto:")
for produto, vendas_produto in total_vendas_produto.items():
    print(f"{produto}: {vendas_produto}")

print(f"Total de vendas por data:")
for dia, vendas_dia in total_vendas_dia.items():
    print(f"{dia}: {vendas_dia}")
