#Definicion de funciones

# calcula los N-ésimo término de la siguiente sucesión aritmética 
def alfa(n):
    resultado = 1
    for i in range(n):
        resultado += i
    return resultado

# es el valor obtenido al evaluar y sumar los 50 primeros términos de la serie numérica
def beta(x):
    suma = 0
    terminos = 1
    for n in range(1,51):
        terminos = (terminos * x) / n
        suma += terminos
    return suma

# calcula la sumatoria de todos los divisores positivos del valor n
def gama(n):
    divisores = 0
    for i in range(1,n + 1):
        if n % i == 0:
            divisores += i
    return divisores

# calcula la sumatoria de todos los números naturales impares entre 1 y el valor de n
def delta(n):
    sumaImpar = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sumaImpar += i
    return sumaImpar
    
# valida que la cantidad de habitantes sea > 0 y <= 10000
def validarHabitantes():
    while True:
        habitantes = int(input("Ingrese habitantes"))
        if habitantes > 0 and habitantes <= 10000:
            return habitantes        
    
#Programa principal

habitantes = validarHabitantes()
 
print(f"Harry, se procesarán {habitantes} habitantes del mundo mágico.")
print()
print("----- INICIO DEL PROCESO -----")
print()

for i in range(habitantes):
    edad = int(input("Ingrese edad"))
    peso = int(input("Ingrese peso"))
    estatura = int(input("Ingrese estatura"))
    meses = edad * 12
    gramos = peso * 1000
    metros = estatura / 100
    raizEdad = int(edad**0.5)
    raizGramos = int(gramos**0.5)
    
    if edad >= 1 and edad <= 20:
        dosis = (alfa(meses) * (peso)) / beta(metros)
    elif edad >= 21 and edad <= 40:
        dosis = (gama(peso) * delta(edad)) / (metros)
    elif edad >= 41 and edad <= 60:
        dosis = (gama(meses) * ((raizGramos)) / (estatura))
    else:
        dosis = (delta(peso) * (raizEdad) / (metros))
    
    dosis_ml = int(dosis)
    diasSuerte = dosis_ml // 200

    print(f"Habitante #{i + 1}")
    print(f"Edad : {edad} año(s) - {meses} meses.-" )      
    print(f"Peso : {peso} Kg - {gramos} g.-")
    print(f"Estatura : {estatura} cm - {metros} m.-")
    print(f"Dosis de FELIX FELICIS según su edad = {dosis_ml} ml.")
    print(f"El habitante tendrá {diasSuerte} días de SUERTE !")
    print("-------------------------------------------------")