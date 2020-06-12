class NodoArbol():

    def __init__(self,produccion, valor):
        self.produccion= produccion
        self.valor = valor
        self.hijos = []
    def agregar_hijos(self,Nodo):
        self.hijos.append(Nodo)
