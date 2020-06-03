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
    'abs'   : 'ABS',
    'if'    : 'IF',
    'read'  : 'READ',
    'exit'  : 'EXIT',
    'int'   : 'INT',
    'float' : 'FLOAT',
    'char'  : 'CHAR'
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
t_AND           = r'&&'
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
    t.lexer.lineno += t.value.count("\n")


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
                | inst_unset
                | inst_goto
                | etiqueta
                | salida
                | inst_if_control'''
    t[0]=t[1]

def p_inst_asignacion(t):
    'inst_asignacion : VAR IGUAL expresion_num PUNTOCOMA'
    t[0] =Asignacion(t[1], t[3])


def p_inst_asignacion_read(t):
    'inst_asignacion  : VAR IGUAL READ PARIZQ PARDER PUNTOCOMA'

def p_inst_asignacion_cast(t):
    '''inst_asignacion : VAR IGUAL PARIZQ INT PARDER expresion_num PUNTOCOMA
                        | VAR IGUAL PARIZQ FLOAT PARDER expresion_num PUNTOCOMA
                        | VAR IGUAL PARIZQ CHAR PARDER expresion_num PUNTOCOMA'''
    if t[2] == 'int':
        t[0] = ('conv_int',t[1],t[6])
    elif t[2] == 'float':
        t[0] = ('conv_float',t[1], t[6])
    elif t[2] == 'char':
        t[0] ==('conv_char',t[1],t[6])

def p_expresion_numerica_binaria(t):
    '''expresion_num : expresion_num SUMA expresion_num
                         | expresion_num RESTA expresion_num
                         | expresion_num MULTI expresion_num
                         | expresion_num DIV expresion_num'''
    if t[2] == '+':
        t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.SUMA)

    elif t[2] == '-':
        t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.RESTA)
    elif t[2] == '*':
        t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.MULTI)
    elif t[2] == '/':
        t[0] = ExpresionBi(t[1], t[3], OPERACION_ARITMETICA.DIV)
def p_expresion_numerica_puntero(t):
    'expresion_num : puntero'

def p_expresion_numerica_logica_relacional(t):
    'expresion_num : expresion_logica_relacional'

def p_expresion_unaria(t):
    'expresion_num : RESTA expresion_num %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_logica_relacional(t):
    '''expresion_logica_relacional : expresion_num MAYORQUE expresion_num
                        | expresion_num MENORQUE expresion_num
                        | expresion_num IGUALQUE expresion_num
                        | expresion_num NIGUALQUE expresion_num
                        | expresion_num MAYORIGUALQUE expresion_num
                        | expresion_num MENORIGUALQUE expresion_num
                        | NOT expresion_num
    '''

def p_puntero(t):
    'puntero : PUNTERO VAR'
    t[0]=('puntero',t[2])

def p_expresion_numero(t):
    '''expresion_num : DECIMAL
                            | ENTERO'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_variable(t):
    '''expresion_num   : VAR   '''
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_variable_id(t):
    'expresion_num : ID'

def p_expresion_cadena(t) :
    'expresion_variable     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])
def p_expresion_cadena_numerico(t) :
    'expresion_variable     : expresion_num'
    t[0] = ExpresionCadenaNumerico(t[1])


def p_inst_imprimir(t):
    'inst_imprimir       : IMPRIMIR PARIZQ expresion_variable PARDER PUNTOCOMA'
    t[0] = Imprimir(t[3])

def p_inst_unset(t):
    'inst_unset         : UNSET PARIZQ expresion_num PARDER PUNTOCOMA'
    t[0]=('unset',t[3])
def p_inst_goto(t):
    'inst_goto          : GOTO expresion_num PUNTOCOMA'
    t[0]=('goto',t[2])

def p_etiqueta(t):
    '''etiqueta            : expresion_num DOSPUNTOS'''
    t[0]=('label',t[1])

def p_exit(t):
    'salida : EXIT PUNTOCOMA'
    t[0]=('salida',t[1])
def p_inst_if_control(t):
    '''inst_if_control : IF PARIZQ expresion_logica_relacional PARDER GOTO expresion_num PUNTOCOMA '''

#////////////////////////////////////////////////////////////////////////////////////

def encontrar_columna(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return  (token.lexpos - line_start) + 1




#ERRORES
def p_error(p):
    # Read ahead looking for a terminating ";"
    while True:
        tok = parser.token()  # Get the next token
        if not tok or tok.type == 'PUNTOCOMA': break
    parser.errok()
    print("Error sintáctico en '%s' columna '%d'" % (p.value, encontrar_columna(input, p)))

    # Return SEMI to the parser as the next lookahead token
    return tok



import ply.yacc as yacc
parser = yacc.yacc()

#f = open("./prueba.txt", "r")
#input = f.read()

#parser.parse(input)


def parse(input) :
    return parser.parse(input)