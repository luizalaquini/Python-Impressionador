funcionarios = ['Maria', 'João', 'José', 'Pedro', 'Ana', 'Paulo', 'Carlos', 'Ricardo', 'Marta', 'Júlia']

for idx, funcionario in enumerate(funcionarios):
    print('O funcionário de índice {} é {}'.format(idx, funcionario))

# Exemplo prático:

produtos = ['coca', 'fanta', 'sprite', 'guaraná', 'pepsi']
estoque = [800, 300, 150, 650, 90]

nivel_critico = 200

for idx, qtd in enumerate(estoque):
    if qtd < nivel_critico:
        print('O produto {} está abaixo do nível com apenas {} unidades'.format(produtos[idx], qtd))