import math

def calcular_diametro(radio):
    if radio > 0:
        return radio * 2
    
def calcular_perimetro(radio):
    if radio > 0:
        return 2 * math.pi * radio

def calcular_area(radio):
    return math.pi * radio **2

def calcular_area_sector(radio, angulo_grados):
    return (math.pi * radio**2) * (angulo_grados / 360)

def calcular_longitud_arco(radio, angulo_grados):
    if radio > 0:
        return(2 * math.pi * radio) * (angulo_grados / 360)
  
#programa principal  
radio = float(input("Ingresa r"))
opcion = int(input("ingrese opcion"))
if opcion == 1:
    print(f"DIAMETRO CIRCUNFERENCIA = {calcular_diametro(radio)}")
elif opcion == 2:
    print(f"PERÍMETRO CIRCUNFERENCIA = {calcular_perimetro(radio)}")  
elif opcion == 3:
    print(f"ÁREA CIRCUNFERENCIA = {calcular_area(radio)}")  
elif opcion == 4:
    angulo_grados = float(input())
    print(f"ÁREA SECTOR CIRCULAR = {calcular_area_sector(radio, angulo_grados)}")  
elif opcion == 5:
    angulo_grados = float(input())
    print(f"LONGITUD ARCO = {calcular_longitud_arco(radio, angulo_grados)}")  