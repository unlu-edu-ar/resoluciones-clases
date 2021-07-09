# Codifique un programa que le solicite al usuario ingresar números enteros,
# y que vaya mostrando el resultado de multiplicar por 2 cada uno. El
# programa debe terminar cuando el usuario ingresa el valor especial -1.

# Extienda su solución para que, antes de terminar, el programa muestre en
# pantalla la suma total de todos los valores ingresados.

# Extienda su solución para que, antes de terminar, el programa muestre en
# pantalla el promedio de entre todos los valores ingresados.

# PROMEDIO = SUMATORIA DE LOS NUMEROS / CANTIDAD TOTAL DE NUMEROS

# INPUT: numero (int)
# OUTPUT: imprime por pantalla (None)

# PSEUDOCODIGO
# dato = Ingresa un numero
# while dato != -1:
#     if dato != -1:
#         Mostrar en pantalla 2*dato
#         dato = Ingresa un numero


def ingrese_dato():
    dato = int(input("Ingresa un numero entero (-1 para terminar): "))
    return dato


def mostrar_el_doble_dato():
    """
    Precondicion: El usuario debe ingresar numeros enteros
    OUTPUT: sumatoria (int), cardinalidad (int)
    Pide datos al usuario y muestra el doble del dato ingresado por pantalla.
    Retorna la sumatoria de los datos ingresados
    """
    # Acumulador vamos a poner la sumatoria de los numeros
    sumatoria = 0
    # Contador cuenta cuantos datos ingresa el usuario
    cardinalidad = 0
    dato = ingrese_dato()
    while dato != -1:
        if dato != -1:
            print(2 * dato)
            sumatoria += dato
            cardinalidad += 1  # cardinalidad = cardinalidad + 1
            dato = ingrese_dato()
    return sumatoria, cardinalidad


sumatoria, cardinalidad = mostrar_el_doble_dato()

# Muestro la sumatoria y el promedio
if cardinalidad != 0:
    print(f"La suma de los numeros ingresados es {sumatoria}")
    promedio = sumatoria / cardinalidad
    print(f"El promedio de los numeros es {promedio}")
else:
    print("El usuario no ingreso ningun numero")
