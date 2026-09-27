def cumplePropiedad1(numero):
    copia = numero
    suma = 0
    for i in range(1,numero + 1):
        if copia % i == 0 and copia % 2 != 0:
            suma += i
    return suma < numero

def cumplePropiedad2(numero):
    copia = numero
    sumatoria = 0
    while copia > 0:
        digito = copia % 10
        if digito % 2 == 0:
            sumatoria += digito
        copia //= 10
    if sumatoria >= 5 and sumatoria <= 35:
            return True
    return False

def cumplePropiedad3(numero):
    copia = numero
    while copia > 0:
        dig = copia % 10
        if dig == 0:
            return False
        copia //= 10
    return True

def cumplePropiedad4(numero):
    copia = numero
    suma4 = 0
    k = 1
    for k in range(1,numero+1):
        suma4 += k
        if suma4 == numero:
            return True
        if suma4 > numero:
            return False
    return False
    
def esMarciano(numero):
    if cumplePropiedad1(numero) and cumplePropiedad2(numero) and cumplePropiedad3(numero) and cumplePropiedad4(numero):
        return True
    return False

a = int(input())
b = int(input())

print(f"NÚMEROS MARCIANOS EN EL INTERVALO [{a}..{b}] :\n")

contMarciano = 0

for i in range(a,b+1):
    if esMarciano(i):
        contMarciano += 1
        print(i)

if contMarciano == 0:
    print("NO HAY.")
elif contMarciano == 1:
    print(f"\nSe encontró 1 número marciano en el intervalo [{a}..{b}].")
else:
    print(f"\nSe encontraron {contMarciano} números marcianos en el intervalo [{a}..{b}].")