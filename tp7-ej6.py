# Cree un script que le solicite al usuario ingresar 10 números, y una vez
# ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
# ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32,
# 9, y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
# ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1

# numero_mayor= 0
# posicion = 0
numero_mayor =int(input('ingrese un numero'))
posicion = 1
for i in range(2,5):
    numero = int (input('ingrese un numero'))
    # if i == 1:
    #     numero_mayor = numero
    #     posicion = 1
    if numero > numero_mayor:
        numero_mayor = numero
        posicion = i  

print(f'El numero mayor ingresado es {numero_mayor} en la posicion {posicion}')


# Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
# programa debe ser capaz de solicitarle al usuario que reingrese el número
# cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
# vez que detecte un error de validación, informele al usuario cuál fue el error, con
# los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
# fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
# válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.

no_valido = True

while no_valido:

    numero = input("Ingrese un numero entero entre 1 y 100: ")
    esunentero = str.isdigit(numero)
    print(esunentero)

    if esunentero:
        numero=int(numero)
        if numero >= 1 and numero <= 100:
            print(f"{numero} es válido. Gracias!")
            no_valido = False
        else:
            print(f"El número ingresado está fuera del rango permitido.")
    else:
        print(f"El dato ingresado no es numérico.")
    
    

# Una forma mejorada de hacerlo
# while True:
#   numero = input("Ingrese un número del 1 al 100: ")
#   print(numero.isalpha())
#   if numero.isalpha():
#     print(f"El dato ingresado no es numerico.")
#   elif float(numero) >= 1 and float(numero) <= 100:
#       print(f"El número {numero} es válido. Gracias!")
#       break
#   else:
#       print(f"El número ingresado está fuera del rango permitido.")