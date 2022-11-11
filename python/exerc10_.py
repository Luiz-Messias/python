num1 = input('Informe um valor 1:')
divisor = input('informe um valor divi: ')

if num1.isalpha(): #isalpha quando for letra
    print('Nao é um numero')

if num1.isdecimal(): #quando for numero
    print('é um numero')

if int(divisor) > 0:
    print('Posso dividr')
    divisao = int(num1) / int(divisor)
    print(f'resultado da divisão é {divisao}')
else:
    print('Valor 0. Não pode ser dividido')