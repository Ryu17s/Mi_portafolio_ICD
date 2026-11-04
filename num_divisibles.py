def poblar():
    lista = []
    while True:
        linea = input()
        sep = linea.split()
        for dato in sep:
            if dato == "FIN": return lista
        
            if dato.isdigit():
                if dato not in lista:
                    lista.append(dato)
    return lista

def esDivisible(cadenaNum):
    for i in range(len(cadenaNum)):
        sub_numero = int(cadenaNum[:i+1])
        digito = int(cadenaNum[i])
        
        if digito == 0: 
            return False
        if sub_numero % digito != 0: 
            return False
            
    return True
    
def divisibles(lista):
    div = []
    noDiv = []
    
    for dato in lista:
        if esDivisible(dato):
            div.append(dato)
        else:
            noDiv.append(dato)
    return div, noDiv
        
lista = poblar()
total = len(lista)

div, noDiv = divisibles(lista)

div_ordenada = sorted([int(x) for x in div], reverse=True)
noDiv_ordenada = sorted([int(x) for x in noDiv], reverse=True) 

contSi = len(div)
contNo = len(noDiv)
if total > 0:
    porcentajeSi = round((contSi * 100) / total,1)
    porcentajeNo = round((contNo * 100) / total,1)
else:
    porcentajeSi = 0
    porcentajeNo = 0
    
print("datos ingresados =", lista)
print("\nlista de    S-Divisibles - (de mayor a menor) =", div_ordenada)
print("lista de NO S-Divisibles - (de mayor a menor) =", noDiv_ordenada, "\n")
print(f"Porcentaje    S-Divisibles = {porcentajeSi} %")
print(f"Porcentaje NO S-Divisibles = {porcentajeNo} %")