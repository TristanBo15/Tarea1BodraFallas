# Aplique arreglos a sus comentarios que estaban mal hechos, solo para
# ver si la lògica de su código funcionaba, pero no corre del todo por culpa
# de la comparacion de type(x) con str, str no esta definido en ningun lado.
# ERR2 -2.5
# ERR3 -1.5


# TAREA 1 microprocesadores y microcontroladores
# Profesor: Rodolfo Piedra Camacho
# Estudiantes: Tristan B. J. y Jesús F. B.
# Fecha: 02/27/2021

# Método "check_char"


x = "A"  # Se define el parámetro de entrada


def check_char(x):
    """
    Primero verificamos si la entrada es un string
    o se encontro un error #3
    """
    if type(x) ! = str:
        return("Error #3")
        """
        Si es un string, se pasa a otro filtro, donde se define un
        contador "count" para la longitud de la cadena y un contador
        "Fuera_Rango" para saber si la cadena esta en el rango de A-Z o a-z
        """
    else:
        cont = 0
        Fuera_Rango = 0
        """
        Luego, se recorre el string con un for y se asigna un ascii a cada caracter
        y se revisa que a esté en los rangos de las letras dadas
        """
    for i in x:
        cont = cont + 1
        a = ord(i)
        if((a >= 0) and (a < 65)) or ((a >= 91)
                                      and (a <= 96)) or ((a >= 123)
                                                         and (a <= 127)):
            Fuera_Rango = Fuera_Rango + 1
        """
        Una vez se tienen los valores de "Fuera_Rango" y "cont",
        se proceden a comparar según corresponde, para identificar los
        dos errores faltantes, Error #2 si el string no está en el rango
        solicitado, o Error #1 si el string posee más de 1 caracter, si no
        cumple con las condiciones de los errores, retorna un 0, que sería una
        entrada string de 1 caracter en el rango
        """
        if Fuera_Rango >= 1:
            return("Error #2")
        elif cont > 1:
            return("Error #1")
        else:
            return 0


print(check_char(x))

"""
Definimos el parametro de entrada
del método caps_switch como un string
"""
y = "A"

"""
método caps_switch: si recibe un único
caracter dentro de los rangos A-Z o a-z devuelve
el caracter en minúscula si es mayúscula y viceversa
"""

def caps_switch(y):
    """
    llamamos al método check_char asignandolo a la
    variable c y comprueba que la entrada sea un único caracter
    dentro de alguno de los rangos deseados
    """
    c = check_char(y)
    if c == 0:
        """
        si el caracter es minúscula retorna
        su equivalente en mayuscula
        """
        if y.islower():
            u = ord(y)
            u2 = u - 32
            return(chr(u2))
        """
        si el caracter es mayúscula retorna
        su equivalente en minuscula
        """
        elif y.isupper():
            v = ord(y)
            v2 = v + 32
            return(chr(v2))
    """
    si no se cumplen las condiciones descritas anteriormente,
    la función retorna un error según check_char
    """
    else:
        return(c)


print(caps_switch(y))
# imprime el resultado del método caps_switch
