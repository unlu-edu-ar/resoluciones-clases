# Codifique un programa que le solicite al usuario ingresar números enteros, 
# y que vaya mostrando el resultado de multiplicar por 2 cada uno. 
# El programa debe terminar cuando el usuario ingresa el valor especial -1


# Extienda su solución para que, antes de terminar,
#  el programa muestre en pantalla la suma total de todos los valores ingresados.

# Extienda su solución para que, antes de terminar, 
# el programa muestre en pantalla el promedio de entre todos los valores ingresados.
contador = 0
numero_ingresado = 0
suma_total = 0
while numero_ingresado != -1:
    numero_ingresado = int(input('ingresar un numero entero, "-1" para salir'))
    if numero_ingresado != -1:
        contador = contador + 1
        multiplicacion = numero_ingresado * 2
        suma_total = suma_total + numero_ingresado
        print(f'la multiplicacion es {multiplicacion}')

promedio = suma_total/contador
print ("el promedio es", promedio)

print(f'la suma fuera del while es {suma_total}')
