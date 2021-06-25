# Codifique un programa que solicite al usuario ingresar dos números enteros,
#  y luego informe si la suma de ambos es mayor a 100 o no

#  Agregue una función que reciba dos enteros como parámetro,
#   e informe (mostrando en pantalla) si al menos uno de los valores es mayor a 50.

# Agregue una función que reciba dos enteros como parámetro, 
# e informe (mostrando en pantalla) si ambos valores son menores que 100.


def informeMenor(numero_1, numero_2):
  if numero_1 < 100 and numero_2 < 100:
    print('ambos son menores que 100')
  else:
    print('al menos un numero es mayor o igual que 100')

informeMenor(10,100)

es_verdadera = True

if 40 > 10:
  es_verdadera = not es_verdadera