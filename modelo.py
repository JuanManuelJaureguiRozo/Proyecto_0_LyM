# Proyecto 0 Lenguajes y Máquinas - Grupo 12

#Integrantes:
#   - Juan Manuel Jáuregui Rozo - 201922481
#   - Adrián Arturo Suarez García - 202123771

#import consola as consola

# -------------------------------------
# Listas de palabras reservadas
# -------------------------------------

# Listas métodos
lista_noms_metodos = ["jump", "walk", "leap", "turn", "turnto",
                      "drop", "get", "grab", "letgo", "nop"]

lista_noms_proc = []

#Listas condicionales   
lista_condicionales = ["if", "while", "repeat"]

lista_condiciones =["facing", "can", "not"]

# Listas Parámetros
lista_parametros_str = ["north", "south", "east", "west",
                    "left", "right", "around", "front", "back"]

lista_parametros_turn1 = ["left", "right", "around"]

lista_parametros_turn2 = ["north", "south", "east", "west"]

lista_param_dir = []

lista_parametros_int = []

# -------------------------------------
# Función para limpiar las líneas
# -------------------------------------

def limpiar_linea(line):

    line = line.lower()
    line = line.rstrip("\n")
    line = line.lstrip()

    line = line.replace("(", ",(,")
    line = line.replace(")", ",),")
    line = line.replace("{", ",{,")
    line = line.replace("}", ",},")
    line = line.replace("\t", ",")
    line = line.replace(" ", ",")
    
    line = line.split(",")

    for elemento in line:
        if elemento == "":
            line.remove(elemento)
        elif elemento == " ":
            line.remove(elemento)

    for elemento in line:
        if elemento == "":
            line.remove(elemento)
        elif elemento == " ":
            line.remove(elemento)

    if line[0] == "defvar":
        line[0] = "defVar"
        
    elif line[0] == "defproc":
        line[0] = "defProc"

    return line

# -------------------------------------
# Funciones para examinar líneas
# -------------------------------------

def test_Var(linea): 
    if len(linea) == 3:     
        if (linea[0] == "defVar") and (type(linea[1]) == str) and (type(linea[2]) == str):  
            try:
                entero = int(linea[2])   
                if linea[1] not in lista_parametros_int:   
                    lista_parametros_int.append(linea[1])   
                    return(True)
                
            except: 
                if linea[2] in lista_parametros_str:         
                        return True
                
                else: return False
        
        else: return False
    
    else: return False

def almacenar_parametros(linea):

    if (linea[0] == "defProc") and (type(linea[1]) == str) and (linea[2] == "("):
        ultimo_parentesis = linea.index(")")
        lista_parametros = linea[3:ultimo_parentesis]
        return lista_parametros
    
    elif (linea[0] in lista_noms_proc) and (linea[1] == "("):
        ultimo_parentesis = linea.index(")")
        lista_parametros = linea[2:ultimo_parentesis]
        return lista_parametros
     
    elif (linea[0] in lista_noms_metodos) and (linea[1] == "("):
        ultimo_parentesis = linea.index(")")
        lista_parametros = linea[2:ultimo_parentesis]
        return lista_parametros
    
def test_Proc(linea, lista_parametros):

    if (linea[0] == "defProc") and (type(linea[1]) == str) and (linea[2] == "("):
        tam = len(lista_parametros)
        for i in lista_parametros:
            if i == linea[3+lista_parametros.index(i)]:
                if linea[3+tam] == ")":
                    if linea[1] not in lista_noms_proc:
                        lista_noms_proc.append(linea[1])
                        return True
                    
        if lista_parametros == []:
            if linea[3] == ")":
                if linea[1] not in lista_noms_proc:
                    lista_noms_proc.append(linea[1])
                    return True
                    
    elif (linea[0] in lista_noms_proc) and (linea[1] == "("):
        tam = len(lista_parametros)
        for i in lista_parametros:
            if i == linea[2+lista_parametros.index(i)]:
                if linea[2+tam] == ")":
                    return True
    
    else: return False

def test_corchete(linea):
    
    if ((linea[0] == "{") and (len(linea) == 1)) or ((linea[0] == "}") and (len(linea) == 1)):
        return True
    else: 
        return False

    
