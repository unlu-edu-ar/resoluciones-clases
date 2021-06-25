# Cree una función que reciba dos string como parámetro (nombre1 y nombre2),
# y retorne True si nombre1 tiene más letras que nombre2, o False en caso
# contrario.

def comparar_nombre(nombre1,nombre2):
    '''
        funcion que retorn si nombre uno es mas largo que nombre dos
    '''
    comparacion = len(nombre1) > len(nombre2) 

    return comparacion

def comparar_numeros(numero1 , numero2):
    return numero1 > numero2

print(comparar_numeros(10,5))

comparar_numeros(7,7)

# primer_nombre = 5
# segundo_nombre = 10
# print(comparar_nombre(primer_nombre,segundo_nombre))
