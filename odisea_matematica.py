import math

def validar(): 
    while True:
        numeroValidado = int(input("Ingrese la cantidad de jugadores (entre 1 y 999): "))
        if numeroValidado > 0 and numeroValidado < 1000:
             break
    return numeroValidado
    
def gauss(n): 
    if n <= 1:
        return False
        
    cont = 1
    raiz = int(math.sqrt(n))
    
    for i in range(2, raiz + 1):
        if n % i == 0:
            if i % 2 == 1:
                cont += 1
            comp = n // i 
            if comp != i and comp % 2 == 1: 
                cont += 1
                
    if n % cont == 0:
         return True
    return False
     
def borel(n):
    contMayor = 0
    contMenor = 0
    
    while n > 0:
        digito = n % 10
        n //= 10
        if digito >= 5:
            contMayor += 1
        else:
            contMenor += 1
            
    if contMenor <= contMayor:
        return True
    return False
    
def pentagonal(n):
    cont = 1 
    termino = 0
    while termino < n:
        termino = int((3 * cont**2 - cont) / 2)
        if termino == n:
            return True
        cont += 1
        
    return False

def procesar(i):
    rut = input("Ingrese rut del jugador")
    num = int(input("Ingrese el número a evaluar para el jugador"))
    
    print(f"Jugador: {i+1} - RUT: {rut}")
    
    if gauss(num) and borel(num) and pentagonal(num):
        print(f"Número {num} SI permite desbloquear portal")
        return True
        
    print(f"Número {num} NO permite desbloquear portal")
    return False

def mostrar(logrado, total_jugadores):
    print(f"Total de jugadores que SI desbloquean portal = {logrado}")
    print(f"Total de jugadores que NO desbloquean portal = {total_jugadores - logrado}")
    return

n = validar()
logrado = 0

for i in range(n):
    if procesar(i):
        logrado += 1
    print()
    
mostrar(logrado, n)