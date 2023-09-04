# Proyecto 0 Lenguajes y Máquinas - Grupo 12

#Integrantes:
#   - Juan Manuel Jáuregui Rozo - 201922481
#   - Adrián Arturo Suarez García - 202123771

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
lista_parametros_str = ["north", "south", "east", "west", "n","s","e","w",
                    "left", "right", "around", "front", "back"]

lista_parametros_turn1 = ["left", "right", "around"]

lista_parametros_turn2 = ["north", "south", "east", "west", "n","s","e","w"]

lista_param_dir = []

lista_parametros_int = []

# -------------------------------------
# Función para limpiar las líneas
# -------------------------------------

def limpiar_linea(line):

    line = line.lower()
    line = line.rstrip("\n")

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
        if (type(linea[0]) == "defVar") and (type(linea[1]) == str) and (type(linea[2]) == (str or int)):
                    
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
     
def test_Proc(linea, lista_parametros):

    if (linea[0] == "defProc") and (type(linea[1]) == str) and (linea[2] == "("):
        tam = len(lista_parametros)
        for i in lista_parametros:
            if i == linea[3+lista_parametros.index(i)]:
                if linea[3+tam] == ")":
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

    
def test_metodo(l, matriz, index):

    met = l[0]
    
    if met == "jump":  

        try:
            entero1 = int(l[2])
            entero2 = int(l[3])
            
            if (l[1] == "(") and (type(entero1) == int) and (type(entero2) == int) and (l[4] == ")"):
                if (l[5] == ";"):         
                    return True
                else:
                    linea_sig = matriz(index) + 1
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return True
            
            else: return False

        except: return False
    
    elif met == "walk":

        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):    
                        
                if (l[4] == ";"):                    
                    return True
            
                
            elif (l[1] =="(") and (type(entero) == int) and (l[3] in lista_parametros_str) and l[4] == ")" and (l[5] == ";"):       
                print("av")        
                return True
            
            else: return False
        
        except: 
            return False
        
    elif met == "leap":
        try: 
            entero = int(l[2])

            if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                if  (l[4] == ";"):
                    return True
                
                else:
                    linea_sig = matriz(index) + 1
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return True
            
            elif (l[1] == "(") and (type(entero) == int) and (l[3] in lista_parametros_str) and (l[4] == ")"):
                if  (l[5] == ";"):
                    return True
                
                else:
                    linea_sig = matriz(index) + 1
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return True
                    
        except: return False
        
    elif met == "turn":
        if (l[1] == "(") and (l[2] in lista_parametros_turn1) and (l[3] == ")"):
                if (l[4] == ";"):
                    return True
                
                else:
                    linea_sig = matriz(index) + 1
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return True
                
        else:return False
        
    elif met == "turnto":
        if (l[1] == "(") and (l[2] in lista_parametros_turn2) and (l[3] == ")"):
                if (l[4] == ";"):
                    return True

                else:
                    linea_sig = matriz(index) + 1
                    if (linea_sig[0] == "}") and len(linea_sig) == 1:
                        return True
        
        else: return False
        
    elif met == "drop":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                    if (l[4] == ";"):
                        return True
                    
                    else:
                        linea_sig = matriz(index) + 1
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return True
        
        except: return False
    
    elif met == "get":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                    if (l[4] == ";"):
                        return True
                    
                    else:
                        linea_sig = matriz(index) + 1
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return True
        
        except: return False
            
    elif met == "grab":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                    if (l[4] == ";"):
                        return True
                    
                    else:
                        linea_sig = matriz(index) + 1
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return True
        
        except: return False
        
    elif met == "letgo":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int) and (l[3] == ")"):
                    if (l[4] == ";"):
                        return True
                    
                    else:
                        linea_sig = matriz(index) + 1
                        if (linea_sig[0] == "}") and len(linea_sig) == 1:
                            return True
        
        except: return False   
    
    elif met == "nop":
        if (l[1] == "(") and (l[2] == ")"):
            if (l[3] == ";"):
                return True
        
            else:
                linea_sig = matriz(index) + 1
                if (linea_sig[0] == "}") and len(linea_sig) == 1:
                    return True
        
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
                        if (l[5] == "{") :
                            
                            lim1 = 5
                            lim2 = l.index("}")
                            
                            h = partir(lim1,lim2,l)
                            lil = h[0] #aquello dentro de paréntesis que toca verificar
                            l = h[1]   #la lista sin lo de dentro del paréntesis
                            
                            if (lil[0] in lista_noms_metodos) or (lil[0] in lista_noms_proc):
                                if (test_metodo(lil) == True) and (l[5] == "else") and (l[6] == "{"):
                                    limi1 = 6
                                    limi2 = l.index("}")
                                    
                                    h = partir(limi1,limi2,l)
                                    lil = h[0] #aquello dentro de paréntesis que toca verificar
                                    l = h[1]   #la lista sin lo de dentro del paréntesis
                                    if (test_metodo(lil) == True) and (l[-1] == ";"):
                                        return True
                                    elif (test_metodo(lil) == True) and (l[-1] != ";"):
                                        lineaa = limpiar_linea(matriz[index+1])
                                        if (lineaa[0] == "}") and (len(lineaa) == 1):
                                            return True
                                        else: return False
                    
                            elif lil[0] in lista_condicionales:
                                        print("me corchó")
                                        return True       
                except: return False 
            
            #[ 'if','can','(','walk','(','1','west',')',')','{','walk','(','1','west',')','}','else','{','nop','(',')','}' ]
            #[ 'if','can','{','walk','(','1','west',')','}','else','nop','(',')' ]
            #[ 'if','can','else','nop','(',')' ]
                
            elif l[1] == "can":
                try:
                    
                    if (l[2] == "(") and (l[3] in (lista_noms_metodos or lista_noms_proc)):
                        
                        lim1 = 2
                        lim2 = l.index(")") +1
                        h = partir(lim1,lim2,l)
                        lil = h[0] #aquello dentro de paréntesis del can
                        l = h[1]   #la lista sin lo de dentro del paréntesis
                        
                        if (test_metodo(lil) == True) and (l[3] == "{"):
                            limi1 = 3
                            limi2 = l.index("}")
                            
                            h = partir(limi1,limi2,l)
                            lili = h[0] # el bloque que ejecuta can
                            l = h[1]   #la lista sin lo de dentro del paréntesis
                            
                            if (test_metodo(lili) == True) and (l[3] == "else") and (l[4] == "{"):
                                limimi1 = 3
                                limimi2 = l.index("}")
                                
                                h = partir(limimi1,limimi2,l)
                                lilili = h[0] #el bloque que ejecuta else
                                l = h[1]   #la lista sin lo de dentro del paréntesis
                                
                                if (test_metodo(lilili) == True) and (l[-1] == ";"):
                                    return True
                                elif (test_metodo(lilili) == True) and (l[-1] != ";"):
                                        lineaa = matriz[index+1]
                                        if (lineaa[0] == "}") and (len(lineaa) == 1):
                                            return True
                                        else: return False
            
                    elif lil[0] in lista_condicionales:
                                print("me corchó")
                                return True       
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
            
        
    elif l[0] == "while":
        if l[1] in lista_condiciones:
            
            if l[1] == "facing":
                try:
    
                    if (l[2] == "(") and (l[3] in lista_parametros_turn2) and (l[4] == ")"):
                        if (l[5] == "{") :
                            print(1)
                except: return False

            
            elif l[1] == "can":
                return True
                    
            elif l[1] == "not":
                return True
        
    elif l[0] == "repeat":
        if type(l[1]) == int:
            if (l[2] == "times"):
                nl = l[3:]
                if test_block(nl) == True:
                    return True    

    else: return False