# Codifique un programa que le solicite al usuario ingresar su nombre de pila y edad. En
# ambos casos se debe verificar que la entrada es válida, y en caso de no serlo, se le
# debe permitir reingresar el dato en cuestión, o abortar el programa (a elección del
# usuario).

# El nombre de pila debe ser un valor alfanumérico que contenga sólo letras (no se
# admiten números).

# La edad debe ser un valor numérico mayor a 18 y menor a 99 (19-98)

# Cuando se obtengan los dos valores correctamente, el programa debe
# simplemente saludar al usuario mostrando su nombre y edad.

# PSEUDOCODIGO
# nombre <- Ingresar y validar el nombre
# edad <- Ingresar y validar la edad
# Saludar usuario(nombre, edad)

seguir = True
# Pido y valido nombre
while seguir:
    nombre = input("Ingrese su nombre (X para abortar): ")
    if nombre == "X":
        seguir = False
    elif not nombre.isalpha():
        print(
            "El nombre debe sólo contener letras (Reintente o ingrese X para abortar)"
        )
    else:
        seguir = False

# Pido y valido edad
if nombre != "X":
    seguir = True
    while seguir:
        edad = input("Ingrese su edad (X para abortar): ")
        if edad == "X":
            seguir = False
        elif not edad.isdecimal():
            print(
                "La edad debe ser un numero natural (Reintente o ingrese X para abortar)"
            )
        elif int(edad) <= 18 or int(edad) >= 99:
            print(
                "La edad debe ser mayor a 18 y menor que 99 (Reintente o ingrese X para abortar)"
            )
        else:
            seguir = False

# Saludo usuario
if nombre != "X" and edad != "X":
    print(f"Hola {nombre}! Tenes {edad} años")