def test_metodo(l, matriz, index, parametros):
    met = l[0]
    
    if met == "jump":  
        
        try:
            if ((l[2] in parametros) and (l[3] in parametros)):
                if (l[1] == "(") and (l[4] == ")"):
                    if (l[5] == ";"):
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
                        
            elif (l[2] not in parametros) and (l[3] not in parametros):
                entero1 = int(l[2])
                entero2 = int(l[3])
                
                if (l[1] == "(") and (type(entero1) == int) and (type(entero2) == int) and (l[4] == ")"):
                    if (l[5] == ";"):     
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
            
            else: return False

        except: return False
    
    elif met == "walk":
        try: 
            if ((l[2] in parametros)):
                if (l[1] == "(") and (l[3] == ")"):
                    if (l[4] == ";"):
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
                        
            elif (l[2] not in parametros):           
                entero = int(l[2])
                
                if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):          
                    if (l[4] == ";"):                 
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
            
            if (l[2] in parametros):
                if (l[1] =="(") and (l[3] in lista_parametros_str) and l[4] == ")":
                    if (l[5] == ";"):     
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
                        
            elif (l[2] not in parametros):
                entero = int(l[2])
                if (l[1] == "(") and (type(entero) == int) and (l[3] in lista_parametros_str) and (l[4] == ")"):          
                    if (l[5] == ";"):                 
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
            
            else: return False
        
        except: 
            return False
        
    elif met == "leap":
        try: 
            if (l[2] in parametros):
                if (l[1] == "(") and (l[3] == ")"):
                    if  (l[4] == ";"):
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False 

            elif (l[2] not in parametros):
                entero = int(l[2])

                if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                    if  (l[4] == ";"):
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
            
            if (l[2] in parametros):
                if (l[1] == "(") and (l[3] in lista_parametros_str) and (l[4] == ")"):
                    if  (l[5] == ";"):
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
                        
            elif (l[2] not in parametros):
                entero = int(l[2])
                if (l[1] == "(") and (type(entero) == int) and (l[3] in lista_parametros_str) and (l[4] == ")"):
                    if  (l[5] == ";"):
                        linea_siguiente = matriz[index + 1]
                        if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                            return False
                        return True
                    
                    else:
                        linea_sig = matriz[index + 1]
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return False
            
            else: return False

        except: return False
        
    elif met == "turn":
        if (l[1] == "(") and (l[2] in lista_parametros_turn1) and (l[3] == ")"):
                if (l[4] == ";"):
                    linea_siguiente = matriz[index + 1]
                    if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                        return False
                    return True
                
                else:
                    linea_sig = matriz[index + 1]
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return False
                
        else:return False
        
    elif met == "turnto":
        if (l[1] == "(") and (l[2] in lista_parametros_turn2) and (l[3] == ")"):
                if (l[4] == ";"):
                    linea_siguiente = matriz[index + 1]
                    if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                        return False
                    return True
                
                else:
                    linea_sig = matriz[index + 1]
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return False
        
        else: return False
        
    elif met == "drop":
        try:
            if (l[2] in parametros):
                if (l[1] == "(") and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False

            elif (l[2] not in parametros):
                entero = int(l[2])
                
                if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False
                            
            else: return False
        
        except: return False
    
    elif met == "get":
        try: 
            if (l[2] in parametros):
                if (l[1] == "(") and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False

            elif (l[2] not in parametros):
                entero = int(l[2])
                
                if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False
                            
            else: return False
        
        except: return False
            
    elif met == "grab":
        try: 
            if (l[2] in parametros):
                if (l[1] == "(") and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False

            elif (l[2] not in parametros):
                entero = int(l[2])
                
                if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False
                            
            else: return False
        
        except: return False
        
    elif met == "letgo":
        try: 
            if (l[2] in parametros):
                if (l[1] == "(") and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False

            elif (l[2] not in parametros):
                entero = int(l[2])
                
                if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                        if (l[4] == ";"):
                            linea_siguiente = matriz[index + 1]
                            if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                                return False
                            return True
                        
                        else:
                            linea_sig = matriz[index + 1]
                            if (linea_sig[0] == "}") and len(linea_sig) == 1:
                                return False
                            
            else: return False
        
        except: return False   
    
    elif met == "nop":
        if (l[1] == "(") and (l[2] == ")"):
            if (l[3] == ";"):
                linea_siguiente = matriz[index + 1]
                if (len(linea_siguiente) == 1 and linea_siguiente[0] == "}"):
                    return False
                return True
            
            else:
                linea_sig = matriz[index + 1]
                if (linea_sig[0] == "}") and len(linea_sig) == 1:
                    return False
        
    else: return False
    
