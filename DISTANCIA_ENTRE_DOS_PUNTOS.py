import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) **2)
dRedond = round(d,1)
print("La distancia total es ",dRedond)