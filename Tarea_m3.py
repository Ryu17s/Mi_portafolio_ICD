# Tarea M3: PUCV Play 
# ====================================
# Integrante: Julián Erazo
# RUT: 22.422.798-1
# Ingeniería Civil en Ciencia de Datos
# Paralelo 1
# ====================================


# ====================================
# BLOQUE 1: FUNCIONES DE LECTURA DE DATOS 
# ====================================

# Lee los datos del catálogo hasta encontrar la palabra "FIN_CATALOGO".
# Retorna una lista de tuplas con la información de cada contenido.
def leer_catalogo():
    lista = []
    while True:
        linea = input()
        if linea == "FIN_CATALOGO":
            break
        datos = linea.split(";")
        # Posición 4 (duracion) se convierte a entero
        tupla = (datos[0], datos[1], datos[2], datos[3], int(datos[4]), datos[5], datos[6])
        lista.append(tupla)
    return lista

# Lee los datos de las visualizaciones hasta encontrar "FIN_VISUALIZACIONES".
# Retorna una lista de tuplas con los registros de reproducción de usuarios.
def leer_visualizaciones():
    lista = []
    while True:
        linea = input()
        if linea == "FIN_VISUALIZACIONES":
            break
        datos = linea.split(";")
        # Posición 2(minutos vistos) se convierte a entero
        tupla = (datos[0], datos[1], int(datos[2]), datos[3])
        lista.append(tupla)
    return lista

# ====================================
# BLOQUE 2: FUNCIONES DE BÚSQUEDA Y CÁLCULOS 
# ====================================

# Recorre el catálogo buscando un código específico.
# Retorna la tupla del contenido si lo encuentra, o una tupla vacía si no.
def buscar_contenido(catalogo, codigo):
    for c in catalogo:
        if c[0] == codigo:
            return c
    return ()

# Calcula qué porcentaje del contenido original alcanzó a ver el usuario.
def calcular_porcentaje(minutos_vistos, duracion_total):
    return (minutos_vistos * 100) / duracion_total

# Clasifica la visualización según las reglas del negocio:
# >= 90% (completa), entre 50% y 89% (parcial), < 50% (abandonada).
def clasificar_visualizacion(porcentaje):
    if porcentaje >= 90:
        return "completa"
    elif porcentaje >= 50:
        return "parcial"
    else:
        return "abandonada"

# Verifica si la visualización se hizo desde un dispositivo móvil.
def es_movil(dispositivo):
    if dispositivo == "CELULAR" or dispositivo == "TABLET":
        return True
    return False

# ====================================
# BLOQUE 3: FUNCIONES DE ESTADÍSTICAS Y CRUCES DE DATOS
# ====================================

# Busca coincidencias exactas de una etiqueta dentro del string de etiquetas 
# de cada contenido, separándolas por la coma.
def contar_por_etiqueta(catalogo, etiqueta_buscada):
    contador = 0
    for c in catalogo:
        lista_etiquetas = c[6].split(",")
        if etiqueta_buscada in lista_etiquetas:
            contador += 1
    return contador

# Cruza el catálogo con las visualizaciones para encontrar el código más repetido.
# Respeta el orden del catálogo original en caso de empates.
def obtener_mas_visto(catalogo, visualizaciones):
    max_vistas = -1
    codigo_ganador = ""
    for c in catalogo:
        codigo_actual = c[0]
        vistas_actuales = 0
        for v in visualizaciones:
            if v[1] == codigo_actual:
                vistas_actuales += 1
        if vistas_actuales > max_vistas:
            max_vistas = vistas_actuales
            codigo_ganador = codigo_actual
    return codigo_ganador, max_vistas

# Verifica las estadísticas de un usuario y evalúa si cumple las condiciones
# para ser clasificado como "Usuario destacado".
def analizar_usuario(visualizaciones, catalogo, usuario):
    cantidad_vis = 0
    minutos_totales = 0
    completas = 0
    for v in visualizaciones:
        if v[0] == usuario:
            cantidad_vis += 1
            minutos_totales += v[2]
            contenido = buscar_contenido(catalogo, v[1])
            porcentaje = calcular_porcentaje(v[2], contenido[4])
            if clasificar_visualizacion(porcentaje) == "completa":
                completas += 1
    es_destacado = False
    if cantidad_vis >= 2 and minutos_totales >= 80 and completas >= 1:
        es_destacado = True
    return cantidad_vis, minutos_totales, es_destacado

# =============================================================================
# BLOQUE 4: GENERACIÓN DE CÓDIGO
# =============================================================================

# Genera un código promocional concatenando partes específicas de la tupla.
def generar_promo(contenido):
    cc = contenido[2][:2]
    aaa = contenido[3][:3]
    nn = contenido[0][-2:]
    etiquetas = contenido[6].split(",")
    ee = etiquetas[0][:2]
    codigo_promocional = cc + "-" + aaa + "-" + nn + "-" + ee
    return codigo_promocional.upper()

