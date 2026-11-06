def poblar():
    lista = []
    n = int(input())
    for i in range(n):
        mensaje = input()
        lista.append(mensaje)
    return lista

def printMensaje(lista):
    print("Lista de Mensajes =",lista)

def calcularCosto(mensaje):
    total = 0
    caracterEspecial = "ñáéíóú"
    
    for c in mensaje:
        if c in caracterEspecial:
            total += 300
        elif c.isdigit():
            total += 200
        elif ("a" <= c <= "z") or ("A" <= c <= "Z"):
            total += 100
        elif c != " ":
            total += 300
    return total

def procesarMensaje(lista):
    numero = 1
    for mensaje in lista:
        costo = calcularCosto(mensaje)
        print()
        print(f"Mensaje {numero} :",mensaje)
        print("Costo es $",costo)
        numero += 1
        
#-------------------------------------------------------------
lista = poblar()
printMensaje(lista)
procesarMensaje(lista)
