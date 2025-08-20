# Coleções

# Tuplas ()
# tupla = ('Marcus', 'Vinicius', 'Faria', 'Souza')

# #Mostrando elementos
# print(tupla)
#
# #Alterando elementos
# #tupla[0] = 'marquinho'
# #tuplas é uma coleção imutavel, não pode trocar, tirar e nem acrescentar elementos
#
# #Slicing de elementos (Fatiar)
# print(tupla[1:3]) #Vinicius e Faria
# #Inclusive:Exclusive ou seja pega o primeiro e tira o ultimo
#
# print(tupla[2:]) #Faria e Souza
# #Posição 2 em diante
#
# #indice negativo pega de traz para frente
# print(tupla[-2]) #(-4, -3, -2, -1) pega o Faria
#
# print(len(tupla)) #tamanho da tupla
# print(max(tupla)) #maior elemento em ordem alfabetica
# print(min(tupla)) #menor elemento

# #Listas []
# #são complementamente mutaveis
# #listas são heterogeneas, aceitam qualquer tipo, int, string
# #mas tem problemas, funçoes min e max não funcionam com varios tipos
# lista = ['Marcus', 'Vinicius', 'Faria', 'Souza']
# print(lista)
#
# #inserindo elementos
# lista.append('Palmeiras')#inserindo elementos no final da lista
# lista.insert(1, "Legal") #inserindo na posição desejada
# print(lista)
#
# #alterando elemetos
# lista[0] = "Maria"
# print(lista)
#
# #Excluindo elementos
# del lista[0] #remoção pelo indice
# lista.remove("Legal") #remoção por valor
# print(lista)
#
# #ordenando
# lista.sort() #ou lista.sorted()
# print(lista)

# #Conjuntos {}
# #Não guarda a ordem dos elementos
# #Não permite elementos repetidos
# conjunto = {'Marcus', 'Vinicius', 'Faria', 'Souza'}
# print(conjunto)
#
# #Adicionando elementos
# conjunto.add("marquinho")
# conjunto.add("marquinho")
# print(conjunto)
#
# #Removendo elementos por valor
# conjunto.remove("marquinho")
# print(conjunto)
#
# #para trocar elementos em conjutos deve apagar um e add o outro, duas funções
#
# #Como descobrir o tipo de algo em pyhton
# print(type(conjunto))

# Dicionarios {} key:value
# as keys não necessáriamente precisam ser string, podem ser numeros também

pessoa = {
    'nome': "Goku",
    'idade': 43,
    'sexo': 'masculino'
}

# adicionando elementos
pessoa['raca'] = 'sayajin'
pessoa['familia'] = ['Gohan', 'Goten', 'Chichi', 'Pan'] #lista dentro do dicionario

#Update
pessoa['idade'] = 45

#Deletando
del pessoa['sexo']

print(pessoa)
print(pessoa['familia'][2]) #Acessando a Chichi