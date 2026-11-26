def leerDatos():
    lista = []
    
    while True:
        linea = input()
        if linea == "FIN":
            break
        if linea.isdigit():
            numero = int(linea)
            if numero not in lista:
                lista.append(numero)
    
    return lista
        
def mostrar(lista, mensaje1, mensaje2):
    print("Largo Lista =", len(lista))
    if len(lista) == 0:
        print(mensaje2)
    else:
        print(f"{mensaje1} = {lista}")
    print()
        
def ordenar(lista):
    return sorted(lista)
    
def esPrimo(numero):
    if numero == 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    raizT = int(numero**0.5)
    for divisor in range(3, raizT+1):
        if numero % divisor == 0:
            return False
    return True
    
def esPalindromo(numero):
    numeroCadena = str(numero)
    numeroDadoVuelta = numeroCadena[::-1]
    if numeroDadoVuelta == numeroCadena:
        return True
    return False
    
def darVuelta(numero):
    numeroCadena = str(numero)
    numeroDadoVuelta = numeroCadena[::-1]
    return int(numeroDadoVuelta)
    
def esOmirp(numero):
    numeroVuelta = darVuelta(numero)
    if not esPalindromo(numero) and esPrimo(numero) and esPrimo(numeroVuelta):
        return True
    return False
    
def obtenerListaTuplas(lista):
    listaTuplas = []
    for numero in lista:
        if esOmirp(numero):
            tupla = (numero, True)
        else:
            tupla = (numero, False)
        listaTuplas.append(tupla)
    return listaTuplas
    
def obtenerListaOmirp(listaTuplas):
    lista = []
    for tupla in listaTuplas:
        if tupla[1] == True:
            lista.append(tupla[0])
    return lista

def obtenerListaNoOmirp(listaTuplas):
    lista = []
    for tupla in listaTuplas:
        if tupla[1] == False:
            lista.append(tupla[0])
    return lista

#{{ STUDENT_ANSWER }}

listaNumerosEnteros = leerDatos()
mostrar(listaNumerosEnteros,"Lista Números Enteros Positivos Leídos","NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS")

listaNumerosEnterosOrdenados = ordenar(listaNumerosEnteros)
mostrar(listaNumerosEnterosOrdenados,"Lista Números Enteros Positivos Ordenados","LISTA VACÍA")

listaTuplas = obtenerListaTuplas(listaNumerosEnterosOrdenados)
mostrar(listaTuplas,"Lista de Tuplas Obtenida","LISTA DE TUPLAS VACÍA")

listaOmirp = obtenerListaOmirp(listaTuplas)
mostrar(listaOmirp,"Lista de Números OMIRP","NO SE ENCONTRARON NÚMEROS OMIRP")

listaNoOmirp = obtenerListaNoOmirp(listaTuplas)
mostrar(listaNoOmirp,"Lista de Números NO OMIRP","NO SE ENCONTRARON NÚMEROS NO OMIRP")