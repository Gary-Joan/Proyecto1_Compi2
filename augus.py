
import gramatica_asc as gr
import tablasimbolo as TS

from acciones import acciones

import sys
sys.setrecursionlimit(10**6)

f = open("./prueba.txt", "r")
input = f.read()

Raiz = gr.parse(input)
#print(Raiz.produccion)

acciones_parser=acciones(Raiz)
acciones_parser.ejecutar()
gr.reportegramatica()
print(acciones_parser.imprimir)
print(acciones_parser.error)
gr.reporte_de_errores_lexicos()
gr.reporte_de_errores_sintacticos()


#print("\n")
#print(acciones_parser.imprimir_tabla_simbolos())

