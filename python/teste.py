from os import system
system('cls')
titulo = ' CONVERSOR DE MEDIDAS '
print(titulo.center(80, '*'))
medida = float(input('Informe a medida em centimetros: '))

print('\nEscolha para que unidade de medida deseja converter')
print('1 - polegada\n2 - Pé\n3 - jarda')

menu = input('opção: ')

valorpolegada = 2.54
valorpé = 30.48
valorjardas = 91.94

if menu == '1':
    polegada = medida / valorpolegada
    resultado = str(f'{medida:.4f} centimetros correspodem a {polegada:.4f} polegadas')
elif menu == '2':
    pes = medida / valorpé
    resultado = str(f'{medida:.4f} centimetros correspondem a {pes:.4f} pes')
elif menu == '3':
    jarda = media / valorjardas
    resultado = str(f'{medida:.4f} centimetros correpondem a {jarda:.4f} jarda')