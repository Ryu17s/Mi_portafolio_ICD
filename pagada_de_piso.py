personas = int(input())
cantPastel = int(input())
precioPastel = int(input())
cantBebida = int(input())
precioBebida = int(input())

totalComprado = cantPastel + cantBebida
totalGastado = (cantPastel * precioPastel) + (cantBebida * precioBebida)
pagar = round(totalGastado / personas)

print("Total items comprados :",totalComprado)
print("Total gastado en pasteles y bebidas :",totalGastado)
print("Monto a pagar por cada uno :",pagar )
