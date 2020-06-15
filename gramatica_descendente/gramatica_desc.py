# -----------------------------------------------------------------------------
# Gary Ortiz
# 200915609 Compiladores 2 Proyecto 1
#
# Gramatica para proyecto 1 Augus
# -----------------------------------------------------------------------------
from NodoArbol import NodoArbol 
import constantes
import os
from graphviz import render
from fpdf import FPDF 

def reportegramatica():
    pdf = FPDF()    
    pdf.add_page() 
    pdf.set_font("Arial", size = 10)
 
    archivo=""
    for item in reversed(constantes.reporte_gramatical):
        archivo+=item+"\n"
    #Aqui ponemos el valor de el diccionario de instruccion dentro de una archivo
    f = open("ReporteGramatical.txt", "w")
    f.write(archivo)
    f.close()
    f = open("ReporteGramatical.txt", "r") 
    pdf.cell(200, 10, txt = "REPORTE GRAMATICAL",  
         ln = 1, align = 'C') 
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 2, align = 'L') 
    
    # save the pdf with name .pdf 
    pdf.output("ReporteGramatical.pdf")  
    f.close()
    pdf.close()


def reporte_de_errores_lexicos():
    pdf = FPDF()    
    pdf.add_page() 
    pdf.set_font("Arial", size = 10)
 
    archivo=""
    f = open("ReporteErroresLexicos.txt", "w")
    f.write(constantes.errores_lexico)
    f.close()
    f = open("ReporteErroresLexicos.txt", "r") 
    pdf.cell(200, 10, txt = "REPORTE ERRORES LEXICOS",  
         ln = 1, align = 'C') 
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 2, align = 'L') 
    
    # save the pdf with name .pdf 
    pdf.output("ReporteErroresLexicos.pdf")  
    f.close()
    pdf.close()
    

def reporte_de_errores_sintacticos():
    pdf = FPDF()    
    pdf.add_page() 
    pdf.set_font("Arial", size = 10)
 
    archivo=""
    f = open("ReporteErroresSintacticos.txt", "w")
    f.write(constantes.errores_sintantico)
    f.close()
    f = open("ReporteErroresSintacticos.txt", "r") 
    pdf.cell(200, 10, txt = "REPORTE ERRORES SINTACTICOS",  
         ln = 1, align = 'C') 
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 2, align = 'L') 
    
    # save the pdf with name .pdf 
    pdf.output("ReporteErroresSintacticos.pdf")  
    f.close()
    pdf.close()

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
    render('dot', 'png', 'AST_Desc.dot') 
    #print(imprimir_arbol(nodoRaiz,0))

def graficar_arbol(arbol):
    try:
        file = open("AST_Desc.dot", "w")
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
        if(hijo!=None):
            if(isinstance(hijo,LexToken) or isinstance(hijo, str)):
                        s=0
            else:  
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
t_PUNTOCOMA     = r'\;'
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
     r'\#.*'
     pass
     # No return value. Token discarded

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.linestart = t.lexer.lexpos
    #t.lexer.lineno += len(t.value)



def t_error(t):
        a="Caracter desconocido - "+str(t.value[0])+ " - en la linea "+str(t.lexer.lineno)+ ", columna "+str(t.lexer.lexpos - t.lexer.linestart + 1)+"\n" 
        #print(a)
        constantes.errores_lexico+=str(a)
        print(a)
        
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
    constantes.reporte_gramatical.append(str(t.slice[0])+" -> " +str(t.slice[1]))
    t[0] = t[1]

    Raiz = t[0]
    #print(t[0])
    recorrer_arbol(t[0])

def p_instruccion(t) :
    '''instruccion      : MAIN DOSPUNTOS listainstrucciones '''
    constantes.reporte_gramatical.append("instruccion ->"+str(t.slice[1].type)+" "+str(t.slice[2].type))
    t[0]=t[3]

def p_listainstrucciones(t):
    'listainstrucciones : lista listainstrucciones_prima'
    #constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type) )
    #t[0]=t[2]
    
    t[0] = t[2]
    
def p_listainstrucciones_prima(t):
    'listainstrucciones_prima : lista listainstrucciones_prima'
    #t[2].append(t[-1])
    
    t[2] = agregar_hijo(t[2],t[-1])
    t[0] = t[2]
    
   
