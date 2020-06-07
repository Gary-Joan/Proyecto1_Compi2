# -----------------------------------------------------------------------------
# Gary Ortiz
# 200915609 Compiladores 2 Proyecto 1
#
# Gramatica para proyecto 1 Augus
# -----------------------------------------------------------------------------
from lista_instrucciones import *
from expresiones import *
from NodoArbol import NodoArbol 
import constantes
import os
from graphviz import render



def incrementar():
    constantes.numero+=1
    return constantes.numero

def crear_hoja(produccion, parametro):
    nodo = NodoArbol(produccion,parametro)
    return nodo

def agregar_hijo(nodo, hijo):
    nodo.agregar_hijos(hijo)
    return nodo

def recorrer_arbol(nodoRaiz):
    #print(nodoRaiz.hijos)
    #for nodo in nodoRaiz.hijos:
     
     #  recorrer_arbol(nodo)
    graficar_arbol(imprimir_arbol(nodoRaiz,0))
    render('dot', 'png', 'AST_asc.dot') 
    #print(imprimir_arbol(nodoRaiz,0))

def graficar_arbol(arbol):
    try:
        file = open("./AST_asc.dot", "w")
        file.write("digraph G {node[shape=box, style=filled, color=Gray95]; edge[color=blue];rankdir=UD \n" + os.linesep)

        file.write(arbol)
        file.write("\n")
        file.write("}")
        file.close()
    except IOError:
        print(IOError)
        
        


def imprimir_arbol(nodoRaiz, id):
    var=0
    cuerpo=""
    id_s=str(id)
    
    for hijo in nodoRaiz.hijos:
        var=incrementar()
        var_s=str(var)
        cuerpo += "\""+id_s+"_"+ nodoRaiz.produccion + "\"->\""+var_s+"_"+hijo.produccion+"\""+"\n"
        aux = imprimir_arbol(hijo, var)+"\n";  
        cuerpo = cuerpo + aux
    return cuerpo

palabrasreservadas = {
    'main' : 'MAIN',
    'print' : 'IMPRIMIR',
    'unset' : 'UNSET',
    'goto'  : 'GOTO',
    'abs'   : 'ABSOLUTO',
    'if'    : 'IF',
    'read'  : 'READ',
    'exit'  : 'EXIT',
    'int'   : 'INT',
    'float' : 'FLOAT',
    'char'  : 'CHAR',
    'array' : 'ARRAY',
    'xor'   : 'XOR'
}

tokens = [
    'DOSPUNTOS',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'PUNTERO',
    'COMENT',
    'PUNTOCOMA',
    'SUMA',
    'RESTA',
    'MULTI',
    'DIV',
    'MENORQUE',
    'MAYORQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'VAR',
    'ID',
    'RESIDUO',
    'NOT',
    'AND',
    'OR',
    'SHIFTDER',
    'SHIFTIZQ',
    'MAYORIGUALQUE',
    'MENORIGUALQUE',
    'LLAVEIZQ',
    'LLAVEDER',
    'STRING',
    'NOTBIT',
    'ANDBIT',
    'ORBIT',
    'XORBIT',
    'CADENADOBLE'
]+ list(palabrasreservadas.values())

t_DOSPUNTOS     = r':'
t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_IGUAL         = r'='
t_LLAVEIZQ      = r'\['
t_LLAVEDER      = r'\]'
t_PUNTERO       = r'\&'
t_PUNTOCOMA     = r';'
t_SUMA          = r'\+'
t_RESTA         = r'\-'
t_MULTI         = r'\*'
t_DIV           = r'\/'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='
t_IGUALQUE      = r'=='
t_NIGUALQUE     = r'!='
t_RESIDUO       = r'%'
t_NOT           = r'!'
t_AND           = r'\&\&'
t_OR            = r'\|\|'
t_SHIFTDER      = r'>>'
t_SHIFTIZQ      = r'<<'
t_NOTBIT        = r'\~'
t_ANDBIT        = r'\&'
t_ORBIT         = r'\|'
t_XORBIT        = r'\^'



def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_VAR(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]+'
    t.type = palabrasreservadas.get(t.value.lower(), 'VAR')
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palabrasreservadas.get(t.value.lower(), 'ID')
    return t



def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t
def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t
# Comentario simple # ...
def t_COMENTARIO(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Error de caracter '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIV','RESIDUO'),
    ('left','MAYORQUE','MENORQUE','IGUALQUE','NIGUALQUE','MAYORIGUALQUE','MENORIGUALQUE'),
    ('left','AND','NOT','OR','XOR'),
    ('right','UMENOS')
    )



def p_init(t) :
    'inicio            : instruccion'
    print("Todo correcto!")
    t[0] = t[1]
    Raiz = t[0]
    recorrer_arbol(t[0])

def p_instruccion(t) :
    '''instruccion      : MAIN DOSPUNTOS listainstrucciones '''
    t[0]=t[3]

