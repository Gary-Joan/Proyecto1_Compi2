from enum import Enum


class TIPO_DATO(Enum):
    NUMERO = 1
    CADENA = 2
    BOOL = 3
    ARREGLO = 4

class Simbolo():
    # tipo puede ser entrero , decimal , todos los tipod de datos primitivos
    # id el nombre de la variable
    # valor si es un valor puntual guardameos el valor , si es vector creo una lista [ ]
    # rol nos indica si es una variable . si es un vec
    # tamano 
    # 
    def __init__(self,id,tipo,valor,rol,tamano,dim):
        self.id  = id
        self.tipo = tipo
        self.valor = valor
        self.rol = rol
        self.tamano=tamano
        self.dim=dim
        #self.declarado = declarado
        #self.dimension = dimension
        #self.referencia = referencia

class tabladesimbolos(object):
    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def add_symbol(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def get_symbol(self, id):
        if not id in self.simbolos:
            #print('Error: variable ', id, ' no definida.')
            return None
        else:
            return self.simbolos[id]

    def update_symbol(self, simbolo):
        if not simbolo.id in self.simbolos:
            print('Error: variable ', simbolo.id, ' no definida.')
        else:
            self.simbolos[simbolo.id] = simbolo