from os import system
import random
system ('cls')

titulo = ' PEDRA | PAPEL | TESOURA '
print(titulo.center(60, "#"))

opcao = 's'
contadorjogadas = 0
contadorjogador = 0
contadorcomp = 0
while opcao.upper()=="S":
    system('cls')
    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opção para se jogar:
    [0] Pedra
    [1] Papel
    [2] tesoura
    Digite sua escolha:'''))
        
    if jogador > 3:
        resultado = f'Voce nao escolheu uma opcao valida'
    else:
        contadorjogadas += 1
        pecas = ('Pedra', 'Papel', 'Tesoura')
        print(f'Voce escolheu {pecas[jogador]}')
        print(f'Computador escolheu {pecas[computador]}')
        tabela = ((0,1,-1), (-1,0,1), (1,-1,0))
        jogada = tabela[computador][jogador]
        if jogada == 0:
            resultado = f'deu empate'
        elif jogada == 1:
            resultado = f'voce ganhou!'
            contadorjogador += 1
        elif jogada == -1:
            resultado = f'O computador ganhou!!'
            contadorcomp += 1
    print(resultado)
    opcao = input('''\njogar novamente? (S) para sim\nsua opcao: ''')    
system("cls")
print('resumo do jogo'.center(60, '*'))
print(f'quantidade de jogadas: {contadorjogadas}')
print(f'voce ganhou: {contadorjogador} jogadas')
print(f'computador ganhou: {contadorcomp} jogadas')