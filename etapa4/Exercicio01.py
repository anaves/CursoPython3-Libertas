N=[]
for i in range(5):
    N.append(float(input('Digite a {}ª nota: '.format(i+1))))

print('Soma: {} e N = {}'.format(sum(N),N))
media = sum(N)/5
print('Média = {}'.format(media))