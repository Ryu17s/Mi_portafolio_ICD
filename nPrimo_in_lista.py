def poblarLista():
    lista = []
    while True:
        dato = int(input())
        if dato < 0: break
        if not(dato in lista): lista += [dato]
    return lista
    
def esPrimo(dato):
    if dato<2: return False
    for i in range(2,int(dato**0.5)+1):
        if dato % i == 0:
            return False
    return True 

        
def identificarPrimo(lista):
    listaPrimo = []
    for dato in lista:
        if esPrimo(dato):
            listaPrimo.append(dato)
    return listaPrimo
            
lista = poblarLista()
lista.sort()
listaP = identificarPrimo(lista)

print("Lista =",lista)
print("total de elementos en la lista SIN repeticiones =",len(lista))
totalPrimo = len(listaP)

if totalPrimo == 0:
    print("La lista original NO contiene números primos.")
else:
    print("Numeros Primos en lista :", *listaP, sep=" ")
    if totalPrimo == 1:
        print("Se encontró 1 número primo en la lista original.")
    else:
        print(f"Se encontraron {totalPrimo} números primos en la lista original.")