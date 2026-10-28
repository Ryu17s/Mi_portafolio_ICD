def filtroEnMenu(t,m,menu):
    print(f"Listado de {t} (s) menores a $ {m} :")
    hay = False
    for cod,nombre,tipo,valor in menu:
        if tipo == t and m > valor:
            hay = True
            print(f"{nombre} = $ {valor}")
    if not hay:
        print("no hay información disponible")

def valorarConsumo(consumo,menu):
    print("cantidad - plato - valor")
    print("------------------------")
    total = 0
    for codPed,cant in consumo:
        for codPlato,nombre,tipo,valor in menu:
            if codPed == codPlato:
                costo = valor * cant
                total += costo
                print(f"{cant} {nombre} $ {costo}")
                break
    print("TOTAL = $",total)
    
    
    
    
