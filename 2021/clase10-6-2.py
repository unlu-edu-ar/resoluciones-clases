
# def contarLetrasNombre(nombre):
#     letras=len(nombre)
#     return(f'El nombre {nombre} tiene {letras} letras.')

# cantidad=contarLetrasNombre('Daiana')
# print(cantidad)

# def perimetro(base, altura):
#     resultado = (base + altura) * 2
#     return resultado
# base = 4
# altura = 7
# resultado2 = perimetro(base,altura)
# print(resultado2)

# Escriba una función que reciba un monto numérico en pesos argentinos y 
# retorne un string con la conversión en dólares, conteniendo la leyenda:
# "Si me das N pesos, te doy M dolares" 
# Asuma un tipo de cambio U$1 = $90
def cambioDolar(pesos):
    '''
        Funcion que recibes pesos y retorna un mensaje
    '''
    cambio_dolares = pesos//90
    return cambio_dolares
