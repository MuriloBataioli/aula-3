print('Olá usuario vamos calcular seu IMC?')
nome = str(input('Primeiro qual é o seu nome? '))
print('''Segundo, você prefere colocar em gramas o seu peso ou em kilogramas?
      [1] kilogramas
      [2] gramas
      ''')
resposta = int(input('  '))
if resposta == 1:
    peso = float(input('Seu peso em kilogramas: '))
elif resposta == 2:
    peso = float(input('Seu peso em gramas: '))/1000
else:
    print('unidade de peso invalido')
    exit()
print('''E a sua altura? qual você prefere?
      [1] metros
      [2] centimetros
      ''')
resposta2 = int(input('  '))
if resposta2 == 1:
    altura = float(input('Qual é a sua altura em metros? '))
elif resposta2 == 2:
    altura = float(input('Qual é a sua altura em centimetros '))/100
else:
    print('unidade de medida invalida')
    exit()
c = peso / altura**2    
qtd_casas_decimais = 1
imc = (c*10**qtd_casas_decimais)/10**qtd_casas_decimais
if imc < 15:
    print(f'{nome}, você está na magreza extrema!!')
elif imc >= 15 and imc < 18.55:
    print(f'{nome}, você está abaixo do peso!!')
elif imc >= 18.55 and imc < 24.95:
    print(f'{nome}, você está no seu peso normal')
elif imc >= 24.95 and imc < 29.95:
    print(f'{nome}, você está acima do peso!!')
elif imc >= 29.95 and imc < 39.95:
    print(f'{nome}, você está na obesidade grau 1!!')
else:
    print(f'{nome}, você está na obesidade grau 2 cuidado!!')
print(f'Seu IMC deu {imc:.2f}')