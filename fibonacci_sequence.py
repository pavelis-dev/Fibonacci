num = int(input())


def fibonacci(n):
    f0, f1 = 0, 1
    for i in range(0, n):
        print(f0)
        f0, f1 = f1, f0 + f1        
    return f1


fibonacci(num)  # последовательность фибоначчи
