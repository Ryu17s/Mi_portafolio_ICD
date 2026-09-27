import math

def calcular_diametro(radio):
    diametro = radio * 2
    return diametro

def calcular_perimetro(radio):
    perimetro = 2 * math.pi * radio
    return perimetro
    
def calcular_area(radio):
    area = (radio ** 2 ) * math.pi
    return area
    
def calcular_area_sector(radio, angulo_grados):
    return (angulo_grados / 360.0) * math.pi * (radio ** 2)
    
def calcular_longitud_arco(radio, angulo_grados):
    return (2.0 * math.pi * radio) * (angulo_grados / 360.0)

"""
radio = float(input())
opcion = int(input())
if opcion == 1 :
    print(f"DIAMETRO CIRCUNFERENCIA = {calcular_diametro(radio)}")
elif opcion == 2 :
    print(f"PERÍMETRO CIRCUNFERENCIA = {calcular_perimetro(radio)}")  
elif opcion == 3 :
    print(f"ÁREA CIRCUNFERENCIA = {calcular_area(radio)}")  
elif opcion == 4 :
    angulo_grados = float(input())
    print(f"ÁREA SECTOR CIRCULAR = {calcular_area_sector(radio, angulo_grados)}")  
elif opcion == 5 :
    angulo_grados = float(input())
    print(f"LONGITUD ARCO = {calcular_longitud_arco(radio, angulo_grados)}")  """