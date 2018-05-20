velocidade=float(input('Digita a velocidade medida em km/h: '))
if(velocidade>=80):
    acima = velocidade-80.0
    multa=5*acima
    print('Você foi multado!')
    print('Multa: R$ {}'.format(multa))
else:
    print('Parabéns você obedece as regras!')
    