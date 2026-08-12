num1 = float(input())
operador = input()
num2 = float(input())

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
    
print("resultado =",round(resultado,1) )
    
    

    
