from random import randint
x1 = randint(0, 9)
x2 = randint(0, 9)
x3 = randint(0, 9)
x4 = randint(0, 9)
print('Eu sou a casa de apostas')
numero1 = int(input('escolha um numero de 0 a 9 '))
numero2 = int(input('escolha mais um numero de 0 a 9 '))
premio = 0
if numero1 == x1 or numero1 == x2 or numero1 == x3 or numero1 == x4:
    premio += 1000
    print('você ganhou no primeiro numero')
if numero2 == x1 or numero2 == x2 or numero2 == x3 or numero2 == x4:
    premio += 1000
    print('você ganhou no segundo numero')
print(premio)
print(x1, x2, x3, x4)