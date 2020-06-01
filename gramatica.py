# -----------------------------------------------------------------------------
# Gary Ortiz
# 200915609 Compiladores 2 Proyecto 1
#
# Gramatica para proyecto 1 Augus
# -----------------------------------------------------------------------------

tokens = [
    'MAIN',
    'IMPRIMIR',
    'UNSET',
    'READ',
    'GOTO',
    'EXIT',
    'ABS',
    'IF',
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
    'ID',
    'RESIDUO',
    'NOT',
    'AND',
    'OR',
    'XOR',
    'SHIFTDER',
    'SHIFTIZQ'
]

t_DOSPUNTOS     = r':'
t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_IGUAL         = r'='
t_PUNTERO       = r'\&'
t_PUNTOCOMA     = r';'
t_SUMA          = r'\+'
t_RESTA         = r'-'
t_MULTI         = r'\*'
t_DIV           = r'/'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_IGUALQUE      = r'=='
t_NIGUALQUE     = r'!='
t_RESIDUO       = r'%'
t_NOT           = r'!'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_XOR           = r'xor'
t_SHIFTDER      = r'>>'
t_SHIFTIZQ      = r'<<'

t_MAIN          = r'main'
t_IMPRIMIR      = r'print'
t_UNSET         = r'unset'
t_READ          = r'read'
t_GOTO          = r'goto'
t_ABS           = r'abs'
t_IF            = r'if'

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


def t_CADENA(t):
    r'\".*?\"'
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
    ('left','MULTI','DIV'),
    )


def p_init(t) :
    'inicio            : instrucciones'
    t[0] = t[1]
    print(t[0])
def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : MAIN DOSPUNTOS
                        | ENTERO   '''
    t[0] = t[1]


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

f = open("./prueba.txt", "r")
input = f.read()
print(input)
parser.parse(input)