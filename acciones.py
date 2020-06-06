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
            # listas de hijos de prduccion lista de instancias
            for node in Raiz.hijos:
                resutl= self.acciones(node)
        elif Raiz.produccion=='asignacion':
            # tenes dos hijos
            izq=Raiz.hijos[0] #hijo izq el nombre de la variable
            der=Raiz.hijos[1] # hijo de derecho tenes expresion
            izq=self.acciones(izq) # el var y esta en tablal de simblos / objeto simbolo
            der=self.acciones(der) # obtengo el resultado del arbol exp_num y me devuelve un objeto tipo simbolo o un null si hubo un erro
            if der != None:
                # no hay un error en tiempo de ejecion
                izq.tipo=der.tipo
                izq.valor=der.valor
                self.tabla_simbolos.update_symbol(izq)
            else:
                #existe un error en tiempo de ejecucion
                self.error+="existe un error en la operacion \n"
        elif Raiz.produccion=='variable':
            if len(Raiz.hijos)==1:
                # es crear una variable simple
                izq=Raiz.hijos[0]
                resutl=self.acciones(izq)

            else:
                #pasos para accesar a un vector
                a=""
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

        elif Raiz.produccion == 'exp_num':
            resutl=self.acciones_exp_num(Raiz)

        elif Raiz.produccion == 'exp_rel':
            resutl = self.acciones_exp_rel(Raiz)

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

        return resutl
    
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
            result = Simbolo('numero','entero',str(Raiz.valor),'entero','1','0')
        elif Raiz.produccion == 'decimal':
            Raiz.valor = Raiz.valor*-1
            result = Simbolo('numero','decimal',str(Raiz.valor),'decimal','1','0')
        return result

    
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
            result = Simbolo('numero','entero',str(Raiz.valor),'entero','1','0')
        elif Raiz.produccion == 'cadena':
            result = Simbolo('cadena','cadena',str(Raiz.valor),'cadena','1','0')
        elif Raiz.produccion == 'decimal':
            result = Simbolo('decimal','decimal',str(Raiz.valor),'decimal','1','0')
        
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
                result=Simbolo('nada','entero',str(num),'entero','0','1')

            elif izq.tipo=="decimal" and der.tipo == "entero":
                num=float(izq.valor)+int(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')
            
            elif izq.tipo=="entero" and der.tipo == "decimal":
                num=float(izq.valor)+int(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

            elif izq.tipo=="decimal" and der.tipo == "decimal":
                num=float(izq.valor)+float(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

            elif izq.tipo=="cadena" and der.tipo == "cadena":
                num= izq.valor + der.valor
                result=Simbolo('nada','cadena',str(num),'cadena','0','1')

        elif op == 'resta':   
            if izq.tipo=="entero" and der.tipo == "entero": 
                num=int(izq.valor)-int(der.valor)
                result=Simbolo('nada','entero',str(num),'entero','0','1')

            elif izq.tipo=="decimal" and der.tipo == "entero":
                num=float(izq.valor)-int(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

            elif izq.tipo=="entero" and der.tipo == "decimal":
                num=int(izq.valor)-float(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1') 

            elif izq.tipo=="decimal" and der.tipo == "decimal":
                num=float(izq.valor)-float(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

        elif op == 'multi':   
            if izq.tipo=="entero" and der.tipo == "entero": 
                num=int(izq.valor)*int(der.valor)
                result=Simbolo('nada','entero',str(num),'entero','0','1')

            elif izq.tipo=="decimal" and der.tipo == "entero":
                num=float(izq.valor)*int(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

            elif izq.tipo=="entero" and der.tipo == "decimal":
                num=int(izq.valor)*float(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

            elif izq.tipo=="decimal" and der.tipo == "decimal":
                num=float(izq.valor)*float(der.valor)
                result=Simbolo('nada','decimal',str(num),'decimal','0','1')

        elif op == 'div':   
            try:
              
                if izq.tipo=="entero" and der.tipo == "entero": 
                    num=int(izq.valor)/int(der.valor)
                    result=Simbolo('nada','entero',str(num),'entero','0','1')

                elif izq.tipo=="decimal" and der.tipo == "entero":
                    num=float(izq.valor)/int(der.valor)
                    result=Simbolo('nada','decimal',str(num),'decimal','0','1')

                elif izq.tipo=="entero" and der.tipo == "decimal":
                    num=int(izq.valor)/float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'decimal','0','1')

                elif izq.tipo=="decimal" and der.tipo == "decimal":
                    num=float(izq.valor)/float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'decimal','0','1')
            except ZeroDivisionError:
                print(' ')# aqui se regresa el error en nodo
        elif op == 'residuo':   
            try:
              
                if izq.tipo=="entero" and der.tipo == "entero": 
                    num=int(izq.valor)%int(der.valor)
                    result=Simbolo('nada','entero',str(num),'entero','0','1')

                elif izq.tipo=="decimal" and der.tipo == "entero":
                    num=float(izq.valor)%int(der.valor)
                    result=Simbolo('nada','decimal',str(num),'decimal','0','1')

                elif izq.tipo=="entero" and der.tipo == "decimal":
                    num=int(izq.valor)%float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'decimal','0','1')

                elif izq.tipo=="decimal" and der.tipo == "decimal":
                    num=float(izq.valor)%float(der.valor)
                    result=Simbolo('nada','decimal',str(num),'decimal','0','1')
            except ZeroDivisionError:
                print(' ')# aqui se regresa el error en nodo      
        return result

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
            result = Simbolo('numero','entero',str(Raiz.valor),'entero','1','0')
        elif Raiz.produccion == 'cadena':
            result = Simbolo('cadena','cadena',str(Raiz.valor),'cadena','1','0')
        elif Raiz.produccion == 'decimal':
            result = Simbolo('decimal','decimal',str(Raiz.valor),'decimal','1','0')
        
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
        result=Simbolo('nada','bool',str(num),'bool','0','1')        
        return result
        