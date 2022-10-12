def f(n):
    f0, f1 = 0, 1
    for i in range(2, n+1):
        f0, f1 = f1, f0 + f1
    return f1


print(f(10))  # максимальная цифра в последовательности фибоначчи
