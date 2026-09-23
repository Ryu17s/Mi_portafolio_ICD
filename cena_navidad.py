def presupuestoCena(presupuesto,adultos_si,adultos_no,ninos):
    totalAdulto = adultos_si + adultos_no
    
    costoComida = (totalAdulto * 5000) + (ninos * 3000)
    costoBebida = (adultos_si * 3000) + ((adultos_no + ninos)* 2000)
    
    if presupuesto < costoComida:
        print(presupuesto - costoComida)
        return presupuesto - costoComida
    elif presupuesto < (costoComida + costoBebida):
        print(0)
        return 0
    else:
        print(presupuesto - (costoComida + costoBebida))
        return presupuesto - (costoComida + costoBebida)  