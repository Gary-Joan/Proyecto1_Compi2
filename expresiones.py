from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    SUMA = 1
    RESTA = 2
    MULTI = 3
    DIV = 4

class OPERACION_LOGICA(Enum) :
    MAYORQUE = 1
    MENORQUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYOR_IGUAL_QUE = 5
    MENOR_IGUAL_QUE = 6
    IGUAL_IGUAL = 7
    NIGUAL = 8

class ExpresionNum:

    '''representa la clase de expresion numerica'''
class ExpresionBi(ExpresionNum) :
    '''representa la clase de expresion numerica de tipo binaria'''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNegativo(ExpresionNum) :
    '''representa la clase de expresion numerica de tipo negacion'''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionNumero(ExpresionNum) :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, val = 0) :
        self.val = val

class ExpresionIdentificador(ExpresionNum) :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id

class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''
class ExpresionDobleComilla(ExpresionCadena) :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''

    def __init__(self, val) :
        self.val = val

class ExpresionCadenaNumerico(ExpresionCadena) :
    '''
        Esta clase representa una expresión numérica tratada como cadena.
        Recibe como parámetro la expresión numérica
    '''
    def __init__(self, exp) :
        self.exp = exp



class ExpresionLogica() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador