from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    SUMA = 1
    RESTA = 2
    MULTI = 3
    DIV = 4
    RESIDUO = 5
    ABS = 6

class OPERACION_LOGICA(Enum) :
    MAYORQUE = 1
    MENORQUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYOR_IGUAL_QUE = 5
    MENOR_IGUAL_QUE = 6
    IGUAL_IGUAL = 7
    NIGUAL = 8
    NOT = 9
    AND = 10
    OR = 11
    XOR = 12

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

class ExpresionAbsoluto(ExpresionNum):
    '''representa la clase de expresion numerica de tipo absoluto'''
    def __init__(self, expAbs):
        self.expAbs = expAbs

class ExpresionLabel(ExpresionNum) :
    '''
        Esta clase representa una etiqueta.
    '''

    def __init__(self, id = "") :
        self.id = id

class ExpresionCadena :
    '''
        Esta clase representa una Expresión de tipo cadena.
    '''
class ExpresionID(ExpresionCadena):
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id
class ExpresionCadenaComillas(ExpresionCadena) :
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
class ExpresionLogicaBinaria(ExpresionLogica):

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
class ExpresionLogicaNot(ExpresionLogica):

    def __init__(self,expNot,notoperador):
        self.expNot = expNot
        self.notoperador = notoperador

class ExpresionRead():
    '''
        esta clase abastracta es para la funcion read()
    '''
class Expresionleer(ExpresionRead):

    def __init__(self):
        super().__init__()

class ExpresionConvert():
    'esta clase va servir para representar una conversion'

class ExpresionConversion(ExpresionConvert):

    def __init__(self, valorc, id):
        self.valorc = valorc
        self.id = id