membresia = int(input())
edad = int(input())
monto = int(input())
forma_pago = int(input())

if edad < 40:
    if membresia == 1:
        porcentaje = 15
        nombre_membresia = "PREMIUM"
    elif membresia == 2:
        porcentaje = 10
        nombre_membresia = "GOLDEN"
    elif membresia == 3:
        porcentaje = 5
        nombre_membresia = "SILVER"
    else:
        porcentaje = 0
        nombre_membresia = "NO TIENE"
else:
    if membresia == 1:
        porcentaje = 20
        nombre_membresia = "PREMIUM"
    elif membresia == 2:
        porcentaje = 15
        nombre_membresia = "GOLDEN"
    elif membresia == 3:
        porcentaje = 10
        nombre_membresia = "SILVER"
    else:
        porcentaje = 5
        nombre_membresia = "NO TIENE"

monto_descuento = float(monto * porcentaje / 100)
if porcentaje == 0:
    monto_descuento = int(monto_descuento)

monto_post_descuento = float(monto - monto_descuento)
if porcentaje == 0:
    monto_post_descuento = int(monto_post_descuento)

print(f"Edad = {edad}")
print(f"Monto Compra Online = $ {monto}")
print(f"Membresía = {nombre_membresia}")
print(f"Porcentaje de descuento según edad y membresía : {porcentaje} %")
print(f"Monto de descuento según edad y membresía = $ {monto_descuento}")

if forma_pago == 2:
    print(f"Monto final a Pagar POST DESCUENTO con débito = $ {monto_post_descuento}")
elif forma_pago == 1:
    recargo = float(monto_post_descuento * 0.05)
    total_con_recargo = float(monto_post_descuento + recargo)
    print(f"Monto final a Pagar POST DESCUENTO con crédito = $ {monto_post_descuento}")
    print(f"Monto recargo por pago con crédito = $ {recargo}")
    print(f"Monto final a Pagar más RECARGO por pago con crédito = $ {total_con_recargo}")