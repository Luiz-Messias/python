from Recibo import Recibo
from os import system
system('cls')

novoRecibo = Recibo('Luiz')

print(novoRecibo.nome)
novoRecibo.valor = 1258, 99
novoRecibo.descricao('Desenvolvimento de sistemas em python')

#print(novoRecibo.nome, novoRecibo.valor, novoRecibo._descricao)
print(novoRecibo)