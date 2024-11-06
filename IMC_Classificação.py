import math
print('Olá usuario vamos calcular seu IMC')
nome = str(input('Qual é o seu nome? '))
peso = float(input('Seu peso em kg: '))
altura = float(input('Sua altura em metros: '))
c = peso / altura**2
qtd_casas_decimais = 1
imc = (c*10**qtd_casas_decimais)/10**qtd_casas_decimais
if imc < 15:
    print(f'{nome}, você está na magreza extrema!!')
elif imc >= 15 and imc < 18.55:
    print(f'{nome}, você está abaixo do peso!!')
elif imc >= 18.55 and imc < 24.55:
    print(f'{nome}, você está no seu peso normal')
elif imc >= 24.55 and imc < 29.55:
    print(f'{nome}, você está acima do peso!!')
elif imc >= 29.55 and imc < 39.55:
    print(f'{nome}, você está na obesidade grau 1!!')
else:
    print(f'{nome}, você está na obesidade grau 2 cuidado!!')
print(f'Seu IMC deu {imc:.2f}')