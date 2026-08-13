obs1 = float(input())
obs2 = float(input())
obs3 = float(input())
pres1 = float(input())
pres2 = float(input())
reporte = float(input())
prueba = float(input())

prom_reporte_prueba = (reporte + prueba) / 2
prom_obs = (obs1 + obs2 + obs3) / 3
prom_pres = (pres1 + pres2) / 2

if prom_reporte_prueba >= 4.0:
    notaPresentacion = (prueba * 0.4) + (reporte * 0.4) + (prom_obs * 0.1) + (prom_pres * 0.1)
else:
    notaPresentacion = (prueba * 0.4) + (reporte * 0.4) + (prom_pres * 0.2)

nota_redondeada = round(notaPresentacion, 1)
print(f"Nota presentación = {nota_redondeada}")

if nota_redondeada >= 5.0:
    print("Aprobado")
elif 3.0 <= nota_redondeada < 5.0:
    print("Debe rendir examen")
else:
    print("Reprobado")

if nota_redondeada > 6.0:
    print("Vuelo de observación!")