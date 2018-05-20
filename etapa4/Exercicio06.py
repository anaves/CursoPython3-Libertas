# importa biblioteca para gerar aleatorio
import random as rnd
V=[] # cria V vazia
for i in range(50): # preencher com V com 50 numeros
    V.append(rnd.randint(1,500)) # sorteia int entre 1 e 500
print(V) # imprime V
P=[] # cria P para armazenar pares
I=[] # cria I para armazenar ímpares
for i in range(len(V)):
    if V[i]%2 == 0: # divide elemento por 2 verifica resto
        P.append(V[i]) # adiciona na lista pares
    else:
        I.append(V[i]) # adiciona na lista ímpares

print('Pares: {}'.format(P))
print('Ímpares: {}'.format(I))

