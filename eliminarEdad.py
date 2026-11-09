def poblar():
    lista = []
    cantidad = int(input())
    for i in range(cantidad):
        edad = int(input())
        lista.append(edad)
    return lista

def datoEliminar(lista,borrar):
    listaEliminar = []

    for dato in lista:
        if dato != borrar:
            listaEliminar.append(dato)
    return listaEliminar
    
    
lista = poblar()
quitar = int(input())
listaFinal = datoEliminar(lista,quitar)
print("Lista Original =",lista)
print("Largo Lista Original =",len(lista))
print("Elemento que se elimina :",quitar)
cantidadEliminado = len(lista) - len(listaFinal)
print(f"Se eliminaron {cantidadEliminado} ocurrencia(s) de la edad",quitar)
print("Lista Final =",listaFinal)
print("Largo Lista Final =",len(listaFinal))