
import gramatica_asc as gr
import tablasimbolo as TS
from lista_instrucciones import *
from expresiones import *



def procesar_instruccion_imprimir(instr, ts) :

    print('> ', resolver_cadena(instr.cad, ts))



def procesar_asignacion(instr, ts) :
    #print(instr.exp)
    if isinstance(instr.exp, ExpresionCadenaComillas):
        sim = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, "")
        ts.add_symbol(sim)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.CADENA, instr.exp.val)
        ts.update_symbol(simbolo)

    elif isinstance(instr.exp, ExpresionNumero):
     
        if(ts.get_symbol(instr.id)==False):
            sim = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)
            ts.add_symbol(sim)
            val = resolver_expresion_aritmetica(instr.exp, ts)
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
            ts.update_symbol(simbolo)
        else:
            val = resolver_expresion_aritmetica(instr.exp, ts)
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
            ts.update_symbol(simbolo)

    elif isinstance(instr.exp, ExpresionBi):
        if(ts.get_symbol(instr.id)==False):
            sim = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)
            ts.add_symbol(sim)
            val = resolver_expresion_aritmetica(instr.exp, ts)
        
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
            ts.update_symbol(simbolo)
        else:
            val = resolver_expresion_aritmetica(instr.exp, ts)
             
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
            ts.update_symbol(simbolo)

    elif isinstance(instr.exp, ExpresionLogicaBinaria):

        sim = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
        ts.add_symbol(sim) 
        val = resolver_expresion_logica(instr.exp, ts)
        if(val):
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 1)
        else:    
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
        ts.update_symbol(simbolo)

    elif isinstance(instr.exp, ExpresionLogicaNot):
        
        sim = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
        ts.add_symbol(sim) 
        val = resolver_expresion_logica_not(instr.exp, ts)
        if(val):
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 1)
        else:    
            simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.BOOL, 0)
        ts.update_symbol(simbolo)

    elif isinstance(instr.exp,ExpresionNegativo):
        sim = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)
        ts.add_symbol(sim)
        val = resolver_expresion_aritmetica(instr.exp, ts)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
        ts.update_symbol(simbolo)

    elif isinstance(instr.exp, ExpresionAbsoluto):
        sim = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)
        ts.add_symbol(sim)
        val = resolver_expresion_aritmetica(instr.exp, ts)
        simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
        ts.update_symbol(simbolo)
    elif isinstance(instr.exp, ExpresionID):
        if(ts.get_symbol(instr.id)==False):
            sim = TS.Simbolo(instr.id, instr.tipo, 0)
            ts.add_symbol(sim)
            val = resolver_cadena(instr.exp, ts)
            simbolo = TS.Simbolo(instr.id, instr.tipo, val)
            ts.update_symbol(simbolo)
           
        else:
            val = resolver_cadena(instr.exp, ts)
            simbolo = TS.Simbolo(instr.id, instr.tipo, val)
            ts.update_symbol(simbolo)
    elif isinstance(instr.exp,ExpresionConversion):
        if(ts.get_symbol(instr.id)==False):
           print('entro')
           val = resolver_conversion(instr.exp, ts) 
           print(type(val),val)
 
def resolver_conversion(expConv, ts):
    #print(expConv)
    if isinstance(expConv, ExpresionConversion):
      valorid = ts.get_symbol(expConv.id)  
      print(type(valorid.valor))
      if expConv.valorc == 'int':  # ##### entro conversion int
        if isinstance(valorid.valor, float):
             return int(valorid.valor)
        elif isinstance(valorid.valor, int):
             return int(valorid.valor)
        elif isinstance(valorid.valor , str):
             if len(valorid.valor)==1:
                 return ord(valorid.valor)
             else:
                 return ord(valorid.valor[0])
        elif isinstance(valorid.valor, list):
            print('es una array')

      elif expConv.valorc == 'float':# ##### entro conversion float
        print('entro float')
        if isinstance(valorid.valor, float):
             return valorid.valor
        elif isinstance(valorid.valor, int):
             return float(valorid.valor)  
        elif isinstance(valorid.valor , str):
             if len(valorid.valor)==1:
                 return float(ord(valorid.valor))
             else:
                 return float(ord(valorid.valor[0]))
        elif isinstance(valorid.valor, list):
            print('es una array')

      elif expConv.valorc == 'char':# ##### entro conversion char
        print('entro char')  
        if isinstance(valorid.valor, float):
            valorid.valor=int(valorid.valor)
            if valorid.valor >=0 and valorid.valor<=255:
                return chr(valorid.valor)
            else:
                return chr(valorid.valor % 256)
        elif isinstance(valorid.valor, int):
            if valorid.valor >=0 and valorid.valor<=255:
                return chr(valorid.valor)
            else:
                return chr(valorid.valor % 256)
        elif isinstance(valorid.valor , str):
            return valorid.valor[0]
        elif isinstance(valorid.valor, list):
            print('es una array')          


def resolver_cadena(expCad, ts) :
    
    if isinstance(expCad, ExpresionID) :
        if ts.get_symbol(expCad.id)==False:
            return False
        else:    
            return ts.get_symbol(expCad.id).valor
    elif isinstance(expCad, ExpresionBi) :

        return str(resolver_expresion_aritmetica(expCad, ts))
    elif isinstance(expCad, ExpresionCadenaComillas):

        return expCad.val
    elif isinstance(expCad, ExpresionLogicaBinaria):
        if resolver_expresion_logica(expCad,ts)==True:
            return 1
        else:
            return 0
    elif isinstance(expCad, ExpresionLogicaNot):
        if resolver_expresion_logica_not(expCad,ts)==True:
            return 1
        else:
            return 0
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
        if expNum.operador == OPERACION_ARITMETICA.RESIDUO : return exp1 % exp2
        
    elif isinstance(expNum, ExpresionNegativo) :
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionAbsoluto):
        exp = resolver_expresion_aritmetica(expNum.expAbs, ts)
        
        return abs(exp)
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.val
    elif isinstance(expNum, ExpresionID) :
        return ts.get_symbol(expNum.id).valor

def resolver_expresion_logica(expLog, ts) :
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)
    
    if expLog.operador == OPERACION_LOGICA.MAYORQUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENORQUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2
    if expLog.operador == OPERACION_LOGICA.AND : return exp1 and exp2
    if expLog.operador == OPERACION_LOGICA.OR : return exp1 or exp2
    if expLog.operador == OPERACION_LOGICA.XOR : return bool(exp1) ^ bool(exp2)

def resolver_expresion_logica_not(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.expNot, ts)
    if expLog.notoperador == OPERACION_LOGICA.NOT : return not(exp1) 

def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    if(instrucciones):
        for instr in instrucciones :
        
            if isinstance(instr, Imprimir) :
            
                procesar_instruccion_imprimir(instr, ts)

            elif isinstance(instr, Asignacion):

                procesar_asignacion(instr, ts)

            else :
                print('Error: instrucción no válida')
    else:
        print('Error: No hay instrucciones para operar')

f = open("./prueba.txt", "r")
input = f.read()

instrucciones = gr.parse(input)
ts_global = TS.tabladesimbolos()

#procesar_instrucciones(instrucciones, ts_global)