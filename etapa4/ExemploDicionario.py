tabela={'Alface':[1000,0.45],
        'Batata':[100,1.20],
        'Tomate':[40,2.30],
        'Feijão':[80,1.50]}
print('Produtos cadastrados')
print(tabela.keys())
produto=input('Digite o produto: ')
print('Estoque {}'.format(tabela[produto][0]))
print('R$ {}'.format(tabela[produto][1]))