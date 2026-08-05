#definicion de funciones

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
            
def suma_digitos(n):
    suma = 0
    while n > 0:
        digito = n % 10
        suma += digito
        n = n // 10
    return suma
    
def producto_digitos(n):
    producto = 1
    while n > 0:
        digito = n % 10
        producto *= digito
        n = n // 10
    return producto
    
def es_primo_truncable_derecha(n):
    while n > 0:
        if not es_primo(n):
            return False
        n //= 10
    return True
    
def suma_divisores_propios(n):
    divisores = 0
    for i in range(1,n):
        if n % i == 0:
            divisores += i
    return divisores
        
def es_deficiente(n):
    return suma_divisores_propios(n) < n

def es_triangular(n):
    suma = 0
    i = 1
    while suma < n:
        suma += i
        i += 1
    return suma == n

def contar_digitos(n):
    cont = 0
    while n > 0:
        cont += 1
        n //= 10 
    return cont
    
def es_automorfico(n):
    cuadrado = n * n
    divisor = 1
    while divisor <= n:
        divisor *= 10
        
    if cuadrado % divisor == n:
        return True
    return False
    
def persistencia_multiplicativa(n):
    cont = 0
    while n > 9:
        n = producto_digitos(n)
        cont += 1
    return cont
    
def activar_reliquia(reliquia, clave):
    if reliquia == "FUEGO":
        return es_primo_truncable_derecha(clave) and (suma_digitos(clave) % 2 == 0)
    elif reliquia == "AGUA":
        return es_deficiente(clave) and es_triangular(clave)
    elif reliquia == "TRUENO":
         return es_automorfico(clave) and (persistencia_multiplicativa(clave) == 2)
    return False

#programa principal

totalJ = 0
jFuego = 0
jAgua = 0
jTrueno = 0
noActivo = 0

while True:
    rut = int(input("Ingrese su RUT"))
    if rut == 0:
        break
    
    reliquia = input("Ingrese reliquia")
    clave = int(input("Ingrese su clave"))
    totalJ += 1

    if activar_reliquia(reliquia, clave):
        print(f"El jugador rut {rut} logró activar la reliquia de {reliquia}.")
    
        if reliquia == "FUEGO":
            jFuego += 1
        elif reliquia == "AGUA":
            jAgua += 1
        elif reliquia == "TRUENO":        
            jTrueno += 1
    else:
        print(f"El jugador rut {rut} no logró activar la reliquia de {reliquia}.")
        noActivo += 1

if totalJ == 0:
    print("No se procesan jugadores")
else:
    print()
    print("REPORTE FINAL")
    print("=============")
    print(f"Cantidad total de jugadores procesados: {totalJ}")
    print(f"Jugadores que activaron reliquias de FUEGO: {jFuego}")
    print(f"Jugadores que activaron reliquias de AGUA: {jAgua}")
    print(f"Jugadores que activaron reliquias de TRUENO: {jTrueno}")
    print(f"Jugadores que no lograron activar su reliquia: {noActivo}")