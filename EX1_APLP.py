    a = int(input('Digite um número: ')) #Inserção da variável feita pelo usuário
    print(type(a)) ##Built-in type mostra qual tipo de item é a variável

    def prime_number(a): #Testar se é inteiro
        if type(a) == int: #Built-in type compara se a variável é inteira
            return ("O número {} é um Prime Number!".format(a))
        else:
            return ("Not a Prime Number!")

    def teste_zero(a): #Testar se o número é maior que zero
        if (a <= 0):
            return ('O número {} é maior que zero'.format(a))
        else:
            return ('Invalid Argument')

    def teste_primo(a): #Testar se o número é primo
        if a % 1:
            return ('Prime Number')
        else:
            return ('Not a Prime Number')

    def teste_limite(a): #Testar se o número encontra-se dentro do limite
        if a < 5.5*10**7: #Comparação do limite proposto pelo exercício
            return ('Ok') #Coloquei qualquer amostra só pra não ficar vazio
        else:
            return ('Argument Out of range')

    print(prime_number(a)) #Mostrar valor da função
    print(teste_zero(a)) #Mostrar valor da função
    print(teste_primo(a)) #Mostrar valor da função
    print(teste_limite(a)) #Mostrar valor da função