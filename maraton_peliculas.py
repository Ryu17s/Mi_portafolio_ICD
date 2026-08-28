bebida = int(input())
precioBebida = int(input())

pizza = int(input())
precioPizza = int(input())

palomita = int(input())
precioPalomita = int(input())

personas = int(input())


totalGasto = ((bebida * precioBebida) + (pizza * precioPizza) + (palomita * precioPalomita))
cuota = round(totalGasto / personas)
cantidadTotal = bebida + pizza + palomita

print("Total gasto compra = ",totalGasto)
print("Valor cuota por invitado = ",cuota)
print("Total items comprados = ",cantidadTotal)