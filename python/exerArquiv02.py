from os import system
import os.path, datetime
system('cls')

arquivo = 'categorias.csv' #caminho do arquivo
categorias = open(arquivo, 'r', encoding='utf-8')
#abre somente leitura o caminho do arquivo e armazena em uma variavel
dicCategoria = {} #instaciar uma variavel do tipo dicionario

if os.path.isfile(arquivo): #verifica se o caminho do arquivo é valido
    for line in categorias: #para cada linha do arquivo
        colunas = line.strip().split(';') 
        #retira os espacos e separa em lista as colunas
        dados =[colunas[1], colunas[2]]
        #armazena em dados uma lista com os valores da coluna 1 e 2
        dicCategoria[colunas[0]] = dados
        #cria uma chave com o valor da coluna 0 e associa o valor com os dados

    
    categorias.close() #fecha o arquivo
    print(dicCategoria) #exibe o dicionario
