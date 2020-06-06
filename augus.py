
import gramatica_asc as gr
import tablasimbolo as TS
from lista_instrucciones import *
from expresiones import *
from acciones import acciones



f = open("./prueba.txt", "r")
input = f.read()

Raiz = gr.parse(input)
#print(Raiz.produccion)

acciones_parser=acciones(Raiz)
acciones_parser.ejecutar()
print(acciones_parser.imprimir)