# ====================================
# PROGRAMA PRINCIPAL
# ====================================

# 1 Carga inicial de datos
catalogo = leer_catalogo()
visualizaciones = leer_visualizaciones()

# 2 Ingreso de variables de consulta
area_consulta = input().upper()
etiqueta_consulta = input().upper()
usuario_consulta = input().upper()
minimo_minutos = int(input())

# 3 Reporte de datos registrados
print("CONTENIDOS REGISTRADOS")
for c in catalogo:
    print(c)
print("Total de contenidos registrados:", len(catalogo))
print()

print("VISUALIZACIONES REGISTRADAS")
for v in visualizaciones:
    print(v)
print("Total de visualizaciones registradas:", len(visualizaciones))
print()

# 4 Procesamiento de Consultas sobre el catálogo
conteo_area = 0
minutos_disponibles = 0
mayor_duracion = -1
menor_duracion = catalogo[0][4]
titulos = []
codigos = []

for c in catalogo:
    if c[3] == area_consulta:
        conteo_area += 1
    minutos_disponibles += c[4]
    if c[4] > mayor_duracion:
        mayor_duracion = c[4]
    if c[4] < menor_duracion:
        menor_duracion = c[4]
    titulos.append(c[1])
    codigos.append(c[0])

conteo_etiqueta = contar_por_etiqueta(catalogo, etiqueta_consulta)
titulos.sort()

# Impresión de estadísticas del catálogo
print("CONSULTAS SOBRE EL CATÁLOGO")
print("Contenidos del área consultada:", conteo_area)
print("Contenidos con la etiqueta consultada:", conteo_etiqueta)
print("Total de minutos disponibles en el catálogo:", minutos_disponibles)
print("Mayor duración registrada:", mayor_duracion)
print("Menor duración registrada:", menor_duracion)
print("Títulos ordenados alfabéticamente:", titulos)

if len(titulos) < 3:
    print("Tres primeros títulos:", titulos)
else:
    print("Tres primeros títulos:", titulos[:3])

if len(codigos) < 3:
    print("Tres últimos códigos registrados:", codigos)
else:
    print("Tres últimos códigos registrados:", codigos[-3:])
print()

# 5 Procesamiento de Consultas sobre visualizaciones

total_minutos_vistos = 0
suma_porcentajes = 0
completas = 0
parciales = 0
abandonadas = 0
moviles = 0
sobre_minimo = 0

for v in visualizaciones:
    total_minutos_vistos += v[2]
    contenido = buscar_contenido(catalogo, v[1])
    porcentaje = calcular_porcentaje(v[2], contenido[4])
    suma_porcentajes += porcentaje
    
    estado = clasificar_visualizacion(porcentaje)
    if estado == "completa":
        completas += 1
    elif estado == "parcial":
        parciales += 1
    else:
        abandonadas += 1
        
    if es_movil(v[3]):
        moviles += 1
        
    if v[2] >= minimo_minutos:
        sobre_minimo += 1

promedio_porcentajes = round(suma_porcentajes / len(visualizaciones), 2)
cod_mas_visto, cant_mas_visto = obtener_mas_visto(catalogo, visualizaciones)

print("CONSULTAS SOBRE VISUALIZACIONES")
print("Total de minutos vistos:", total_minutos_vistos)
print("Promedio de porcentajes vistos:", promedio_porcentajes)

# Impresión de estadísticas de visualizaciones

contenido_mas_visto = buscar_contenido(catalogo, cod_mas_visto)
titulo_mas_visto = contenido_mas_visto[1]
print("Contenido más visto: " + cod_mas_visto + " - " + titulo_mas_visto)

print("Visualizaciones del contenido más visto:", cant_mas_visto)
print("Visualizaciones completas:", completas)
print("Visualizaciones parciales:", parciales)
print("Visualizaciones abandonadas:", abandonadas)
print("Visualizaciones móviles:", moviles)
print("Visualizaciones con minutos vistos mayor o igual al mínimo:", sobre_minimo)
print()

# 6 Consultas de Usuario

vis_usuario, min_usuario, destacado = analizar_usuario(visualizaciones, catalogo, usuario_consulta)
print("CONSULTAS SOBRE EL USUARIO")
print("Visualizaciones del usuario consultado:", vis_usuario)
print("Total de minutos vistos por el usuario consultado:", min_usuario)

if destacado:
    print("Usuario destacado: SÍ")
else:
    print("Usuario destacado: NO")
print()

# 7 Generación de Código Promocional

print("CÓDIGO PROMOCIONAL")
print("Código promocional:", generar_promo(contenido_mas_visto))