def p_lista_listainstrucciones(t):
    'listainstrucciones_prima : '
    #t[0]=[t[-1]]
    
    constantes.reporte_gramatical.append(str(t.slice[0].type+" -> <vacio>"))

    t[0] = crear_hoja('lista_inst','')
    t[0] = agregar_hijo(t[0],t[-1])

   
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
    constantes.reporte_gramatical.append(str(t.slice[0].type+" -> "+str(t.slice[1].type)))
    
    t[0]=t[1]
    #print(t[0])

def p_inst_asignacion(t):
    '''inst_asignacion : variable IGUAL expresion PUNTOCOMA 
                          '''
    #t[0]=('asig',t[1],t[3])
    #print(t[0])
  
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type)+" "+str(t.slice[3].type)+ " "+str(t.slice[4].type))
    t[0] = crear_hoja('asignacion','')
    t[0] = agregar_hijo(t[0],t[1])
    t[0] = agregar_hijo(t[0],t[3])
    
    #t[0] = Asignacion(t[1], t[3])

def p_variable_normal(t):
    'variable : VAR variable_prima'
    #t[0] = ('var',t[1])
    #print(t[0])
    #constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type))
    t[0] = crear_hoja('variable','')
    hijo = crear_hoja('var', t[1])
    t[0] = agregar_hijo(t[0],hijo)
def p_variable_prima(t):
    'variable_prima : var_arreglo variable_prima' 
    t[2] = agregar_hijo(t[2],t[-1])
    t[0] = t[2]

def p_variable_arreglo_lista(t):
    'variable_prima  : '

    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> <vacio>")
    t[0] =t[-1]
    if len(t[0].hijos)==1:
        hijo = crear_hoja('param_accesso','')
        hijos = t[-3]
        hijo = agregar_hijo(hijo,hijos)
        t[0] = agregar_hijo(t[0],hijo)
    else:
        
        hijo = t[0].hijos
        hijos = t[-3]
        hijo = agregar_hijo(hijo,hijos)
    

def p_variable_cochetes(t):
    'var_arreglo : LLAVEIZQ valorp LLAVEDER' 
   
    # constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type)+" "+str(t.slice[3].type))
    t[0] = t[2]
   

def p_inst_asignacion_numerica(t):
    'expresion : expresion_num'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type))
    t[0]= t[1]

def p_inst_asignacion_conversion(t):
    'expresion : conversion'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type))
    t[0] = t[1]
def p_inst_asignacion_read(t):
    'expresion : leer_valor'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type))
    t[0] = t[1]

def p_inst_asignacion_arreglo(t):
    'expresion : variable'
   
    # constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type))
    t[0] = crear_hoja('valorIMP','')
    t[0] = agregar_hijo(t[0],t[1])
    #t[0]=('valor_imp',t[1])
def p_inst_array(t):
    'expresion : inst_array'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type))
    t[0] = t[1]

def p_expresion_numerica_binaria(t):
    'expresion_num : valorp op valorp'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type)+" "+str(t.slice[3].type))
                        
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
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
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
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type))
    t[0] = crear_hoja('negativo','')
    t[0] = agregar_hijo(t[0],t[2])


def p_expresion_absoluto(t):
    'expresion_num : ABSOLUTO PARIZQ valorp PARDER '
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2]-type)+" "+str(t.slice[3].type)+" "+str(t.slice[4].type))
    #print(t[3])
   # t[0] = ExpresionAbsoluto(t[3])
    t[0] = crear_hoja('abs','')
    t[0] = agregar_hijo(t[0],t[3])
   
def p_expresion_unaria(t):
    'expresion_num :  valorp'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 

    t[0]=t[1]
   
def p_valorp_numerico(t):
    '''valorp : DECIMAL
    '''
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
    t[0]=crear_hoja('decimal',t[1])
    #t[0] = ExpresionNumero(t[1])
def p_valorp_numerico_entero(t):
    '''valorp : ENTERO
    '''
    # constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
    t[0] = crear_hoja('entero',t[1])
    #t[0] = ('entero',t[1])
    

