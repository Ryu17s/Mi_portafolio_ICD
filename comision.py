ventas = int(input())

if ventas < 50000:
    comision = 0
elif ventas >= 50000 and ventas < 500000:
    comision = ventas * 0.08
elif ventas >= 500000 and ventas < 1000000:
    comision = ventas * 0.1
else:
    comision = ventas * 0.15
    
print("Su comisión es de $",round(comision))