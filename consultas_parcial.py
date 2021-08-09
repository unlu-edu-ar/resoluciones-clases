#1 Cree un script que le solicite al usuario ingresar una temperatura en grados 
# 2 Celsius, y valide que la entrada es correcta, teniendo en cuenta que la 
# # 3 temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El 
# # 4 programa debe permitir reingresar el dato cuantas veces sea necesario, hasta 
# # 5 que el usuario provea un dato válido.Procure informar al usuario cuando su # 6 dato es inválido, y cuáles son los valores aceptados. 

# Cree un script que le solicite al usuario ingresar su edad. Verifique que el dato ingresado sea válido, teniendo en cuenta que la edad es un número entero, 
# y el rango válido para este programa es de 18 a 60 años. El programa debe solicitar el reingreso de manera indefinida, hasta que el dato sea correcto


edad = int(input('Ingrese la edad: '))

while (edad < 18 or edad > 60):
    print('invalido')
    edad = int(input('Ingrese la edad: '))

print('edad valida')