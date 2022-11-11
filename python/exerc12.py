from os import system
import random #biblioteca que gera valores aleatorios.

system('cls') #Primeiro importa a biblioteca "os", depois dar um "system('cls')" para limpar.

#print(random.randint(0, 100)) #"random" escolhe um numero aleatoriamente. "randint" escolhe um numero inteiro.
num = random. randint(0, 100)

#o numero escolhido é par ou impar?
#o numero escolhido é maior que 50 ou menor(mais perto do 100 ou do 0)
#o numero escolhido é primos

num = random.randint(0, 100)

res = num % 2

print(f'{num}')

if res == 0:
    print('Numero par')
else:
    print('Numero impar')

if (num > 50):
    print('Ele é mais próximo do 100')
else:
    print('Ele é mais próximo do 0')






