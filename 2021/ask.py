def mayusculas_minusculas(palabra):    
    mayus = palabra.upper()
    minus = palabra.lower()

    return minus , mayus # Retorno las dos palabras

palabra = input("Ingrese una palabra: ")

#Luego uso la funcion para asignar los dos resultados en dos variables diferentes
#que llamamos palabra_minuscula y palabra_mayuscula
palabra_minuscula, palabra_mayuscula = mayusculas_minusculas(palabra)

print("En mayuscula es ",palabra_mayuscula)
print("En minuscula es ",palabra_minuscula)