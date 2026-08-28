import math

PrecioEmpanada = int(input())
precioChicha = int(input())
asistentes = int(input())
while asistentes < 1 or asistentes > 1000:
    asistentes = int(input())
print("Cantidad de asistentes al remate dieciochero =",asistentes,"\n")

print("REMATE DIECIOCHERO")
print("===================\n")
  
totalRecaudado = 0
totalEmpanada = 0
totalChicha = 0
soloComproChicha = 0
conDescuento = 0
sinDescuento = 0
dineroSinDescuento = 0
menorMonto = 9999999999999
nombreMenor = ""

for i in range(1, asistentes + 1):
    nombre = input()
    cantidadEmpanada = int(input())
    cantidadChicha = int(input())
    
    totalEmpanada += cantidadEmpanada
    totalChicha += cantidadChicha
    
    print(f"Asistente # {i} - nombre : {nombre}")
    print(f"Ha comprado {cantidadEmpanada} empanadas y {cantidadChicha} botellas de chicha")
    
    pagarEmpanada = PrecioEmpanada * cantidadEmpanada
    pagarChicha = precioChicha * cantidadChicha
    totalSinD = pagarEmpanada + pagarChicha
    
    print("Precio total a pagar SIN descuento = $",totalSinD)
    
    if cantidadEmpanada >= 1 and cantidadEmpanada <= 5:
        descEmp = 0
    elif cantidadEmpanada >= 6 and cantidadEmpanada <= 15:
        descEmp = 0.10
    elif cantidadEmpanada > 15:
        descEmp = 0.20
    else:
        descEmp = 0
    
    if cantidadChicha >= 1 and cantidadChicha <= 10:
        descChicha = 0.05
    elif cantidadChicha >= 11 and cantidadChicha <= 20:
        descChicha = 0.10
    elif cantidadChicha > 20:
        descChicha= 0.20
    else:
        descChicha = 0
        
    if cantidadEmpanada == 0 and cantidadChicha > 0:
        soloComproChicha += 1
    
    montoDescuentoEmp = math.trunc(pagarEmpanada * descEmp)
    montDescuentoChicha = math.trunc(pagarChicha * descChicha)
    totalDesc = math.trunc(montoDescuentoEmp + montDescuentoChicha)
    precioDescuento = math.trunc(totalSinD - totalDesc)
    totalRecaudado += precioDescuento
    
    if totalDesc > 0:
        conDescuento += 1
    else:
        sinDescuento += 1
        dineroSinDescuento += precioDescuento
    
    if precioDescuento < menorMonto:
        menorMonto = precioDescuento
        nombreMenor = nombre
        
    print("Total de descuento = $",totalDesc)
    print("Precio total a pagar CON descuento = $",precioDescuento,"\n")
    
porcentajeChicha = round((soloComproChicha * 100) / asistentes, 1)
porcentajeConDescuento = round((conDescuento * 100) / asistentes, 1)

print("REPORTE FINAL - REMATE DIECIOCHERO")
print("==================================\n")
print("Total recaudación (con descuentos) = $",totalRecaudado)
print("Total empanadas =",totalEmpanada)
print("Total botellas de chicha =",totalChicha)
print(f"Porcentaje asistentes que SOLO compran chicha : {porcentajeChicha} %")
print(f"Porcentaje asistentes CON descuento : {porcentajeConDescuento} %")

if sinDescuento > 0:
    promedioSinDesc = math.trunc(dineroSinDescuento / sinDescuento)
    print(f"Promedio de compra para clientes SIN descuento = $ {promedioSinDesc}")

print(f"Asistente con MENOR monto en comprar : {nombreMenor} ( $ {menorMonto} )")