def fib(x):
    if x == 0 or x == 1:
        f = x
    else:
        f = fib(x - 1) + fib(x - 2)
    return f

Fibonacci = lambda x: x if (x == 0 or x == 1) else fib(x - 1) + fib(x - 2)

print('Lambda: ', [Fibonacci(x) for x in range(0, 20)])
print('Saída: ', list(map(fib, list(range(0, 20)))))
