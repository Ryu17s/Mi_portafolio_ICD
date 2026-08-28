def filtroEnMenu(tipo,monto,menu):
    print(f"Listado de {tipo} (s) menores a $ {monto} :")
    flag = False 
    for i in range(len(menu)):
        if (tipo == menu[i][2] and monto > menu[i][3]):
            flag = True
            print(f"{menu[i][1]} = $ {menu[i][3]}")
    if flag == False:
        print("no hay información disponible")    
    return

def buscarPrecioyNombre(codigo, menu):
    for codigo_plato, nombre, tipo, valor in menu:
        if codigo == codigo_plato:
            return(valor, nombre)

def valorarConsumo(consumo, menu):
    print("cantidad - plato - valor")
    print("------------------------")
    total = 0 
    for tupla in consumo:
        precio, nombre = buscarPrecioyNombre(tupla[0], menu)
        subtotal = precio * tupla[1]
        print(f"{tupla[1]} {nombre} $ {subtotal}")
        total += subtotal
        
    print(f"Total = $ {total}")


