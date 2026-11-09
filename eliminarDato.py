def poblarLista():
    lista = []
    while True:
        dato = int(input())
        if dato < 0: break
        lista.append(dato)
    return lista
    
lista = poblarLista()
datoEliminar = int(input())

print("Lista Original =",lista)
print("Largo Lista Original =",len(lista))
print("Elemento que se elimina :",datoEliminar)
if datoEliminar in lista:
    lista.remove(datoEliminar)
print("Lista Final =",lista)
print("Largo Lista Final =",len(lista))