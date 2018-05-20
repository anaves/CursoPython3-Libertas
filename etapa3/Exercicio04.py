num = int(input('Digite o número para obter a tabuada'))
print('*'*30)
print('Tabuada de {}'.format(num))
print('*'*30)

for i in range(11):
    print('{} x {} = {}'.format(num,i,num*i))