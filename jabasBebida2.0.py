cantBebidas = int(input())
jabas = cantBebidas // 12
sobrantes = cantBebidas % 12
print("Cantidad de jabas =", jabas)

if sobrantes == 0:
    print("todas las bebidas fueron trasladadas")
else:
    print(f"Quedan {cantBebidas % 12} sin trasladar")   

