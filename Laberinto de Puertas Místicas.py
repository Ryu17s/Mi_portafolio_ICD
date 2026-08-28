def esPrimo(n):
    contD = 0
    for i in range(1, n + 1):
        if n % i == 0:
            contD += 1
    return contD == 2

def cumpleSabio(num):
    if esPrimo(num) and esPrimo(2 * num + 1):
        return True
    else:
        return False

def sumaDig(n):
    suma = 0
    while n > 0:
        dig = n % 10
        suma += dig
        n = n // 10
    return suma

def cumpleAlma(num):
    return num % sumaDig(num) == 0

def cumpleFortuna(n):
    while n > 0:
        dig = n % 10
        if dig == 7:
            return True
        n = n // 10
            
    return False
    
def cumpleArmonia(n):
    sumaInversos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sumaInversos += 1 / i
    return sumaInversos > 2
    
def cumpleDestino(n):
    actual = 1
    aumento = 1
    while actual < n:
        actual += aumento
        aumento += 1
    return actual == n
    
totalJ = 0
pSabio = 0
pFortuna = 0
pDestino = 0

while True:
    rut = input("Ingrese el RUT del jugador (o '0-0' para salir): ")
    if rut == "0-0":
        break 
    puerta = input("Ingrese el tipo de puerta (SABIO, ALMA, FORTUNA, ARMONIA, DESTINO): ")
    clave = int(input("Ingrese el número propuesto para abrir la puerta: "))
    totalJ += 1
    
    print(f"JUGADOR {totalJ} - RUT {rut}")
    print(f"ENCONTRÓ PUERTA TIPO {puerta} Y PROPONE NÚMERO {clave}")
    
    if puerta == "SABIO":
        if cumpleSabio(clave):
            print("SI PUEDE ABRIR LA PUERTA DEL SABIO.")
            pSabio += 1
        else:
            print("NO PUEDE ABRIR LA PUERTA DEL SABIO.")
    elif puerta == "ALMA":
        if cumpleAlma(clave):
            print("SI PUEDE ABRIR LA PUERTA DEL ALMA.")
        else:
            print("NO PUEDE ABRIR LA PUERTA DEL ALMA.")
    elif puerta == "FORTUNA":
        if cumpleFortuna(clave):
            print("SI PUEDE ABRIR LA PUERTA DE LA FORTUNA.")
            pFortuna += 1
        else: 
            print("NO PUEDE ABRIR LA PUERTA DE LA FORTUNA.")
            
    elif puerta == "ARMONIA":
        if cumpleArmonia(clave):
            print("SI PUEDE ABRIR LA PUERTA DE LA ARMONÍA.")
        else:
            print("NO PUEDE ABRIR LA PUERTA DE LA ARMONÍA.")
    elif puerta == "DESTINO":
        if cumpleDestino(clave):
            print("SI PUEDE ABRIR LA PUERTA DEL DESTINO.")
            pDestino += 1
        else:
            print("NO PUEDE ABRIR LA PUERTA DEL DESTINO")
    
    print()

print()
print(f"TOTAL JUGADORES PROCESADOS = {totalJ}")
print(f"TOTAL JUGADORES QUE LOGRARON ABRIR PUERTAS DEL SABIO = {pSabio}")
print(f"TOTAL JUGADORES QUE LOGRARON ABRIR PUERTAS DE LA FORTUNA = {pFortuna}")
print(f"TOTAL JUGADORES QUE LOGRARON ABRIR PUERTAS DEL DESTINO = {pDestino}")
