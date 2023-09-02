# Proyecto 0 Lenguajes y Máquinas - Grupo 12

#Integrantes:
#   - Juan Manuel Jáuregui Rozo - 201922481
#   - Adrián Arturo Suarez García - 202123771

# -------------------------------------
# Función para limpiar las líneas
# -------------------------------------

def limpiar_linea(line):

    line = line.lower()

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

"""
LISTA DE DUDAS QUE VAN SURGIENDO 
- ¿Todos los archivos deben empezar con defProc?
- ¿Puedo definir una variable que NO puedo usar? tipo, un str que no puedo meter en ninguna variable
- Al principio dice que se pueden designar variables como en python, tipo "hola = 10"; se puede?
    - En tal caso toca hacer otro caso inicial como variante de defVar
- ¿Hay casos de #'s negativos?
- Cuantos parámetros se pueden tener en un método? ¿Siempre menos 2?

LISTA PROBLEMAS / DETALLES QUE FALTAN POR IMPLEMENTAR
- Seguramente toque separar los métodos normales, los nuevos, y los condicionales, haciendo una nueva función para verificar los condicionales
    - Puede hacerse agregando un 5to caso, o con un if dentro del verificador de métodos; seguramente 1era opción
- La última línea de un bloque NO tiene ";" lo cual será un problema.
    - Tal vez verificando que la siguiente línea sea "}" se pueda saltar este caso
    - Podemos crear un diccionario de booleanos, c/u es un centinela, así podemos verificar cosas de +1 línea
- Para los "{}" mejor hacer una pila simple; en una lista previamente declarada se van agregando los "{", y cada que salga un 
"}" se va eliminando la -1 posición con una función, la cual preguna el len de la lista. Si es <0 se devuelve True y el programa
sigue, sino se para, y al final del todo se pregunta el tamaño de la lista, si no es =0, está mal y el txt es incorrecto

- "if" "else" siempre están en la misma línea?
    - Asumí que si
"""

"""
FALTA:
1. Contador o lista para los corchetes. (A) HECHO
    - falta meterle los de los condionales
2. Verificar condiciones while, if, repeat. (P)
3. Definir solución para variables tipo python. (P)
4. Definir solución para los ; de los métodos. (P)
5. Definir solución para facing, can y not. (J)
"""

# -------------------------------------
# Listas de palabras reservadas
# -------------------------------------

lista_noms_metodos = ["jump", "walk", "leap", "turn", "turnto",
                      "drop", "grab", "letGo", "nop"]

lista_noms_proc = []

            #Listas condicionales   
lista_condicionales = ["if", "else", "while", "repeat"]

lista_condiciones =["facing", "can", "not"]


            # Listas Parámetros
lista_parametros_str = ["north", "south", "east", "west", "n", "s", "e", "w",
                    "left", "right", "around", "front", "back"]

lista_parametros_turn1 = ["left", "right", "around"]

lista_parametros_turn2 = ["north", "south", "east", "west", "n", "s", "e", "w"]

lista_param_dir = []

lista_parametros_int = []

# -------------------------------------
# Funciones para examinar líneas
# -------------------------------------

def test_Var (linea): 

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
    
     
def test_Proc (linea):

    if (linea[0] == "defProc") and (type(linea[1]) == str) and (linea[2] == "(") and (type(linea[3]) == (str or int)) and (type(linea[4]) == (str or int)) and (linea[5] == ")"):
        
        if linea[1] not in lista_noms_proc:
            lista_noms_proc.append(linea[1])
        return True
        
    elif (linea[0] == "defProc") and (type(linea[1]) == str) and (linea[2] == "(") and (type(linea[3]) == (str or int)) and (linea[4] == ")"):
        if linea[1] not in lista_noms_proc:
            lista_noms_proc.append(linea[1])
        return True
        
    elif (linea[0] == "defProc") and (type(linea[1]) == str) and (linea[2] == "(") and (linea[3] == ")"):
        if linea[1] not in lista_noms_proc:
            lista_noms_proc.append(linea[1])
        return True
    
    else: return False
    

def test_corchete(linea):
    
    if ((linea[0] == "{") and (len(linea) == 1)) or ((linea[0] == "}") and (len(linea) == 1)):
        return True
    else: 
        return False

    
def test_metodo (l):

    met = l[0]
    
    if met == "jump":  

        try:
            entero1 = int(l[2])
            entero2 = int(l[3])
            
            if (l[1] == "(") and (type(entero1) == int) and (type(entero2) == int) and (l[4] == ")") and (l[5] == ";"):         
                return True
            
            else: return False

        except: return False
    
    elif met == "walk":

        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int):                
                if (l[3] == ")") and (l[4] == ";"):                    
                    return True
                
            elif (l[1] =="(") and (l[3] in lista_parametros_str):               
                if l[4] == ")" and (l[5] == ";"):                   
                    return True
            
            else: return False
        
        except: return False
        
    elif met == "leap":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int):
                if (l[3] == ")") and (l[4] == ";"):
                    return True
                
            elif (l[1] =="(") and (l[3] in lista_parametros_str):
                if l[4] == ")" and (l[5] == ";"):
                    return True
            
        except: return False
        
    elif met == "turn":
        if (l[1] == "(") and (l[2] in lista_parametros_turn1):
                if (l[3] == ")") and (l[4] == ";"):
                    return True
                else: return False
                
        else:return False
        
    elif met == "turnto":
        if (l[1] == "(") and (l[2] in lista_parametros_turn2):
                if (l[3] == ")") and (l[4] == ";"):
                    return True
                else: return False
        
        else: return False
        
    elif met == "drop":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False
    
    elif met == "get":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False
            
    elif met == "grab":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False
        
    elif met == "letGo":
        try: 
            entero = int(l[2])
            
            if (l[1] == "(") and (type(entero) == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False   
    
    elif met == "nop":
        if (l[1] == "(") and (l[2] == ")") and (l[3] == ";"):
            return True
        
        else: return False

    elif met in lista_noms_proc:
        if (l[1] == "(") and (l[2] == ")") and (l[3] == ";"):
            return True
        
        elif (l[1] == "(") and (type(l[2]) == (str or int)) and (l[3] == ")") and (l[4] == ";"):
            return True
        
        elif (l[1] == "(") and (type(l[2]) == (str or int)) and (type(l[3]) == (str or int)) and (l[4] == ")") and (l[5] == ";"):
            return True

        
    else: return False
     
     
def test_condicionales (l):
    
    #lista_condicionales = ["if", "else", "while", "repeat"]

    #lista_condiciones =["facing", "can", "not"]

    if l[0] == "if":
        if (l[1] in lista_condiciones):
            
            if l[1] == "facing":
                if (l[2] == "(") and (l[3] in lista_parametros_turn2) and (l[4] == ")"):
                    if (l[5] == "{") :
                
                else: return False    
                
                # if facing(O) {} else {];
                
            elif: l[1] == "can":
            
            elif l[1] == "not":
                print("a")
        else: return False
            
        
    elif l[0] == "while":
        print(1)
        
    elif l[0] == "repeat":
        print(1)    