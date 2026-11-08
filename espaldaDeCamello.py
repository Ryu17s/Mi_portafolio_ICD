def poblar():
    cantidadDatos = int(input())
    lista = []

    for i in range(1,cantidadDatos+1):
        dato = int(input())
        lista.append(dato)
    return lista
        
def esCamello(lista):
    for c in range(1,len(lista)-1):
        actual = lista[c]
        anterior = lista[c-1]
        sucesor = lista[c+1]
        
        esMayor = actual > anterior and actual > sucesor
        esMenor = actual < anterior and actual < sucesor
        if not (esMayor or esMenor):
            return False
    return True
        
#-----------------------------------------------------       
lista = poblar()

if esCamello(lista):
    print("Lista =",lista)
    print("La lista SI es espalda de camello")
else:
    print("Lista =",lista)
    print("La lista NO es espalda de camello")