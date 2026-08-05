alto = round(float(input("Ingrese medida")))
ancho =  round(float(input("Ingrese nmedida")))
manos_pintura = int(input("¿Cuantos manos hara?"))
rendimiento_litros = int(input("Ingrese rendimiento de Litros"))

superficie = alto * ancho

litros_necesarios = (superficie * manos_pintura) / rendimiento_litros

print(f"Superficie Pared = {superficie} m2")
print(f"Manos de Pintura = {manos_pintura}")
print(f"Metros Cuadrados por Litro de Pintura = {rendimiento_litros}")
print(f"Humberto necesitas comprar {litros_necesarios} litro(s) de pintura")
