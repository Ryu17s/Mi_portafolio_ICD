def filtrarNumero(n):
    if n % 2 == 0 and n < 500 and n % 10 == 6:
        return True
    else:
        return False


"=================================================="

def alertaSistema(temperatura):
    temperatura = float(input())
    if temperatura >= 100:
        if int(temperatura) % 2 == 0:
            return "Alerta critica par" 
        else:
            return "alerta critica impar"
    else:
        return "Operacion normal."