def partir (lim1, lim2, linea):
    
    lil = []
    i = 0
    while i < (lim2-lim1):
            lil.append(linea[lim1])
            linea.pop(lim1)
            i += 1
    linea.pop(lim1)
    lil.pop(0)
    lil.append(";")
    
    return lil, linea

def test_condicionales (l, matriz, index):
    
    #lista_condicionales = ["if", "else", "while", "repeat"]
    #lista_condiciones =["facing", "can", "not"]

    if l[0] == "if":
        if (l[1] in lista_condiciones):
            
            if l[1] == "facing":
                try:
                    
                    if (l[2] == "(") and (l[3] in lista_parametros_turn2) and (l[4] == ")"):
                        if (l[5] == "{") and (l[6] in lista_noms_metodos):
                            
                            lim1 = 5
                            lim2 = l.index("}")
                            
                            h = partir(lim1,lim2,l)
                            lil = h[0] #aquello dentro de paréntesis que toca verificar
                            l = h[1]   #la lista sin lo de dentro del paréntesis
                            
                            if (lil[0] in lista_noms_metodos) or (lil[0] in lista_noms_proc):
                                if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[5] == "else") and (l[6] == "{"):
                                    limi1 = 6
                                    limi2 = l.index("}")
                                    
                                    h = partir(limi1,limi2,l)
                                    lil = h[0] #aquello dentro de paréntesis que toca verificar
                                    l = h[1]   #la lista sin lo de dentro del paréntesis
                                    if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] == ";"):
                                        return True
                                    elif (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] != ";"):
                                        lineaa = (matriz[index+1])
                                        if (lineaa[0] == "}") and (len(lineaa) == 1):
                                            return True
                                        else: return False
                    
                        elif (l[5] == "{") and (l[6] in lista_condicionales):
                            
                            l.reverse()
                            index_alreves = l.index("else")
                            l.reverse()
                            index_alderecho = len(l) - (index_alreves + 2)
                            
                            lim1 = 5
                            lim2 = index_alderecho
                            
                            h = partir(lim1,lim2,l)
                            
                            lil = h[0] #aquello dentro de paréntesis que toca verificar
                            lil.pop(-1)
                            l = h[1]
                            lil.append(";")

                            if (test_condicionales(lil, matriz, index) == True) and (l[5] == "else") and (l[6] == "{"):
                                limi1 = 6
                                limi2 = l.index("}")
                                
                                h = partir(limi1,limi2,l)
                                lil = h[0] #aquello dentro de paréntesis que toca verificar
                                l = h[1]   #la lista sin lo de dentro del paréntesis
                                if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] == ";"):
                                    return True
                                elif (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] != ";"):
                                    lineaa = (matriz[index+1])
                                    if (lineaa[0] == "}") and (len(lineaa) == 1):
                                        return True
                                    else: return False
                                else: return False
                            else: return False
                        else: return False
                    else: return False
                               
                except: return False 
                
            elif l[1] == "can":
                try:
                    
                    if (l[2] == "(") and (l[3] in (lista_noms_metodos or lista_noms_proc)):
                        
                        lim1 = 2
                        lim2 = l.index(")") +1
                        h = partir(lim1,lim2,l)
                        lil = h[0] #aquello dentro de paréntesis del can
                        l = h[1]   #la lista sin lo de dentro del paréntesis
                        
                        if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[3] == "{"): #l[2]?
                            limi1 = 3
                            limi2 = l.index("}")
                            
                            h = partir(limi1,limi2,l)
                            lili = h[0] # el bloque que ejecuta can
                            l = h[1]   #la lista sin lo de dentro del paréntesis
                            
                            if (test_metodo(lili,matriz,index,almacenar_parametros(lili)) == True) and (l[3] == "else") and (l[4] == "{"):
                                limimi1 = 3
                                limimi2 = l.index("}")
                                
                                h = partir(limimi1,limimi2,l)
                                lilili = h[0] #el bloque que ejecuta else
                                l = h[1]   #la lista sin lo de dentro del paréntesis
                                
                                if (test_metodo(lilili,matriz,index,almacenar_parametros(lilili)) == True) and (l[-1] == ";"):
                                    return True
                                elif (test_metodo(lilili,matriz,index,almacenar_parametros(lilili)) == True) and (l[-1] != ";"):
                                        lineaa = matriz[index+1]
                                        if (lineaa[0] == "}") and (len(lineaa) == 1):
                                            return True
                                        else: return False
                                else: return False
                            else: return False
                        else: return False
                    
                    elif lil[0] in lista_condicionales:
                                return True      
                    else: return False 
                except: return False 
            
            elif l[1] == "not":
                for elemento in l:
                    if elemento == "not":
                        l.remove("elemento")
                marca = test_condicionales(l,matriz,index)
                if marca == True:
                    return True
                else: return False
            else: return False
                
        else: return False
            
        
    elif l[0] == "while":
        if l[1] in lista_condiciones:
            
            if l[1] == "facing":
                try:
    
                    if (l[2] == "(") and (l[3] in lista_parametros_turn2) and (l[4] == ")"):
                        if (l[5] == "{") and len(l) > 6:
                            
                            lim1 = 5
                            lim2 = l.index("}")
                            
                            h = partir(lim1,lim2,l)
                            lil = h[0] #aquello dentro de paréntesis que toca verificar
                            l = h[1]   #la lista sin lo de dentro del paréntesis
                            if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] == ";"):
                                
                                return True
                        elif (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] != ";"):
                            lineaa = (matriz[index+1])
                            if (lineaa[0] == "}") and (len(lineaa) == 1):
                                return True
                            
                        elif (l[5] == "{") and len(l) == 6:
                            centinela = False
                            num_linea = index + 1
                            while centinela == False:

                                if matriz[num_linea][0] != "}":
                                    resultado = funcion_consola(matriz[num_linea], matriz, num_linea)
                                    if resultado == True:
                                        num_linea += 1
                                        pass

                                    elif resultado == False:
                                        centinela = True
                                        return False
                                    
                                else: centinela = True

                            return True
                        else: return False
                    else: return False
                            
                except: return False
            
            elif l[1] == "can":
                try:
                    
                    if (l[2] == "(") and (l[3] in (lista_noms_metodos or lista_noms_proc)):
                        
                        lim1 = 2
                        lim2 = l.index(")") +1
                        h = partir(lim1,lim2,l)
                        lil = h[0] #aquello dentro de paréntesis del can
                        l = h[1]   #la lista sin lo de dentro del paréntesis
                        
                        if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[2] == "{"):
                            limi1 = 2
                            limi2 = l.index("}")
                            h = partir(limi1,limi2,l)
                            lili = h[0] # el bloque que ejecuta can
                            l = h[1]   #la lista sin lo de dentro del paréntesis
                            
                            if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[2] == ";"):
                                return True
                            elif (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[2] != ";"):
                                lineaa = (matriz[index+1])
                                if (lineaa[0] == "}") and (len(lineaa) == 1):
                                    return True
                            
                        elif (l[2] == "{") and len(l) == 6:
                            centinela = False
                            num_linea = index + 1
                            while centinela == False:

                                if matriz[num_linea][0] != "}":
                                    resultado = consola.funcion_consola(matriz[num_linea], matriz, num_linea)
                                    if resultado == True:
                                        num_linea += 1
                                        pass

                                    elif resultado == False:
                                        centinela = True
                                        return False
                                    
                                else: centinela = True

                            return True
                        else: return False
                    else: return False
                
                except: return False 

            elif l[1] == "not":
                for elemento in l:
                    if elemento == "not":
                        l.remove("elemento")
                marca = test_condicionales(l,matriz,index)
                if marca == True:
                    return True
                else: return False
            else: return False

    elif l[0] == "repeat":
        if type(l[1]) == int:
            if (l[2] == "times"):
                if (l[3] == "{") and len(l) > 4:
                    lim1 = 3
                    lim2 = l.index("}")
                    
                    h = partir(lim1,lim2,l)
                    lil = h[0]
                    l = h[1]

                    if (test_metodo(lil,matriz,index,almacenar_parametros(lil)) == True) and (l[-1] == ";"):
                        return True
                    
                elif (l[3] == "{") and len(l) == 4:
                    centinela = False
                    num_linea = index + 1
                    while centinela == False:

                        if matriz[num_linea][0] != "}":
                            resultado = consola.funcion_consola(matriz[num_linea], matriz, num_linea)
                            if resultado == True:
                                num_linea += 1
                                pass

                            elif resultado == False:
                                centinela = True
                                return False
                            
                        else: centinela = True

                    return True

    else: return False
    
    