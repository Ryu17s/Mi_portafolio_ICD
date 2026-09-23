def factorial(numero):
    facto = 1
    for i in range(1, numero + 1):
        facto *= i
    return facto

def taylor_cos(x, n):
    suma = 0
    for i in range(n):
        exponente = 2 * i
        numerador = ((-1) ** i) * (x ** exponente)
        denominador = factorial(exponente)
        suma = suma + (numerador / denominador)
    return suma