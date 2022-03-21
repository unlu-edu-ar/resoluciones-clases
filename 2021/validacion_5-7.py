# Codifique un programa que le solicite al usuario ingresar su nombre de pila y edad. 
# En ambos casos se debe verificar que la entrada es válida, y en caso de no serlo, 
# se le debe permitir reingresar el dato en cuestión, o abortar el programa (a elección del usuario).

# El nombre de pila debe ser un valor alfanumérico que contenga sólo letras (no se admiten números).

# La edad debe ser un valor numérico mayor a 18 y menor a 99.

# Cuando se obtengan los dos valores correctamente, el programa debe simplemente saludar al usuario mostrando su nombre y edad.

edad = input('Edad: ')
no_quiero_salir = True
while ((not(edad.isjdigit()) or int(edad)<18 or int(edad)>99) and no_quiero_salir):
    print('La edad no es valida')
    edad = input("Ingrese una edad Vallida: . -1 para salir") 
    if edad == '-1':
        no_quiero_salir = False
print(f'tu edad es :{edad}')
nombre = input('ingrese el nombre: ')

while not nombre.isalpha() and nombre != '-1':
    print('Error') 
    nombre = input("ERROR. Ingrese un nombre válido: , -1 para salir") 

print(f'Hola que tal {nombre} tu edad es: {edad}')


# nombre = input("ingresa el nombre: ") 
# edad = "-1" 
# bandera = True 
# while(int(edad) < 18 or int(edad) > 99 and bandera and nombre.isalpha()): 
#     edad = int(input("ingrese su edad: ")) 
#     if int(edad) > 18 and int(edad) <99: 
#         print(f"la edad es: {edad}") 
#         print(f"el nombre de pila es {nombre}") 
#         bandera = False 
