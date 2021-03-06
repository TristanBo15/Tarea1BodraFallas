from métodos import check_char
from métodos import caps_switch
import pytest

''' Se hace la parametrización de todos los carácteres con su tupla'''


@pytest.mark.parametrize("char, out", [
    ('A', 0), ('B', 0),
    ('C', 0), ('D', 0),
    ('E', 0), ('F', 0),
    ('G', 0), ('H', 0),
    ('I', 0), ('J', 0),
    ('K', 0), ('L', 0),
    ('M', 0), ('N', 0),
    ('O', 0), ('P', 0),
    ('Q', 0), ('R', 0),
    ('S', 0), ('T', 0),
    ('U', 0), ('V', 0),
    ('W', 0), ('X', 0),
    ('Y', 0), ('Z', 0),
    ('a', 0), ('b', 0),
    ('c', 0), ('d', 0),
    ('e', 0), ('f', 0),
    ('g', 0), ('h', 0),
    ('i', 0), ('j', 0),
    ('k', 0), ('l', 0),
    ('m', 0), ('n', 0),
    ('o', 0), ('p', 0),
    ('q', 0), ('r', 0),
    ('s', 0), ('t', 0),
    ('u', 0), ('v', 0),
    ('w', 0), ('x', 0),
    ('y', 0), ('z', 0)])
def test_check_char(char, out):

    assert check_char(char) == out
    ''' Revisa que los valores que retorna check_char sea
          0 para entradas en el rango de caracteres'''

    ''' Parametrización de todos los carácteres A-Z, a-z para las pruebas '''


@pytest.mark.parametrize("MAY, minu", [
    ('A', 'a'), ('B', 'b'),
    ('C', 'c'), ('D', 'd'),
    ('E', 'e'), ('F', 'f'),
    ('G', 'g'), ('H', 'h'),
    ('I', 'i'), ('J', 'j'),
    ('K', 'k'), ('L', 'l'),
    ('M', 'm'), ('N', 'n'),
    ('O', 'o'), ('P', 'p'),
    ('Q', 'q'), ('R', 'r'),
    ('S', 's'), ('T', 't'),
    ('U', 'u'), ('V', 'v'),
    ('W', 'w'), ('X', 'x'),
    ('Y', 'y'), ('Z', 'z'),
    ('a', 'A'), ('b', 'B'),
    ('c', 'C'), ('d', 'D'),
    ('e', 'E'), ('f', 'F'),
    ('g', 'G'), ('h', 'H'),
    ('i', 'I'), ('j', 'J'),
    ('k', 'K'), ('l', 'L'),
    ('m', 'M'), ('n', 'N'),
    ('o', 'O'), ('p', 'P'),
    ('q', 'Q'), ('r', 'R'),
    ('s', 'S'), ('t', 'T'),
    ('u', 'U'), ('v', 'V'),
    ('w', 'W'), ('x', 'X'),
    ('y', 'Y'), ('z', 'Z')])
def test_caps_switch(charM, charm):
    assert caps_switch(charM) == charm
    ''' Se revisa que el switch está funcionando correctamente,
    retornando minusculas y mayusculas segun la entrada '''


def test_error_b():

    assert check_char('test') == 'Error #1'


''' Revisa que al ingresar un string con mas de 1 caracter,
    efectivamente retorne el error b'''


def test_error_c():

    assert check_char('17') == 'Error #2'


''' Revisa que al ingresar un string fuera del rango A-Z o a-z,
    efectivamente retorne el error c'''


def test_error_d():

    assert check_char(10) == 'Error #3'

   ''' Revisa que al ingresar un parámetro que no corresponde a un string,
        efectivamente retorne el error d'''
