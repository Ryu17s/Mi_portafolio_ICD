tipoPasajero = input()
horaViaje = input()

if tipoPasajero == "5" or tipoPasajero == "6":
    print("valor pasaje = 250")
elif (tipoPasajero == "4" or tipoPasajero == "7") and horaViaje == "1":
    print("valor pasaje = 680")
elif (tipoPasajero == "4" or tipoPasajero == "7") and horaViaje == "2":
    print("valor pasaje = 550")
elif (tipoPasajero == "4" or tipoPasajero == "7") and horaViaje == "3":
    print("valor pasaje = 410.")