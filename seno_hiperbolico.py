import math

def factorial(n):
    facto = 1
    for i in range(2,n+1):
        facto *= i
    return facto

def senoHiperbolico(n,contTermino):
    serie = 0
    radian = n * (math.pi / 180)
    for i in range(1,contTermino+1,2):
        numerador = radian ** i
        denominador = factorial(i)
        serie += numerador / denominador
    return serie