def p_listainstrucciones(t):
    'listainstrucciones : listainstrucciones lista'
   
    t[0] = t[1]
    t[0] = agregar_hijo(t[0],t[2])

def p_lista_listainstrucciones(t):
    'listainstrucciones : lista'
    t[0] = crear_hoja('lista_inst','')
    t[0] = agregar_hijo(t[0],t[1])

   
def p_lista(t):
    '''lista :    inst_asignacion
                | inst_imprimir
                | inst_if
                | inst_goto
                | etiqueta
                | inst_unset
                | inst_exit
                | error
                '''
    t[0]=t[1]

def p_inst_asignacion(t):
    '''inst_asignacion : variable IGUAL expresion PUNTOCOMA 
                          '''
    # print(t[3])
    t[0] = crear_hoja('asignacion','')
    t[0] = agregar_hijo(t[0],t[1])
    t[0] = agregar_hijo(t[0],t[3])
    #t[0] = Asignacion(t[1], t[3])

def p_variable_normal(t):
    'variable : VAR'
   #  t[0] = ('var',t[1])
    t[0] = crear_hoja('variable','')
    hijo = crear_hoja('var', t[1])
    t[0] = agregar_hijo(t[0],hijo)

def p_variable_arreglo_lista(t):
    'variable  : variable var_arreglo '
    
    t[0] = t[1]
    hijo = crear_hoja('param_accesso','')
    hijos = t[2]
    hijo = agregar_hijo(hijo,hijos)
    t[0] = agregar_hijo(t[0],hijo)

def p_variable_cochetes(t):
    'var_arreglo : LLAVEIZQ valorp LLAVEDER' 
   
    t[0] = t[2]
   

def p_inst_asignacion_numerica(t):
    'expresion : expresion_num'
    t[0]= t[1]

def p_inst_asignacion_conversion(t):
    'expresion : conversion'
    t[0] = t[1]
def p_inst_asignacion_read(t):
    'expresion : leer_valor'
    t[0] = t[1]

def p_inst_asignacion_arreglo(t):
    'expresion : variable'
    t[0] = crear_hoja('valorIMP','')
    t[0] = agregar_hijo(t[0],t[1])
def p_inst_array(t):
    'expresion : inst_array'
    t[0] = t[1]

def p_expresion_numerica_binaria(t):
    'expresion_num : valorp op valorp'
                        

    t[0]=crear_hoja(t[2].valor,'')
    t[0]=agregar_hijo(t[0],t[1])
    t[0]=agregar_hijo(t[0],t[2])
    t[0]=agregar_hijo(t[0],t[3])

def p_op(t):
    '''op : SUMA
          | RESTA
          | MULTI
          | DIV
          | RESIDUO
          | MAYORQUE
          | MENORQUE
          | IGUALQUE
          | MAYORIGUALQUE
          | MENORIGUALQUE
          | NIGUALQUE
          | AND
          | OR
          | XOR
          | NOTBIT
          | ANDBIT
          | ORBIT
          | XORBIT   
    '''  
    if   t[1] == '+':     
             t[0]= crear_hoja('suma','exp_num')
    elif t[1] == '-':   
            t[0]= crear_hoja('resta','exp_num')
    elif t[1] == '*':    
            t[0]= crear_hoja('multi','exp_num')
    elif t[1] == '/':   
            t[0]= crear_hoja('div','exp_num')
    elif t[1] == '%':    
            t[0]= crear_hoja('residuo','exp_num')
    elif t[1] == '>'  :
            t[0]= crear_hoja('mayorque','exp_rel')
    elif t[1] == '<'  :
            t[0]= crear_hoja('menorque','exp_rel')
    elif t[1] == '==' : 
            t[0]= crear_hoja('igualque','exp_rel')
    elif t[1] == '!=' :
            t[0]= crear_hoja('noigual','exp_rel')
    elif t[1] == '>=' : 
            t[0]= crear_hoja('mayorigualque','exp_rel')
    elif t[1] == '<=' :
            t[0]= crear_hoja('menorigualque','exp_rel')
    elif t[1] == '&&' :
            t[0]= crear_hoja('and','exp_log')
    elif t[1] == '||' :
            t[0]= crear_hoja('or','exp_log')
    elif t[1] == 'xor' : 
            t[0]= crear_hoja('xor','exp_log')
    elif t[1] == '~' : 
            t[0]= crear_hoja('notbit','exp_bit_bit')            
    elif t[1] == '&' : 
            t[0]= crear_hoja('andbit','exp_bit_bit')           
    elif t[1] == '|' : 
            t[0]= crear_hoja('orbit','exp_bit_bit')
    elif t[1] == '^' : 
            t[0]= crear_hoja('xorbit','exp_bit_bit')  

def p_expresion_unaria_negativo(t):
    'expresion_num : RESTA valorp %prec UMENOS'
    t[0] = crear_hoja('negativo','')
    t[0] = agregar_hijo(t[0],t[2])


