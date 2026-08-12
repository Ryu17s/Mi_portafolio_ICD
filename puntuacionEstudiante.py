p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())

promedio = (p1 + p2 + p3 + p4) // 4

print("promedio =",promedio)

if promedio <= 100 and promedio >= 90:
    print("nota final = A")
elif promedio >= 80 and promedio <= 89:
    print("nota final = B")
elif promedio >= 70 and promedio <= 79:
    print("nota final = C")
elif promedio >= 60 and promedio <= 69:
    print("nota final = D")
else:
    print("nota final = E")