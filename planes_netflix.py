n = 0

while True:
    n = int(input("Cantidad: "))
    if n > 0 and n < 1001:
        break
    print("Error")
    
cont_basico = 0
cont_premium = 0
cont_premium_mas_50_gb = 0
acum_horas_basico = 0
cont_premium_intensivo = 0 

for i in range(1, n + 1):
    print(f"Usuario {i}")

    nombre = input("Ingrese nombre: ")
    plan = int(input("Ingrese plan (1 = Basico y 2 = Premium): ")) 
    minutos_mes = int(input("Ingrese minutos visualizados en el mes: "))
    dias_uso = int(input("Ingrese dias de uso en el mes: "))
    calidad = int(input("Ingrese calidad (1 = SD , 2 = HD y 3 = 4K): "))

    if calidad == 1:
        factor_gb = 1
    elif calidad == 2:
        factor_gb = 3
    else:
        factor_gb = 7

    horas_mes = minutos_mes / 60
    gb_consumidos = horas_mes * factor_gb
    promedio_diario_min = minutos_mes / dias_uso

    print(f"Usuario {nombre}, registrado")

    if plan == 2:
        cont_premium += 1
        if gb_consumidos > 80:
            cont_premium_intensivo += 1
            clasificacion = "Premium intensivo"
        else:
            clasificacion = "Premium estandar"

        if gb_consumidos > 50:
            cont_premium_mas_50_gb += 1
    else:
        cont_basico += 1
        acum_horas_basico += horas_mes

        if promedio_diario_min < 60:
            clasificacion = "Basico ocasional"
        else:
            clasificacion = "Basico activo"

    print("Horas del mes:", round(horas_mes, 2))
    print("Promedio diario (min):", round(promedio_diario_min, 2))
    print("Datos consumidos:", round(gb_consumidos, 2), "GB")
    print("Clasificación:", clasificacion)
     
print("Usuarios premium intensivo:", cont_premium_intensivo)

if cont_basico > 0:
    prom_horas_basico = acum_horas_basico / cont_basico
    print("Promedio horas usuarios Basico:", round(prom_horas_basico, 2))


if cont_premium > 0:

    porcentaje_premium_mas_50_gb = (cont_premium_mas_50_gb * 100) / cont_premium
    print("Porcentaje Premium > 50GB:", round(porcentaje_premium_mas_50_gb, 2), "%")