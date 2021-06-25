# Cree un script que, dado un número de día de la semana ingresado por teclado,
# muestre el nombre de ese día en lenguaje natural. La relación entre números
# y días de la semana es la siguiente:
# 1 = Domingo.
# 2 = Lunes.
# 3 = Martes.
# 4 = Miércoles.
# 5 = Jueves.
# 6 = Viernes.
# 7 = Sábado.

def nombre_dia(numero):
    '''
    Esta función recibe un número de día y retorna el nombre
    '''
    dia_str = ''
    if numero==1:
        dia_str = 'Domingo'
    elif numero==2:
        dia_str = 'Lunes'
    elif numero==3:
        dia_str = 'Martes'
    elif numero==4:
        dia_str = 'Miércoles'
    elif numero==5:
        dia_str = 'Jueves'
    elif numero==6:
        dia_str = 'Viernes'
    elif numero==7:
        dia_str = 'Sábado'
    else:
        print('El valor ingresado no corresponde a un día')
        
    return dia_str

dia_numero = input('Ingrese el número de día: ')

# Si en dia_numero hay solo valores numéricos
if dia_numero.isdigit():
    resultado = nombre_dia(int(dia_numero))

    # Para Matias
    if resultado!='':
        print('El día', dia_numero, 'es', resultado)

    # Para Matias (II)
    if resultado!='':
        print('El día ' + str(dia_numero) + ' es ' + resultado)

    # Para Matias (III)
    if resultado!='':
        print('El día {} es {}'.format(dia_numero, resultado))

    if resultado!='':
        print(f'El día {dia_numero} es {resultado}')


else:
    print('Usted no ingresó un número válido')

