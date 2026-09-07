while True:
    nComuna = int(input())
    if nComuna > 0 and nComuna <= 346: break

print("Total de Comunas a procesar :", nComuna, "\n")
print("AMPLITUDES TÉRMICAS 1 de Enero")
print("==============================", "\n")

sumaMaximas = 0
menorAmplitud = 999
comunaMenorAmp = ""
contInsignificante = 0
contMedia = 0

for i in range(1, nComuna + 1):
    nombre = input()
    print(f"Comuna # {i} nombre: {nombre}")
    minima = int(input())
    maxima = int(input())
    
    amplitud = maxima - minima
    sumaMaximas += maxima
    
    if amplitud < menorAmplitud:
        menorAmplitud = amplitud
        comunaMenorAmp = nombre
        
    if amplitud < 5:
        categoria = "INSIGNIFICANTE"
        contInsignificante += 1
    elif amplitud < 10:
        categoria = "BAJA"
    elif amplitud < 18:
        categoria = "MEDIA"
        contMedia += 1
    else:
        categoria = "ALTA"

    print("Temp. Mínima =", minima)
    print("Temp. Máxima =", maxima)
    print(f"Amplitud Térmica = {amplitud} ==> Categoria = {categoria}", "\n")
    
promMax = round(sumaMaximas / nComuna, 2)

print("REPORTE FINAL DE AMPLITUDES TÉRMICAS")
print("====================================\n")
print(f"Promedio de temperaturas máximas registradas es : {promMax} grados Celsius\n")
print(f"Menor amplitud térmica calculada : {menorAmplitud} grados Celsius - en {comunaMenorAmp}\n")

if contInsignificante > 0:
    porcInsignificante = round((contInsignificante * 100) / nComuna, 2)
    print(f"{porcInsignificante} % de Comunas en Categoría 1 - INSIGNIFICANTE\n")
else:
    print("No se procesaron comunas cuya amplitud térmica fuera insignificante.\n")

if contMedia > 0:
    porcMedia = round((contMedia * 100) / nComuna, 2)
    print(f"{porcMedia} % de Comunas en Categoría 3 - MEDIA")
else:
    print("No se procesaron comunas cuya amplitud térmica fuera media.")
