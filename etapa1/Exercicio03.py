# Escreva um programa que leia a quantidade de dias, horas, minutos e
# segundos do usuário. Calcule o total em segundos
dias = int(input('Digite o total de dias: '))
horas = int(input('Digite o total de horas: '))
minutos = int(input('Digite o todal de minutos: '))
segundos = int(input('Digite o total de segundos: '))
totalSegundos=dias*24*3600+horas*3600+minutos*60+segundos
print('Total em segundos: {}s'.format(totalSegundos))