x = input('Digite um número: ')
print('O valor inserido foi: {}'.format(x))


def prime_number():  # Testar limite do número
    if x < 5.5 * 10 ** 7:
        print('Argument out of range')


def teste_primo(x):  # Testar se o número é primo
    if x % 2 == 1:
        print("Prime Number!")
    else:
        print("Not a Prime Number!")


def teste_PIZ(x):  # Testar se é positivo, inteiro e maior que zero

    if x is int:
        print('O numero {} é positivo e maior que zero')
    else:
        print('Invalid Argument')


print(prime_number(x))
print(teste_PIZ(x))
print(teste_primo(x))