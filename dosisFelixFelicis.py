import math

def alpha(n):
    suma = 1
    for i in range(1, n):
        suma += i
    return suma

def factorial(n):
    facto = 1
    for i in range(1, n + 1):
        facto *= i
    return facto
    
def beta(n):
    sumatoria = 0.0
    for i in range(1, 51):
        numerador = n ** i
        denominador = factorial(i)
        sumatoria += numerador / denominador
    return sumatoria

def gama(n):
    suma = 0
    for i in range(1,n+1):
        if n % i == 0:
            suma += i
    return suma

def delta(n):
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum += i
    return sum

def dosisFelix(edad,meses,peso,gramos,metros,estatura):
    if edad >= 1 and edad <= 20:
        dosis = (alpha(meses) * (peso) / beta(metros))
    elif edad >= 21 and edad <= 40:
        dosis = (gama(peso) * delta(edad) / metros)
    elif edad >= 41 and edad <= 60:
        dosis = (gama(meses) * math.trunc(math.sqrt(gramos)) / estatura)
    elif edad > 60:
        dosis = (delta(peso) * math.trunc(math.sqrt(edad)) / metros)
    return math.trunc(dosis)
    
while True:
    habitante = int(input())
    if 0 < habitante <= 10000: 
        break

print(f"Harry, se procesarán {habitante} habitantes del mundo mágico.\n")
print("----- INICIO DEL PROCESO -----\n")

for k in range(1, habitante + 1):
    print(f"Habitante #{k}")
    edad = int(input())
    peso = int(input())
    estatura = int(input())
    
    meses = edad * 12
    gramos = peso * 1000
    metros = estatura / 100
    dosis = dosisFelix(edad,meses,peso,gramos,metros,estatura)
    horaSuerte = (dosis * 12) / 100
    diasSuerte = math.trunc(horaSuerte / 24)
   
    print(f"Edad : {edad} año(s) - {meses} meses.-")
    print(f"Peso : {peso} Kg - {gramos} g.-")
    print(f"Estatura : {estatura} cm - {metros} m.-")
    print(f"Dosis de FELIX FELICIS según su edad = {dosis} ml.")
    print(f"El habitante tendrá {diasSuerte} días de SUERTE !")
    print("--------------------------------------------------")