#faça um progrma que receba 3 numeros e informe qual é o maior e qual é o menor

import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
num3 = random.randint(0, 100)

escolhidos = (num1, num2, num3)
print(escolhidos)

if num1 > num2 and num1 > num3:
    print(f'\nO {num1} é maior. ')
elif num2 > num1 and num2 > num3:
    print(f'\nO {num2} é maior. ')
else:
    print(f'\nO {num3} é maior. ')
if num1 < num2 and num1 < num3:
    print(f'\nO {num1} é menor. ')
elif num2 < num1 and num2 < num3:
    print(f'\nO {num2} é menor. ')
else:
    print(f'\nO {num3} é menor. ')
