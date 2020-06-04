from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2
    BOOL = 3

class Simbolo():

    def __init__(self,id,tipo,valor):
        self.id  = id
        self.tipo = tipo
        self.valor = valor
        #self.declarado = declarado
        #self.dimension = dimension
        #self.referencia = referencia

class tabladesimbolos():
    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def add_symbol(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def get_symbol(self, id):
        if not id in self.simbolos:
           # print('Error: variable ', id, ' no definida.')
            return False
        return self.simbolos[id]

    def update_symbol(self, simbolo):
        if not simbolo.id in self.simbolos:
            print('Error: variable ', simbolo.id, ' no definida.')
        else:
            self.simbolos[simbolo.id] = simbolo