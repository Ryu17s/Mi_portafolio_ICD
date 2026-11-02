def poblarLista():
    lista = []
    while True:
        rut = input()
        if rut == "0-0": 
            break
        nombre = input()
        altura = float(input())
        peso = int(input())
        
        tupla = (rut, nombre, altura, peso)
        lista.append(tupla)
    return lista
    
def calculoIMC(altura, peso):
    imce = (peso / altura**2)
    return round(imce, 2)
    
def listaConIMC(lista):
    listaIMC = []
    for rut, nombre, altura, peso in lista:
        imc = calculoIMC(altura, peso)
        tuplaIMC = (rut, nombre, imc)
        listaIMC.append(tuplaIMC)
    return listaIMC

lista = poblarLista()
listaIMC = listaConIMC(lista)

print("Contenido Lista de Tuplas - Datos Pacientes")
print("==============================================")
for paciente in lista:
    print(paciente)

print("\nContenido Lista de Tuplas - IMC Pacientes")
print("==============================================")
for paciente in listaIMC:
    print(paciente)

print("\nREPORTE PACIENTES CON OBESIDAD")
print("==============================")

listaDeGordos = []
esGordo = 0

for rut, nombre, imc in listaIMC:
    if imc >= 30:
        esGordo += 1
        listaDeGordos.append(nombre)

totalPaciente = len(lista)
if totalPaciente > 0:
    porcentajeGordo = round((esGordo * 100) / totalPaciente, 1)
else:
    porcentajeGordo = 0.0

if esGordo == 0:
    print("Pacientes con Obesidad : NO HAY")
else:
    print(f"Pacientes con Obesidad : {esGordo} persona(s) = {porcentajeGordo:.1f} %.")
    listaDeGordos.sort()
    print(f"Lista de Pacientes con Obesidad Ordenadas Alfabéticamente  = {listaDeGordos}")



    