def p_expresion_absoluto(t):
    'expresion_num : ABSOLUTO PARIZQ valorp PARDER '
    #print(t[3])
   # t[0] = ExpresionAbsoluto(t[3])
    t[0] = crear_hoja('abs','')
    t[0] = agregar_hijo(t[0],t[3])
   
def p_expresion_unaria(t):
    'expresion_num :  valorp'

    t[0]=t[1]
def p_valorp_numerico(t):
    '''valorp : DECIMAL
    '''
    t[0]=crear_hoja('decimal',t[1])
    #t[0] = ExpresionNumero(t[1])
def p_valorp_numerico_entero(t):
    '''valorp : ENTERO
    '''
    t[0]=crear_hoja('entero',t[1])


def p_valorp_cadena(t):
    '''valorp : CADENA
                | STRING
                | CADENADOBLE
                
    '''
    t[0] =crear_hoja('cadena',t[1])
    #t[0] = ExpresionCadenaComillas(t[1])
def p_valorp_variable(t):
    'valorp : VAR'
   # t[0] = ExpresionID(t[1])
    t[0] = crear_hoja('var',t[1])

def p_valor_identificador_label(t):
    'valorp : ID'
    t[0] = crear_hoja('etiqueta',t[1])
    

def p_expresion_relacional_not(t):
    'expresion_num : NOT valorp'
    #t[0] = ExpresionLogicaNot(t[2], OPERACION_LOGICA.NOT)
    t[0] = crear_hoja('not_log','')
    t[0] = agregar_hijo(t[0],t[2])

def p_conversion(t):
    '''conversion : PARIZQ valor_conversion PARDER VAR
    '''
    t[0] = crear_hoja('conversion','')
    t[0] = agregar_hijo(t[0],t[2])

    hijo = crear_hoja('var',t[4])
    t[0] = agregar_hijo(t[0],hijo)
     
  
    #t[0] = ExpresionConversion(t[2],t[4])
def p_valor_conversion(t):
    '''valor_conversion : INT
                        | FLOAT
                        | CHAR
    
    '''
    if   t[1] == 'int':     
             t[0]= crear_hoja('int','conversion')
    elif t[1] == 'float':   
            t[0]= crear_hoja('float','conversion')
    elif t[1] == 'char':    
            t[0]= crear_hoja('char','conversion')
def p_read_valor(t):
    'leer_valor : READ PARIZQ PARDER' 
    
    t[0] = crear_hoja('read','')
def p_etiqueta(t):
    'etiqueta : ID DOSPUNTOS'
    t[0] =crear_hoja('label','')
    hijo= crear_hoja('id',t[1])
    t[0] = agregar_hijo(t[0],hijo)
    #t[0] = ExpresionLabel(t[1])

def p_inst_unset(t):
    'inst_unset : UNSET PARIZQ VAR PARDER PUNTOCOMA'
    t[0] = crear_hoja('unset','')
    t[0] = agregar_hijo(t[0],t[3])

def p_inst_exit(t):
    'inst_exit : EXIT PUNTOCOMA'
    t[0] = crear_hoja('exit','')

def p_array(t):
    'inst_array : ARRAY PARIZQ PARDER'
    t[0] = crear_hoja('array','')  

def p_inst_imprimir(t):
    'inst_imprimir       : IMPRIMIR PARIZQ expresion PARDER PUNTOCOMA'
    #t[0] = Imprimir(t[3])
    t[0] =crear_hoja('imprimir','')
    t[0] = agregar_hijo(t[0],t[3])
    
def p_inst_if(t):
    'inst_if : IF PARIZQ expresion PARDER GOTO ID PUNTOCOMA'
    #print(t[1],t[2],t[3],t[4],t[5],t[6], t[7])
    t[0] = crear_hoja('sentenciaif','')
    t[0] = agregar_hijo(t[0],t[3])
    hijo_go = crear_hoja('goto','')
    hijo= crear_hoja('label',t[6])
    hijo_go= agregar_hijo(hijo_go,hijo)
    t[0] = agregar_hijo(t[0],hijo_go)

def p_inst_goto(t):
    'inst_goto : GOTO ID PUNTOCOMA'
    #print(t[1],t[2])
    t[0] = crear_hoja('goto','')
    hijo = crear_hoja('label',t[2])
    t[0] = agregar_hijo(t[0],hijo)


#////////////////////////////////////////////////////////////////////////////////////




#encontrar columna


#ERRORES
def p_error(p):
     if p:
          print("Error Sintactico en token", p)
          # Just discard the token and tell the parser it's okay.
          parser.errok()
     else:
          print("\n")

import ply.yacc as yacc
parser = yacc.yacc()

#f = open("./prueba.txt", "r")
#input = f.read()

#parser.parse(input)


def parse(input) :
    Raiz=parser.parse(input)
    return Raiz