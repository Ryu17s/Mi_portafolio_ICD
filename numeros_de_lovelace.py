def suma_digitos(n):
    suma = 0
    copiaN = n
    while copiaN > 0:
        suma = suma + (copiaN % 10)
        copiaN = copiaN // 10 
    return suma
    
def cont_divisores(n):
    cant = 0
    for i in range(1, n + 1):
        if n % i == 0:
             cant += 1
    return cant

def cumple1(n):
    suma = suma_digitos(n)
    if suma % 2 != 0:
        return True
    return False 

def cumple2(n): 
    copiaN = n 
    while copiaN > 0:
        digito = copiaN % 10
        if digito == 9:  
            return True 
        copiaN = copiaN // 10 
    return False

def cumple3(n):
    if n % 2 != 0 and n > 1:
         return True
    return False

def cumple4(n):
    if cont_divisores(n) == 4:
        return True
    return False

cantidad_lovelace = 0
    
while True:
    numero = int(input("Ingrese un numero"))
    if numero <= 0:
            break
    print("----------------------------")
    print("Análisis Número" , numero)
    print("----------------------------")
    
    if cumple1(numero): 
        suma = suma_digitos(numero)
        print("SI Cumple Propiedad 1 : suma digitos", numero, "=", suma, "es impar.")
    else:
        print("NO Cumple Propiedad 1.")

    if cumple2(numero):
        print("SI Cumple Propiedad 2 : Tiene al menos un dígito igual a 9")
    else:
        print("NO Cumple Propiedad 2.")
    
    if cumple3(numero):
        mitad = numero // 2
        cont = mitad + 1
        print("SI Cumple Propiedad 3 :", numero, "=", mitad, "+", cont)
    else:
        print("NO Cumple Propiedad 3.")
    
    if cumple4(numero):
        print(f"SI Cumple Propiedad 4 : {numero} tiene 4 divisores positivos diferentes.")
    else: 
        print("NO Cumple Propiedad 4.")

    if cumple1(numero) and cumple2(numero) and cumple3(numero) and cumple4(numero):
        print("Por lo tanto, SI es de Lovelace.")
        cantidad_lovelace = cantidad_lovelace + 1
    else:
        print("Por lo tanto, NO es de Lovelace.")
    
    print("")

if cantidad_lovelace == 0:
    print("NO se encontraron números de Lovelace en el conjunto de datos.")
elif cantidad_lovelace == 1:
    print("Se encontró 1 número de Lovelace en el conjunto de datos.")
else:
    print("Se encontraron", cantidad_lovelace, "números de Lovelace en el conjunto de datos.")
    