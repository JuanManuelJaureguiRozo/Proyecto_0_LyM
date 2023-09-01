# Proyecto 0 Lenguajes y Máquinas - Grupo 12

#Integrantes:
#   - Juan Manuel Jáuregui Rozo - 201922481
#   - Adrián Arturo Suarez García -  

# Lectura de archivo que se requiere verificar.
archivo = open('ejemplo.txt', 'r')

# Palabras reservadas del lenguaje.

linea = "defVar hola north"

# "linea" es la línea que se está leyendo; de momento no se ha implementado, 
# # pero se declaró para que no muestre error

def limpiar_linea(line):

    # Todo queda en minúscula
    line = line.lower()
    
    # Quita todo lo 'extra', dejando solo los strings
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

    return line

"""
LISTA DE DUDAS QUE VAN SURGIENDO 
- monitor dijo que había una línea especial con la que empezaba; no la veo en los ejemplos; omitir de momento
- Cuando lee los números en el txt, ¿los toma como str?
- ¿Siempre, después de un método, hay una "{" sola, o puede que haya código despues, tipo "{ while...."?
- ¿hay algún caso en que se definan variables después de métodos, o incluso dentro? ¿O siempre al principio?   
- ¿puedo definir una variable que NO puedo usar? tipo, un str que no puedo meter en ninguna variable
- Al principio dice que se pueden designar variables como en python, tipo "hola = 10"; se puede?
    - En tal caso toca hacer otro caso inicial como variante de defVar
- ¿Hay casos de #'s negativos?
- Cuantos parámetros se pueden tener en un método? ¿Siempre menos 2?

LISTA PROBLEMAS / DETALLES QUE FALTAN POR IMPLEMENTAR
- Seguramente toque separar los parametros str / int para poder verficar dentro de un método que sea del tipo correcto
    - Cuando se declare un nuevo parametro toca intentara volverlo int con un try/except, así sabemos si es int o no, pues
    pues todos vienen como str
- Seguramente toque separar los métodos normales, los nuevos, y los condicionales, haciendo una nueva función para verificar los condicionales
    - Puede hacerse agregando un 5to caso, o con un if dentro del verificador de métodos; seguramente 1era opción
- Falta, después del test_Var, decirle que lo agregue a la lista
- La última línea de un bloque NO tiene ";" lo cual será un problema
    - tal vez verificando que la siguiente línea sea "}" se pueda saltar este caso
    - Podemos crear un diccionario de booleanos, c/u es un centinela, así podemos verificar cosas de +1 línea
- Para los "{}" mejor hacer una pila simple; en una lista previamente declarada se van agregando los "{", y cada que salga un 
"}" se va eliminando la -1 posición con una función, la cual preguna el len de la lista. Si es <0 se devuelve True y el programa
sigue, sino se para, y al final del todo se pregunta el tamaño de la lista, si no es =0, está mal y el txt es incorrecto
- Para leer las líneas sería mejor hacer un for, donde al final se sume 1 a la línea, así podemos seguir leyendo en casos correctos
- Recordar que todo debe volverse minúscula, sobre todo en los parámetros
- Los nuevos métodos toca agregarlos de una en la lista de métodos para que haya recursión, pero ¿cómo hacemos para saber si 
los parámetros son correctos (tipo), antes de leer las líneas de abajo?
- Todos los métodos pueden terminar con o sin ";"

"""

# -------------------------------------
# Listas de palabras reservadas
# -------------------------------------

lista_noms_metodos = ["jump", "walk", "leap", "turn", "turnto",
                      "drop", "grab", "letGo", "nop"]

lista_condiciones = ["if", "else", "while", "repeat"]

lista_condicionales =["facing", "can", "not"]

lista_parametros_str = ["north", "south", "east", "west", "n", "s", "e", "w",
                    "left", "right", "around", "front", "back"]

lista_parametros_turn1 = ["left", "right", "around"]

lista_parametros_turn2 = ["north", "south", "east", "west", "n", "s", "e", "w"]

lista_param_dir = []

# Sirve para guardar nuevas variables con valores de #'s.
# Todos los #'s vienen como str, toca intentar convertirlos antes de verificarlos.
lista_parametros_int = []

# -------------------------------------
# Funciones para agregar a las listas
# -------------------------------------

def agregar_metodo ():
    return 1

def agregar_parametro ():
    return 1

# -------------------------------------
# Funciones para examinar líneas
# -------------------------------------

