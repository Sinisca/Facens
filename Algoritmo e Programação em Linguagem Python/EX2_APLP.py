lista1 = [] #Lista 1 vazia
lista2 = [] #Lista 2 vazia
x =  []     #Declaração de x
soma = []   #Declaração de soma
lista = []  #Declaração de lista

def lista_1(lista1):

    x = int(input('Insira a quantidade de elementos da lista 1: '))             #Inserção dos elementos das lista 1 pelo usuário
    for i in range(0, x):                                                       #Especificando a quantidade de elementos da lista começando pelo índice 0
        elementos = int(input('Elemento inserido no índice {}: '.format(i)))    #Inserção dos elementos e mostrando qual índice
        lista1.append(elementos)                                                #Adiciona um elemento na ultima posição da lista
    return(lista1)

def lista_2(lista2):

    x = int(input('Insira a quantidade de elementos da lista 2: '))             #Inserção dos elementos das lista 1 pelo usuário
    for i in range(0, x):                                                       #Especificando a quantidade de elementos da lista começando pelo índice 0
        elementos = int(input('Elemento inserido no índice {}: '.format(i)))    #Inserção dos elementos e mostrando qual índice
        lista2.append(elementos)                                                #Adiciona um elemento na ultima posição da lista
    return(lista2)


def sum_of_products(x):
    x = any(type(x) != int for x in lista1 and lista2) #Compara se os elemento inseridos nas lista são inteiros númericos ou strings
    if type(x) != str:                                 #Verifica e compara se os elementos são inteiros
        return ('Somente números')
    else:
        return ('Wrong number')

def soma_listas(soma):
    soma = [lista1 + lista2 for lista1, lista2 in zip(lista1, lista2)] #Soma de elementos das listas através de seus índices
    return (soma)

def vazio(lista):
    if lista1 and lista2 != None: #Verifica se as listas estão vazias e retorna -1
        return ('-1')

print(lista_1(lista1))
print(lista_2(lista2))
print(sum_of_products(x))
print(soma_listas(soma))
print(vazio(lista))