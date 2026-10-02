def transformar(celsius):
    gradosK = 0
    nuevo = []
    for i in celsius:
        gradosK = i + 273.15
        nuevo.append(gradosK)
    return nuevo
    
    
def poblar(n):
    lista = []
    for k in range(n):
        dato = int(input())
        lista.append(dato)
    return lista
    
n = int(input())
celsius = poblar(n)
kelvin = transformar(celsius)
for i in kelvin:
    print(i,end= " ")