    a = int(input('Digite um número: '))
    print(type(a))

    def prime_number(a): #Testar se é inteiro
        if type(a) == int:
            return ("O número {} é um Prime Number!".format(a))
        else:
            return ("Not a Prime Number!")

    def teste_zero(a): #Testar se o número é maior que zero
        if (a <= 0):
            return ('O número {} é maior que zero'.format(a))
        else:
            return ('Invalid Argument')

    def teste_primo(a):
        if a % 1:
            return ('Prime Number')
        else:
            return ('Not a Prime Number')

    def teste_limite(a):
        if a < 5.5*10**7:
            return ('Ok')
        else:
            return ('Argument Out of range')

    print(prime_number(a))
    print(teste_zero(a))
    print(teste_primo(a))
    print(teste_limite(a))