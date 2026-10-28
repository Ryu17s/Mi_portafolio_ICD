def poblarLista(dias):
    listaDias = []
    for i in range(dias):
        listaDias.append(int(input()))
    return listaDias
    
def realizarAccion(lista,palabra):
    if palabra == "AGREGAR":
        dato = int(input())
        lista.append(dato)
        print(f"AGREGAR {dato} - nueva lista:",lista)
    
    elif palabra == "INSERTAR":
        posicion = int(input())
        dato2 = int(input())
        lista.insert(posicion,dato2)
        print(f"INSERTAR {posicion} {dato2} - nueva lista:",lista)
    
    elif palabra == "ELIMINAR":
        dato = int(input())
        if dato in lista:
            lista.remove(dato)
            print(f"ELIMINAR {dato} - nueva lista:",lista)
        else:
            print(f"ELIMINAR - {dato} no está en la lista")

dias = int(input())
listaDias = poblarLista(dias)
print("Lista inicial de ventas de cafés es:",listaDias,"\n")

palabra = input()
while palabra != "FIN":
    realizarAccion(listaDias,palabra)
    palabra = input()
    
print()
print("Estadísticas")
print("============")
print("Total de ventas =",sum(listaDias))

if len(listaDias) > 0:
    promedio = round(sum(listaDias) / len(listaDias),2)
else:
    promedio = 0
print("Promedio de ventas de cafés por día =",promedio)
print(f"Cantidad de días con ventas = 0 es:",listaDias.count(0))
if len(listaDias) > 0:
    print(f"Mayor venta fue {max(listaDias)} en día",listaDias.index(max(listaDias))+1)