# una funcion que reciba como parametro una nota y retorne true/false si un alumno aprobo o no un examen

# mejorarla para que reciba dos notas y retorne si un alumno queda libre o regular o recupera

# si un alumno promociona 

# que diga la condicion del alumno

def aprueba(nota1,nota2):
    ''''
        Retorna la condicion de un alumno 
    '''
    promedio = (nota1 + nota2 ) // 2
    condicion = ''

    if promedio < 4:
        condicion = 'Libre'
    elif nota1 < 4 or nota2 < 4:
        condicion = 'Recupera'
    elif promedio >= 4 and promedio < 7:
        condicion = 'Regular'
    elif promedio >= 7:
        condicion = 'Promovido'
    return condicion

print(aprueba(3,2))