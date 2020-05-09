def F(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1

    else:
        fN = 2 * F(n - 1) + G(n - 2)
        return fN


def G(n):
    if n == 1 or n == 2:
        return n
    else:
        gN = G(n - 1) + 3 * F(n - 2)
        return gN


def K(n):
    if n > 0:
        return F(n), G(n)


print('Para K = 2 a saída é: ', K(2))
print('Para K = 3 a saída é: ', K(3))
print('Para K = 4 a saída é: ', K(4))

ListComprehension = [(F(n), G(n)) for n in range(1, 6)]
print(ListComprehension)

f_lambda = lambda x: 2 if x == 1 else (1 if x == 2 else 2 * F(x - 1) + G(x - 2))
g_lambda = lambda x: x if (x == 1 or x == 2) else G(x - 1) + 3 * F(x - 2)
k_lambda = lambda x: (F(x), G(x)) if x > 0 else None

print('Para K = 2 a saída é: ', k_lambda(2))
print('Para K = 3 a saída é: ', k_lambda(3))
print('Para K = 4 a saída é: ', k_lambda(4))
