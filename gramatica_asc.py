# -----------------------------------------------------------------------------
# Gary Ortiz
# 200915609 Compiladores 2 Proyecto 1
#
# Gramatica para proyecto 1 Augus
# -----------------------------------------------------------------------------
from lista_instrucciones import *
from expresiones import *

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
    'XOR',
    'SHIFTDER',
    'SHIFTIZQ',
    'MAYORIGUALQUE',
    'MENORIGUALQUE'
]+ list(palabrasreservadas.values())

t_DOSPUNTOS     = r':'
t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_IGUAL         = r'='
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
t_XOR           = r'xor'
t_SHIFTDER      = r'>>'
t_SHIFTIZQ      = r'<<'



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

# Comentario simple // ...
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
   # print(t[0])
def p_instruccion(t) :
    '''instruccion      : MAIN DOSPUNTOS listainstrucciones '''
    t[0]=t[3]

def p_listainstrucciones(t):
    'listainstrucciones : listainstrucciones lista'
    t[1].append(t[2])
    t[0] = t[1]

def p_lista_listainstrucciones(t):
    'listainstrucciones : lista'
    t[0] = [t[1]]
def p_lista(t):
    '''lista : inst_asignacion
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
    '''inst_asignacion : VAR IGUAL expresion PUNTOCOMA
                          '''
    # print(t[3])
    t[0] = Asignacion(t[1], t[3])
def p_inst_asignacion_numerica(t):
    'expresion : expresion_num'
    t[0] = t[1] 
def p_inst_asignacion_relacional(t):
    'expresion : expresion_relacional'
    t[0] =  t[1]
def p_inst_asignacion_conversion(t):
    'expresion : conversion'
    t[0] = t[1]
def p_inst_asignacion_read(t):
    'expresion : leer_valor'
    t[0] = t[1]
def p_expresion_numerica_binaria(t):
    '''expresion_num :     expresion_num SUMA expresion_num
                         | expresion_num RESTA expresion_num
                         | expresion_num MULTI expresion_num
                         | expresion_num DIV expresion_num
                         | expresion_num RESIDUO expresion_num'''

    if   t[2] == '+':     t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.SUMA)
    elif t[2] == '-':     t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.RESTA)
    elif t[2] == '*':     t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.MULTI)
    elif t[2] == '/':     t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.DIV)
    elif t[2] == '%':     t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.RESIDUO)
    
def p_expresion_unaria(t):
    'expresion_num : RESTA expresion_num %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])   

def p_expresion_absoluto(t):
    'expresion_num : ABSOLUTO PARIZQ expresion_num PARDER '
    #print(t[3])
    t[0] = ExpresionAbsoluto(t[3])
def p_expresion_numerica_valor(t):
    'expresion_num : valorp'   
    t[0]=t[1]

def p_valorp_numerico(t):
    '''valorp : DECIMAL
                | ENTERO
    '''
    t[0] = ExpresionNumero(t[1])

def p_valorp_cadena(t):
    '''valorp : CADENA
    '''
    t[0] = ExpresionCadenaComillas(t[1])
def p_valorp_variable(t):
    'valorp : VAR'
    t[0] = ExpresionID(t[1])

def p_valor_identificador_label(t):
    'valorp : ID'
    t[0] = ExpresionLabel(t[1])
    

def p_expresion_relacional(t):
    '''expresion_relacional :        expresion_num MAYORQUE expresion_num
                                   | expresion_num MENORQUE expresion_num
                                   | expresion_num IGUALQUE expresion_num
                                   | expresion_num NIGUALQUE expresion_num
                                   | expresion_num MAYORIGUALQUE expresion_num
                                   | expresion_num MENORIGUALQUE expresion_num
                                   | expresion_num AND expresion_num
                                   | expresion_num OR expresion_num
                                   | expresion_num XOR expresion_num
                                  
    '''
    if   t[2] == '>'  : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.MAYORQUE)
    elif t[2] == '<'  : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.MENORQUE)
    elif t[2] == '==' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.DIFERENTE)
    elif t[2] == '>=' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.MAYOR_IGUAL_QUE)
    elif t[2] == '<=' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.MENOR_IGUAL_QUE)
    elif t[2] == '&&' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.AND)
    elif t[2] == '||' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.OR)
    elif t[2] == 'xor' : t[0] = ExpresionLogicaBinaria(t[1], t[3], OPERACION_LOGICA.XOR)

def p_expresion_relacional_not(t):
    'expresion_relacional : NOT expresion_num'
    t[0] = ExpresionLogicaNot(t[2], OPERACION_LOGICA.NOT)

def p_conversion(t):
    '''conversion : PARIZQ valor_conversion PARDER expresion_num
    '''
    print(t[2],t[4])
def p_valor_conversion(t):
    '''valor_conversion : INT
                        | FLOAT
                        | CHAR
    
    '''
def p_read_valor(t):
    'leer_valor : READ PARIZQ PARDER' 
    
    
def p_etiqueta(t):
    'etiqueta : ID DOSPUNTOS'
    t[0] = ExpresionLabel(t[1])

def p_inst_unset(t):
    'inst_unset : UNSET PARIZQ VAR PARDER PUNTOCOMA'


def p_inst_exit(t):
    'inst_exit : EXIT PUNTOCOMA'

def p_inst_imprimir(t):
    'inst_imprimir       : IMPRIMIR PARIZQ expresion PARDER PUNTOCOMA'
    t[0] = Imprimir(t[3])
    
def p_inst_if(t):
    'inst_if : IF PARIZQ expresion PARDER GOTO ID PUNTOCOMA'
    print(t[1],t[2],t[3],t[4],t[5],t[6], t[7])
def p_inst_goto(t):
    'inst_goto : GOTO ID PUNTOCOMA'
    print(t[1],t[2])

#////////////////////////////////////////////////////////////////////////////////////




#encontrar columna


#ERRORES
def p_error(p):
     if p:
          print("Error Sintactico en token", p)
          # Just discard the token and tell the parser it's okay.
          parser.errok()
     else:
          print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

#f = open("./prueba.txt", "r")
#input = f.read()

#parser.parse(input)


def parse(input) :
    return parser.parse(input)