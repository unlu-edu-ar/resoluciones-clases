# Cree un script que le solicite al usuario ingresar un número por teclado, y
# luego le informe en pantalla si su número es mayor que 10; antes de finalizar
# e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:

# Modifique el script anterior para que mantenga el funcionamiento, pero
# ahora, cuando el número no es mayor que 10, también se muestre un
# mensaje “Tu número (N) es menor o igual que 10!”.

def mayor_menor_10(numero):
    if(numero > 10):
        print("Tu numero ",numero,"es mayor que 10!")
    else:
        print("Tu numero",numero, "es menor que 10")
    
    print("Saludos")


numero_ingresado = int(input("Ingrese un numero"))

mayor_menor_10(numero_ingresado)











