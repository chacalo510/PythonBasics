def fibonacci(n):
    if n <= 1:
        return 1
    fn_1 = 1
    fn_2 = 1
    resultado = 0
    for i in range(2, n+1):
        resultado = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = resultado

    return resultado

print(fibonacci(5))
