# Codifique un programa que muestre en pantalla los primeros 10 números enteros, 
# comenzando desde el 1. Los números deben mostrarse uno en cada línea.

# Modifique el código para que se muestren sólo los números impares.

# Modifique el código para que se muestren los primeros 10 impares.

# acumulador = range(1,11)

# a = 1
# for i in range(1,20,2):
#     print(f'el numero {i} es el impar numero {a}')
#     a = a+1

# generar una funcion que dado un numero n devuelva su factorial
# Cree un script que le solicite al usuario ingresar un número entero, y muestre
# en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
# este ejercicio, pero recuerde que la función range no incluye al valor máacumuladorimo
# enviado como parámetro.
# factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n

#  '!4' = 1*2*3*4




def factorial(numero):
    acumulador = 1
    for factorial in range(1,numero+1):
        acumulador = acumulador * factorial
    return acumulador

n = int (input(' ingrese un numero: '))
print(factorial(n))


