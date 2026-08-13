precioUnitario = int(input())
totalProducto = int(input())

precioFinal = precioUnitario * totalProducto

if totalProducto >= 10:
    precioFinal *= 0.9
    
print("Precio final = $",round(precioFinal))