def p_valorp_cadena(t):
    '''valorp : CADENA
                | STRING
                | CADENADOBLE
                
    '''
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
    t[0] = crear_hoja('cadena',t[1])
    #t[0] = ExpresionCadenaComillas(t[1])
def p_valorp_variable(t):
    'valorp : variable'
#     constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
#    # t[0] = ExpresionID(t[1])
#     t[0] = crear_hoja('var',t[1])
    #t[0]=('var',t[1])
    t[0] = t[1]


def p_valor_identificador_label(t):
    'valorp : ID'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
    t[0] = crear_hoja('etiqueta',t[1])
    

def p_expresion_relacional_not(t):
    'expresion_num : NOT valorp'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type)) 
    #t[0] = ExpresionLogicaNot(t[2], OPERACION_LOGICA.NOT)
    t[0] = crear_hoja('not_log','')
    t[0] = agregar_hijo(t[0],t[2])

def p_conversion(t):
    '''conversion : PARIZQ valor_conversion PARDER VAR
    '''
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)) 
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
    t[0] =crear_hoja('label',t[1])
    #hijo= crear_hoja('id',t[1])
    #t[0] = agregar_hijo(t[0],t[1])
    #t[0] = ExpresionLabel(t[1])

def p_inst_unset(t):
    'inst_unset : UNSET PARIZQ VAR PARDER PUNTOCOMA'
    t[0] = crear_hoja('unset','')
    t[0] = agregar_hijo(t[0],t[3])

def p_inst_exit(t):
    'inst_exit : EXIT PUNTOCOMA'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type))
    
    t[0] = crear_hoja('exit','')

def p_array(t):
    'inst_array : ARRAY PARIZQ PARDER'
    t[0] = crear_hoja('array','')  

def p_inst_imprimir(t):
    'inst_imprimir       : IMPRIMIR PARIZQ expresion PARDER PUNTOCOMA'
    # constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type)+" "+str(t.slice[3].type)+" "+str(t.slice[4].type)+" "+str(t.slice[5].type))
    # #t[0] = Imprimir(t[3])
    t[0] = crear_hoja('imprimir','')
    t[0] = agregar_hijo(t[0],t[3])
    #t[0] =('imprimir',t[3])

    
def p_inst_if(t):
    'inst_if : IF PARIZQ expresion PARDER GOTO ID PUNTOCOMA'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+""+str(t.slice[2].type)+" "+str(t.slice[3].type)+" "+str(t.slice[4].type)+str(t.slice[5].type)+" "+str(t.slice[6].type)+" "+str(t.slice[7].type))
    #print(t[1],t[2],t[3],t[4],t[5],t[6], t[7])
    t[0] = crear_hoja('sentenciaif','')
    t[0] = agregar_hijo(t[0],t[3])
    hijo_go = crear_hoja('goto','')
    hijo= crear_hoja('label',t[6])
    hijo_go= agregar_hijo(hijo_go,hijo)
    t[0] = agregar_hijo(t[0],hijo_go)

def p_inst_goto(t):
    'inst_goto : GOTO ID PUNTOCOMA'
    constantes.reporte_gramatical.append(str(t.slice[0].type)+" -> "+str(t.slice[1].type)+" "+str(t.slice[2].type)+" "+str(t.slice[3].type)) 
    #print(t[1],t[2])
    t[0] = crear_hoja('goto','')
    hijo = crear_hoja('label',t[2])
    t[0] = agregar_hijo(t[0],hijo)


#////////////////////////////////////////////////////////////////////////////////////




#encontrar columna


#ERRORES

def p_error(p):
    try:
        error= "Error sintactico en token "+str(p.value)+" linea "+str(p.lexer.lineno)+" columna "+str(p.lexer.lexpos - p.lexer.linestart  )+"\n"
        constantes.errores_sintantico+=str(error)
        print(error)
    except:
        error= "Error sintactico"
        constantes.errores_sintantico+=str(error)
        print(error)

import ply.yacc as yacc
from ply.lex import LexToken
parser = yacc.yacc()

f = open("./gramatica_descendente/prueba.txt", "r")
input = f.read()

parser.parse(input)


def parse(input) :
    Raiz=parser.parse(input)
    return Raiz