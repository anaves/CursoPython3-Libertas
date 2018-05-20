L=[5,9,13]
i = 0
for el in L:
    print('indíce: {} - conteúdo: {}'.format(i,el))
    i = i+1

# Enumerate
print('com uso do enumerate')
for i,el in enumerate(L):
    print('indíce: {} - conteúdo: {}'.format(i, el))