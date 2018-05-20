categoria = int(input('Digite a categoria'))
if categoria == 1:
    preco = 10.0
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    preco = 0

print('Categoria {} e preço: R$ {}'.format(categoria,preco
                                           ))