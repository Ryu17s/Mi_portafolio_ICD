tiempo = int(input())
categoria = int(input())

if tiempo <= 30:
    if categoria == 4:
        cobroTotal = 800 + 200
    else:
        cobroTotal = 800
else:
    minutos_adicionales = tiempo - 30
    
    if categoria == 1:
        cobroTotal = 800 + (minutos_adicionales * 20)
        
    elif categoria == 2:
        cobroTotal = 800 + (minutos_adicionales * 25)
        
    elif categoria == 3:
        bloques_extra = minutos_adicionales // 30
        cobroTotal = 800 + (minutos_adicionales * 30) + (bloques_extra * 15)
        
    elif categoria == 4:
        bloques_extra = minutos_adicionales // 25
        cobroTotal = 800 + (minutos_adicionales * 35) + (bloques_extra * 15) + 200

print("El cobro total es",cobroTotal)