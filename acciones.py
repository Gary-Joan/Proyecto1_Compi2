from tablasimbolo import Simbolo, tabladesimbolos

class acciones ():
    def __init__(self,Raiz):
        self.Raiz=Raiz
        self.imprimir="---- Consola-----\n"
        self.error="----- Error ----\n"
        self.tabla_simbolos=tabladesimbolos() #instancio mi tabla simbolos
    
    def ejecutar (self,):
        self.acciones(self.Raiz)

    def acciones(self,Raiz):
        resutl=None
        if Raiz.produccion=='lista_inst':
            # listas de hijos de produccion lista de instancias
            for node in Raiz.hijos:
                resutl= self.acciones(node)
        elif Raiz.produccion=='asignacion':
            # tenes dos hijos
            izq=Raiz.hijos[0] #hijo izq el nombre de la variable
            der=Raiz.hijos[1] # hijo de derecho tenes expresion
            if len(izq.hijos)==1:
            
                izq=self.acciones(izq) # el var y esta en tablal de simblos / objeto simbolo
                der=self.acciones(der) # obtengo el resultado del arbol exp_num y me devuelve un objeto tipo simbolo o un null si hubo un error
                if der != None:
                # no hay un error en tiempo de ejecion
    
                    izq.tipo=der.tipo
                    izq.valor=der.valor
                    izq.rol = der.rol
                    self.tabla_simbolos.update_symbol(izq)
                else:
                    #existe un error en tiempo de ejecucion
                    self.error+="existe un error en la operacion \n"
            else:
                der=self.acciones(der)
            
                if der != None:
                     sim=der
                     resutl = self.acciones_array(Raiz.hijos[0],sim) 
                else:
                    self.error+="existe un error en la operacion \n"
        elif Raiz.produccion=='variable':
            if len(Raiz.hijos)==1:
                # es crear una variable simple
                izq=Raiz.hijos[0]
                resutl=self.acciones(izq)

            else:
                #pasos para accesar a un vector
               print('')

        elif Raiz.produccion=='var':
            # solo el nombre de la variable
            nombre=Raiz.valor #obtengo el nombre de la variable
            nuevo_simbolo=Simbolo(nombre,'sin','0','var','1','0')
            self.tabla_simbolos.add_symbol(nuevo_simbolo)
            resutl=nuevo_simbolo
        elif Raiz.produccion == 'imprimir':
            resutl=self.acciones(Raiz.hijos[0])
            if resutl != None:
                self.imprimir+=resutl.valor+"\n"

        elif Raiz.produccion == 'array':
            
            nuevo_simbolo=Simbolo('sin','array',{},'array','1','1')
            resutl=nuevo_simbolo
         
        elif Raiz.produccion == 'exp_num':
            resutl=self.acciones_exp_num(Raiz)

        elif Raiz.produccion == 'exp_rel':
            resutl = self.acciones_exp_rel(Raiz)
        
        elif Raiz.produccion == 'exp_log':
            resutl = self.acciones_exp_log(Raiz)

        elif Raiz.produccion == 'valorIMP':
            resutl=self.acciones_exp_num(Raiz)
        
        elif Raiz.produccion == 'entero':
            resutl = self.acciones_exp_num(Raiz)
        
        elif Raiz.produccion == 'cadena':
            resutl = self.acciones_exp_num(Raiz)
        
        elif Raiz.produccion == 'var':
            resutl = self.acciones_exp_num(Raiz)
        
        elif Raiz.produccion == 'decimal':
            resutl = self.acciones_exp_num(Raiz)
        
        elif Raiz.produccion == 'negativo':
            resutl = self.acciones_negativo(Raiz)
        
        elif Raiz.produccion == 'abs':
            resutl = self.acciones_abs(Raiz)
        
        elif Raiz.produccion == 'conversion':
            resutl = self.acciones_conversion(Raiz)

        return resutl
 #-----------------------------------------------------------------------------VALORES NEGATIVOS-------------------------------       
    def  acciones_negativo(self,Raiz):
        result = None
        if Raiz.produccion == 'negativo':
            izq = Raiz.hijos[0]
            result = self.acciones_negativo(izq)
        elif Raiz.produccion=='var' :
            # busco el simbolo en la tabla de simbolos
            nombre=Raiz.valor #obtengo el nombre de la variable
            valor_var=self.tabla_simbolos.get_symbol(nombre)
            valor_var.valor='-'+valor_var.valor
            result =self.tabla_simbolos.get_symbol(nombre)
        elif Raiz.produccion == 'entero':
            Raiz.valor = Raiz.valor*-1
            result = Simbolo('numero','entero',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'decimal':
            Raiz.valor = Raiz.valor*-1
            result = Simbolo('numero','decimal',str(Raiz.valor),'var','1','0')
        return result
 #-----------------------------------------------------------------------------VALOR ABSOLUTO---------------------------------      
    def acciones_abs(self, Raiz):
        result = None
        if Raiz.produccion == 'abs':
            izq = Raiz.hijos[0]
            result = self.acciones_abs(izq)
        elif Raiz.produccion=='var' :
            # busco el simbolo en la tabla de simbolos
            nombre=Raiz.valor #obtengo el nombre de la variable
            valor_var=self.tabla_simbolos.get_symbol(nombre)
            valor_var.valor= str(abs(int(valor_var.valor)))
            result =self.tabla_simbolos.get_symbol(nombre)
        elif Raiz.produccion == 'entero':
            Raiz.valor = abs(Raiz.valor)
            result = Simbolo('numero','entero',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'decimal':
            Raiz.valor = abs(Raiz.valor)
            result = Simbolo('numero','decimal',str(Raiz.valor),'var','1','0')
        return result
 #-----------------------------------------------------------------------------EXPRESIONES NUMERICAS------------------------------   
    def acciones_exp_num(self,Raiz):
        result=None
        if Raiz.produccion=='exp_num':
            izq = Raiz.hijos[0] # seria el valor de el lado izq
            op  = Raiz.hijos[1] # seria el operador + ,-,*,/,%
            der = Raiz.hijos[2] # seria el valor derecho
            izq=self.acciones_exp_num(izq) # ya tengo el valor del hijo izq
            der=self.acciones_exp_num(der) # ya tengo el valor del hijo der
            result=self.operaciones_aritmeticas(izq,der,op.produccion) # me regresa el objeto de tipo simbolo

        elif Raiz.produccion == 'entero':
            result = Simbolo('numero','entero',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'cadena':
            result = Simbolo('cadena','cadena',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'decimal':
            result = Simbolo('decimal','decimal',str(Raiz.valor),'var','1','0')
        
        elif Raiz.produccion == 'valorIMP':
            result = self.acciones_exp_num(Raiz.hijos[0])
        elif Raiz.produccion == 'variable':
            if len(Raiz.hijos)==1:
                # acceso a un avariable
                izq=Raiz.hijos[0]
                result=self.acciones_exp_num(izq)

            else:
                #acceso a un vector
                a=""
        
        elif Raiz.produccion=='var':
            # busco el simbolo en la tabla de simbolos
            nombre=Raiz.valor #obtengo el nombre de la variable
            result=self.tabla_simbolos.get_symbol(nombre)
        return result

    def operaciones_aritmeticas(self,izq,der,op):
        result=None
        if op == 'suma':
            if izq.tipo=="entero" and der.tipo == "entero": 
                num=int(izq.valor)+int(der.valor)
                result=Simbolo('nada','entero',str(num),'var','0','1')

            elif izq.tipo=="decimal" and der.tipo == "entero":
                num=float(izq.valor)+int(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')
            
            elif izq.tipo=="entero" and der.tipo == "decimal":
                num=float(izq.valor)+int(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

            elif izq.tipo=="decimal" and der.tipo == "decimal":
                num=float(izq.valor)+float(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

            elif izq.tipo=="cadena" and der.tipo == "cadena":
                num= izq.valor + der.valor
                result=Simbolo('nada','cadena',str(num),'var','0','1')

        elif op == 'resta':   
            if izq.tipo=="entero" and der.tipo == "entero": 
                num=int(izq.valor)-int(der.valor)
                result=Simbolo('nada','entero',str(num),'var','0','1')

            elif izq.tipo=="decimal" and der.tipo == "entero":
                num=float(izq.valor)-int(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

            elif izq.tipo=="entero" and der.tipo == "decimal":
                num=int(izq.valor)-float(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1') 

            elif izq.tipo=="decimal" and der.tipo == "decimal":
                num=float(izq.valor)-float(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

        elif op == 'multi':   
            if izq.tipo=="entero" and der.tipo == "entero": 
                num=int(izq.valor)*int(der.valor)
                result=Simbolo('nada','entero',str(num),'var','0','1')

            elif izq.tipo=="decimal" and der.tipo == "entero":
                num=float(izq.valor)*int(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

            elif izq.tipo=="entero" and der.tipo == "decimal":
                num=int(izq.valor)*float(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

            elif izq.tipo=="decimal" and der.tipo == "decimal":
                num=float(izq.valor)*float(der.valor)
                result=Simbolo('nada','decimal',str(num),'var','0','1')

        elif op == 'div':   
            try:
              
                if izq.tipo=="entero" and der.tipo == "entero": 
                    num=int(izq.valor)/int(der.valor)
                    result=Simbolo('nada','entero',str(num),'var','0','1')

                elif izq.tipo=="decimal" and der.tipo == "entero":
                    num=float(izq.valor)/int(der.valor)
                    result=Simbolo('nada','decimal',str(num),'var','0','1')

                elif izq.tipo=="entero" and der.tipo == "decimal":
                    num=int(izq.valor)/float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'var','0','1')

                elif izq.tipo=="decimal" and der.tipo == "decimal":
                    num=float(izq.valor)/float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'var','0','1')
            except ZeroDivisionError:
                print(' ')# aqui se regresa el error en nodo
        elif op == 'residuo':   
            try:
              
                if izq.tipo=="entero" and der.tipo == "entero": 
                    num=int(izq.valor)%int(der.valor)
                    result=Simbolo('nada','entero',str(num),'var','0','1')

                elif izq.tipo=="decimal" and der.tipo == "entero":
                    num=float(izq.valor)%int(der.valor)
                    result=Simbolo('nada','decimal',str(num),'var','0','1')

                elif izq.tipo=="entero" and der.tipo == "decimal":
                    num=int(izq.valor)%float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'var','0','1')

                elif izq.tipo=="decimal" and der.tipo == "decimal":
                    num=float(izq.valor)%float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'var','0','1')
            except ZeroDivisionError:
                print(' ')# aqui se regresa el error en nodo      
        return result
 #-----------------------------------------------------------------------------EXPRESIONES RELACIONALES-------------------------   
    def acciones_exp_rel(self, Raiz):
        result=None
        if Raiz.produccion=='exp_rel':
            izq = Raiz.hijos[0] # seria el valor de el lado izq
            op  = Raiz.hijos[1] # seria el operador >, <, >=, <=, !=
            der = Raiz.hijos[2] # seria el valor derecho
            izq=self.acciones_exp_rel(izq) # ya tengo el valor del hijo izq
            der=self.acciones_exp_rel(der) # ya tengo el valor del hijo der
            result=self.operaciones_relacionales(izq,der,op.produccion) # me regresa el objeto de tipo simbolo

        elif Raiz.produccion == 'entero':
            result = Simbolo('numero','entero',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'cadena':
            result = Simbolo('cadena','cadena',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'decimal':
            result = Simbolo('decimal','decimal',str(Raiz.valor),'var','1','0')
        
        elif Raiz.produccion == 'valorIMP':
            result = self.acciones_exp_num(Raiz.hijos[0])
        elif Raiz.produccion == 'variable':
            if len(Raiz.hijos)==1:
                # acceso a un avariable
                izq=Raiz.hijos[0]
                result=self.acciones_exp_num(izq)

            else:
                #acceso a un vector
                a=""
        elif Raiz.produccion=='var':
            # busco el simbolo en la tabla de simbolos
            nombre=Raiz.valor #obtengo el nombre de la variable
            result=self.tabla_simbolos.get_symbol(nombre)
        return result   
    def operaciones_relacionales(self,izq,der,op):
        result=None
        num = 0
        if op == 'mayorque':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor)>int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor)>float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)>int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)>float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor>int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor>float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor>der.valor
                
        elif op == 'menorque':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor)<int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor)<float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)<int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)<float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor<int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor<float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor<der.valor

        elif op == 'igualque':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor)==int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor)==float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)==int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)==float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor==int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor==float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor==der.valor

        elif op == 'noigual':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor)!=int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor)!=float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)!=int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)!=float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor!=int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor!=float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor!=der.valor

        elif op == 'menorigualque':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor)<=int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor)<=float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)<=int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)<=float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor<=int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor<=float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor<=der.valor

        if op == 'mayorigualque':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor)>=int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor)>=float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)>=int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)>=float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor>=int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor>=float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor>=der.valor
                
               
        if num == True: num=1
        else:           num=0
        result=Simbolo('nada','bool',str(num),'var','0','1')        
        return result
 #-----------------------------------------------------------------------------EXPRESIONES logicas----------------------------
    def acciones_exp_log(self, Raiz):
        result=None
        if Raiz.produccion=='exp_log':
            izq = Raiz.hijos[0] # seria el valor de el lado izq
            op  = Raiz.hijos[1] # seria el operador >, <, >=, <=, !=
            der = Raiz.hijos[2] # seria el valor derecho
            izq=self.acciones_exp_log(izq) # ya tengo el valor del hijo izq
            der=self.acciones_exp_log(der) # ya tengo el valor del hijo der
            result=self.operaciones_logicas(izq,der,op.produccion) # me regresa el objeto de tipo simbolo

        elif Raiz.produccion == 'entero':
            result = Simbolo('numero','entero',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'cadena':
            result = Simbolo('cadena','cadena',str(Raiz.valor),'var','1','0')
        elif Raiz.produccion == 'decimal':
            result = Simbolo('decimal','decimal',str(Raiz.valor),'var','1','0')
        

        elif Raiz.produccion == 'variable':
            if len(Raiz.hijos)==1:
                # acceso a un avariable
                izq=Raiz.hijos[0]
                result=self.acciones_exp_num(izq)

            else:
                #acceso a un vector
                a=""
        elif Raiz.produccion=='var':
            # busco el simbolo en la tabla de simbolos
            nombre=Raiz.valor #obtengo el nombre de la variable
            result=self.tabla_simbolos.get_symbol(nombre)
        return result      
    
    def operaciones_logicas(self, izq,der,op):
        result=None
        num = 0
        if op == 'and':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor) and int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor) and float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor) and int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor) and float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor and int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor and float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor and der.valor
                
        elif op == 'or':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor) or int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor) or float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor) or int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor) or float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor or int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor or float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor or der.valor

        elif op == 'xor':
            if izq.tipo=="entero" and der.tipo == "entero":     num=int(izq.valor) ^ int(der.valor)
            elif izq.tipo=="entero" and der.tipo == "decimal":  num=int(izq.valor) ^ float(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "entero":  num=float(izq.valor)^int(der.valor)
            elif izq.tipo=="decimal" and der.tipo == "decimal": num=float(izq.valor)^float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "entero":   num=izq.valor^int(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "decimal":  num=izq.valor^float(der.valor)
            elif izq.tipo=="cadena" and der.tipo == "cadena":   num=izq.valor^der.valor

        if num == True: num=1
        else:           num=0
        result=Simbolo('nada','bool',str(num),'var','0','1')        
        return result
 #-----------------------------------------------------------------------------CONVERSION DE VALORES---------------------
    def acciones_conversion(self, Raiz):
        result=None
        if Raiz.produccion=='conversion':
            izq = Raiz.hijos[0].produccion # seria tipo a convertir
            if izq=='int':
                if Raiz.hijos[1].produccion == 'var':
                    # busco el simbolo en la tabla de simbolos
                    nombre=Raiz.hijos[1].valor #obtengo el nombre de la variable
                    result=self.tabla_simbolos.get_symbol(nombre)
                    if result.tipo == 'decimal':
                        result.valor=str(int(float(result.valor)))
                        result.tipo = 'entero'
                        return result
                    elif result.tipo == 'cadena':
                        if len(result.valor)==1:
                            result.valor=str(ord(result.valor))
                            result.tipo = 'entero'
                            return result
                        else:
                            result.valor=str(ord(result.valor[0]))
                            result.tipo = 'entero'
                            return result
                    elif result.tipo == 'vector':
                        print('conversion vector a entero solo el primer elemento')
                else:
                    return result
            elif izq == 'float':
                if Raiz.hijos[1].produccion == 'var':
                    # busco el simbolo en la tabla de simbolos
                    nombre=Raiz.hijos[1].valor #obtengo el nombre de la variable
                    result=self.tabla_simbolos.get_symbol(nombre)
                    if result.tipo == 'entero':
                        result.valor=str(float(int(result.valor)))
                        result.tipo = 'decimal'
                        return result
                    elif result.tipo == 'cadena':
                        if len(result.valor)==1:
                            result.valor=str(float(ord(result.valor)))
                            result.tipo = 'decimal'
                            return result
                        else:
                            result.valor=str(float(ord(result.valor[0])))
                            result.tipo = 'decimal'
                            return result
                    elif result.tipo == 'vector':
                        print('conversion vector a decimal solo el primer elemento')
                else:
                    return result
            elif izq == 'char':
                if Raiz.hijos[1].produccion == 'var':
                    # busco el simbolo en la tabla de simbolos
                    nombre=Raiz.hijos[1].valor #obtengo el nombre de la variable
                    result=self.tabla_simbolos.get_symbol(nombre)
                    if result.tipo == 'entero':
                        numero=int(result.valor)
                        if(numero>=0 and numero <=255):
                            result.valor= chr(numero)
                        else:
                            result.valor = chr((numero%256))
                        result.tipo = 'cadena'
                        return result
                    elif result.tipo == 'decimal':
                        numero=int(result.valor)
                        if(numero>=0 and numero <=255):
                            result.valor= chr(numero)
                        else:
                            result.valor = chr((numero%256))
                        result.tipo = 'cadena'
                        return result
                    elif result.tipo=='cadena':
                        result.valor=result.valor[0]
                        return result
                    elif result.tipo == 'vector':
                        print('conversion vector a decimal solo el primer elemento')
                else:
                    return result
  #-----------------------------------------------------------------------------CONVERSION DE VALORES---------------------
    def acciones_array(self, Raiz,valorP):
        result = None
        if Raiz.produccion=='variable':
           
            nuevo_simbolo=self.tabla_simbolos.get_symbol(Raiz.hijos[0].valor)
            cont=0
            tabla={}
            aux ={}
            for nodo in Raiz.hijos:
                cont+=1
                #si hijos es mayor a 2 entonces la primer no se toma
                if len(Raiz.hijos)==2:
                   if nodo.produccion=='param_accesso' and cont ==2:
                        valor1=self.accion_get_param(nodo.hijos[0])
                        tabla=nuevo_simbolo.valor
                        if valor1 in tabla: 
                            aux=tabla[valor1]
                            tabla[valor1]={aux}
                            tabla[valor1].add(valorP.valor)
    
                        else:  
                            tabla[valor1]=valorP.valor
                            nuevo_simbolo.valor=tabla
  
                elif len(Raiz.hijos)==3:
                    if nodo.produccion=='param_accesso' and cont ==2:
                        valor1=self.accion_get_param(nodo.hijos[0])
                        tabla=nuevo_simbolo.valor
                        if valor1 in tabla: 
 
                            aux=tabla[valor1]
                            
                        else: 
                            print('df')
                        tabla[valor1]={}
                        nuevo_simbolo.valor=tabla
                        tabla=tabla[valor1]
                    elif nodo.produccion=='param_accesso'and cont==3:
                        valor1=self.accion_get_param(nodo.hijos[0])
                        tabla[valor1]=valorP.valor
                        tabla.update(aux)
            result =nuevo_simbolo                    
            return  result

    def accion_get_param(self,hijo):
        print('')
        return hijo.valor