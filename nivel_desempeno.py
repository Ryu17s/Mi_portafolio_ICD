import math 

def factorial(n):
    facto = 1
    for i in range(1,n+1):
        facto *= i
    return facto

def desempeño(k):
    desempeño = 0
    for i in range(0,50):
        exponente = 2 * i
        numerador = k ** exponente
        denominador = factorial(exponente)
        desempeño += numerador / denominador
    return math.trunc(desempeño)
# main

k = int(input())
resultado = desempeño(k)
print("CANTIDAD DE DRAGONES DERROTADOS =",k)
print("DESEMPEÑO JUGADOR =",resultado)
if resultado >= 0 and resultado < 500:
    print("NIVEL NOVATO")
elif resultado > 500 and resultado <50000:
    print("NIVEL EXPERTO")
else:
    print("NIVEL MAESTRO")