def test_Var (linea): 

    # linea[0] = "defVar"
    # linea[1] = nombre de la variable
    # linea[2] = valor de la variable

    if len(linea) == 3:       
        if (type(linea[0]) == "defVar") and (type(linea[1]) == str) and (type(linea[2]) == (str or int)):
                    
            try:
                entero = int(linea[2])    
                if linea[1] not in lista_parametros_int:   
                    lista_parametros_int.append(linea[1])   
                    return(True)
                
            except: 
                if linea[2] not in lista_parametros_str:         
                        return False
                
                else: return True
            # not sure; ¿será que si no está, no la necesitamos?¿es esto necesariamente bien o mal?
            
            return True
        
        else: return False
    
    else: return False
    
     
def test_Proc (linea):

    if (linea[0] == "defProc") and (linea[1] == str) and (linea[2] == "(") and (linea[3] == (str or int)) and (linea[4] == (str or int)) and (linea[5] == ")"):
        if linea[1] not in lista_noms_metodos:
            lista_noms_metodos.append(linea[1])
            return True
        
    elif (linea[0] == "defProc") and (linea[1] == str) and (linea[2] == "(") and (linea[3] == (str or int)) and (linea[4] == ")"):
        if linea[1] not in lista_noms_metodos:
            lista_noms_metodos.append(linea[1])
            return True
        
    elif (linea[0] == "defProc") and (linea[1] == str) and (linea[2] == "(") and (linea[3] == ")"):
        if linea[1] not in lista_noms_metodos:
            lista_noms_metodos.append(linea[1])
            return True
    
def test_metodo (l):

    # l es la lista; "prueba"
    # Para los parámetros int, falta agregar el caso en que estén
    # en la lista de funciones nuevas; para todos los métodos

    met = l[0]
    
    if met == "jump":       
        if (l[1] == "(") and (l[2] == int) and (l[3] == int) and (l[4] == ")") and (l[5] == ";"):           
            return True 
        
        else: return False  
    
    elif met == "walk":

        try: 
            x = int(l[2])
            
            if (l[1] == "(") and (x == int):                
                if (l[3] == ")") and (l[4] == ";"):                    
                    return True
                
            elif (l[1] =="(") and (l[3] in lista_parametros_str):               
                if l[4] == ")" and (l[5] == ";"):                   
                    return True
            
            else: return False
        
        except: return False
        
    elif met == "leap":
        try: 
            x = int(l[2])
            
            if (l[1] == "(") and (x == int):
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
            x = int(l[2])
            
            if (l[1] == "(") and (x == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False
    
    elif met == "get":
        try: 
            x = int(l[2])
            
            if (l[1] == "(") and (x == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False
            
    elif met == "grab":
        try: 
            x = int(l[2])
            
            if (l[1] == "(") and (x == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False
        
    elif met == "letGo":
        try: 
            x = int(l[2])
            
            if (l[1] == "(") and (x == int):
                    if (l[3] == ")") and (l[4] == ";"):
                        return True
        
        except: return False   
    
    elif met == "nop":
        if (l[1] == "(") and (l[2] == ")") and (l[3] == ";"):
            return True
        
        else: return False

    elif met in lista_noms_metodos:
        if (l[1] == "(") and (l[2] == ")") and (l[3] == ";"):
            return True
        
        else: return False

    elif met in lista_noms_metodos:
        if (l[1] == "(") and (l[2] == (str or int)) and (l[3] == ")") and (l[4] == ";"):
            return True
        
        else: return False

    elif met in lista_noms_metodos:
        if (l[1] == "(") and (l[2] == (str or int)) and (l[3] == (str or int)) and (l[4] == ")") and (l[5] == ";"):
            return True
        
        else: return False

    elif met == "if":
        print(1)
        
    elif met == "while":
        print(1)
        
    elif met == "repeat":
        print(1)    
        
    else: return False
     

lista_corchetes = []


prueba = limpiar_linea(linea)

try: 
    if prueba[0] == "defVar":
        
        marca = test_Var(prueba)
        
        if marca == True:
            print("Aquí debemos ir a la siguiente línea")
        
        else:
            print("El código no es válido") 
            #break
        
    elif prueba[0] == "defProc": 
        
        test_Proc(prueba)
        
    elif prueba[0] == "{": 
        
        h = 0
        
    elif prueba[0] in lista_noms_metodos:
        
        d =0

except: print("El código no es válido")

    
    




















