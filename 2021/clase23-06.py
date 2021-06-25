# Cree un script que le solicite al usuario ingresar un número por teclado, y
# luego le informe en pantalla si su número es mayor que 10; antes de finalizar
# e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:
# Número mayor que 10:
# Tu número (N) es mayor que 10!
# Saludos!
# Número menor o igual que 10:
# Saludos!

# INPUT: Numero ingresado por usuario por teclado (float)
# OUTPUT: Mensaje por pantalla (str)

# CASOS DE TEST (input, salida esperada)

# Ingreso 11
# Tu número (N) es mayor que 10!
# Saludos!

# Ingreso 9
# Saludos!

# Ingreso 10
# Saludos!

# Ingreso 3.3
# Saludos!

# PSEUDOCODIGO
# x <- Pida al usuario ingresar un numero
# es_mayor <- Averiguar si x > 10
# Informar por pantalla los mensajes (x, es_mayor)


##############################
# Funciones principales
##############################


def ingresar_numero_teclado():
    """
    INPUT: --
    OUTPUT: n (float)
    Pide al usuario un numero y lo devuelve
    """
    n = float(input("Ingrese por favor un numero: "))
    return n


def averiguar_mayor_diez(n):
    """
    INPUT: n (float)
    OUTPUT: es_mayor (bool)
    Retorna True si n > 10, y False si n <=10
    """
    if n > 10:
        es_mayor = True
    else:
        es_mayor = False
    return es_mayor


def informar_pantalla(n, es_mayor):
    """
    INPUT: n (float), es_mayor (bool)
    OUTPUT: None
    ESPECIFICACION:
    Imprime los mensajes pedidos
    Número mayor que 10:
    Tu número (N) es mayor que 10!
    Saludos!
    Número menor o igual que 10:
    Saludos!
    """
    if es_mayor:
        print(f"Tu número ({n}) es mayor que 10!")
    print("Saludos!")


###################
# Funciones de test
###################


def test_averiguar_mayor_diez():
    print("Testeando averiguar_mayor_diez.... ", end="")
    assert averiguar_mayor_diez(11) == True
    assert averiguar_mayor_diez(10) == False
    assert averiguar_mayor_diez(9) == False
    print("Pasó!")


###################
# Principal
###################

# test_averiguar_mayor_diez()


def main():
    n = ingresar_numero_teclado()
    es_mayor = averiguar_mayor_diez(n)
    informar_pantalla(n, es_mayor)


if __name__ == "__main__":
    main()