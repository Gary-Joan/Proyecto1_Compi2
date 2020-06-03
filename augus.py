import gramatica as gr
import tablasimbolo as TS
from lista_instrucciones import *
from expresiones import *

def procesar_instruccion_imprimir(instr, ts) :
    print('> ', resolver_cadena(instr.cad, ts))



def procesar_asignacion(instr, ts) :

    sim = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)
    ts.add_symbol(sim)
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)

    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    ts.update_symbol(simbolo)

def resolver_cadena(expCad, ts) :

    if isinstance(expCad, ExpresionDobleComilla) :
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico) :
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else :
        print('Error: Expresión cadena no válida')

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBi) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)

        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)

        if expNum.operador == OPERACION_ARITMETICA.SUMA : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.RESTA : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.MULTI : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIV : return exp1 / exp2
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador) :
        return ts.get_symbol(expNum.id).valor


def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, Imprimir) :
            procesar_instruccion_imprimir(instr, ts)

        elif isinstance(instr, Asignacion):
            procesar_asignacion(instr, ts)

        else : print('Error: instrucción no válida')

f = open("./prueba.txt", "r")
input = f.read()

instrucciones = gr.parse(input)
ts_global = TS.tabladesimbolos()

procesar_instrucciones(instrucciones, ts_global)