# Proyecto 0 Lenguajes y Máquinas - Grupo 12

#Integrantes:
#   - Juan Manuel Jáuregui Rozo - 201922481
#   - Adrián Suarez 

# Lectura de archivo que se requiere verificar.
archivo = open('ejemplo.txt', 'r')

# Palabras reservadas del lenguaje.

linea = "a"

# "linea" es la línea que se está leyendo; de momento no se ha implementado, pero se declaró para que no muestre error
## 

def limpiar_linea(list:linea):

    #esto ya quita los espacios, no se si las indentaciones
    ## sino toca quitar lo que no sirva tal que queden solo los strings
    ### el caso de los parentesis pueden o NO llevar espacio dentro, tipo "(a, b)"
    #### tmpc sabemos cuandos parámetros puedan solicitar; toca hacer un separador que recorra toda la lista
    # tal vez podría recorrerse al revés, pues los paréntesis siempre van al final
    return linea.split(" ")

"""
LISTA DE DUDAS QUE VAN SURGIENDO 
- monitor dijo que había una línea especial con la que empezaba; no la veo en los ejemplos; omitir de momento
- Cuando lee los números en el txt, ¿los toma como str?
- ¿Siempre, después de un método, hay una "{" sola, o puede que haya código despues, tipo "{ while...."?
- ¿hay algún caso en que se definan variables después de métodos, o incluso dentro? ¿O siempre al principio?   
- los métodos siempre tienen un espacio para los paréntesis? Tipo "jump ()"  

LISTA PROBLEMAS / DETALLES QUE FALTAN POR IMPLEMENTAR
- Seguramente toque separar los parametros str / int para poder verficar dentro de un método que sea del tipo correcto
    - Cuando se declare un nuevo parametro toca intentara volverlo int con un try/except, así sabemos si es int o no, pues
    pues todos vienen como str
- Seguramente toque separar los métodos normales, los nuevos, y los condicionales, haciendo una nueva función para verificar los condicionales
    - Puede hacerse agregando un 5to caso, o con un if dentro del verificador de métodos; seguramente 1era opción
- Falta, después del test_Var, decirle que lo agregue a la lista
- Falta limpiar bien la linea, pues cuando vienen pegados toca separar los paréntesis, los ";", los "\t", y otros casos posibles
    - La última línea de un bloque NO tiene ";" lo cual será un problema
        - tal vez verificando que la siguiente línea sea "}" se pueda saltar este caso
- Para los "{}" mejor hacer una pila simple; en una lista previamente declarada se van agregando los "{", y cada que salga un 
"}" se va eliminando la -1 posición con una función, la cual preguna el len de la lista. Si es <0 se devuelve True y el programa
sigue, sino se para, y al final del todo se pregunta el tamaño de la lista, si no es =0, está mal y el txt es incorrecto
- Para leer las líneas sería mejor hacer un for, donde al final se sume 1 a la línea, así podemos seguir leyendo en casos correctos
- Recordar que todo debe volverse minúscula, sobre todo en los parámetros
- Los nuevos métodos toca agregarlos de una en la lista de métodos para que haya recursión, pero ¿cómo hacemos para saber si 
los parámetros son correctos (tipo), antes de leer las líneas de abajo?

"""

# -------------------------------------
# Listas de palabras reservadas
# -------------------------------------

# nombres de métodos, para verificar si un método es válido; para c/u toca hacer un caso, con sus parámetros y eso
# Crear función para agregar un método, así se puede hacer recursión
lista_noms_metodos = ["jump", "walk", "leap", "turn", "turnto",
                      "drop", "grab", "letGo", "nop", "if", "else", "while", "repeat"]

lista_condicionales =["facing", "can", "not"]

# parametros por default del proyecto; crear función que agregue cuando se declare una nueva variable
## Recordar que toca tomar volver todo a minúscula antes de corroborarlo con estas variables
lista_parametros = ["north", "south", "east", "west", "n", "s", "e", "w",
                    "left", "right", "around"]


# -------------------------------------
# Funciones para agregar a las listas
# -------------------------------------

def agregar_metodo ():
    return y

def agregar_parametro ():
    return y

# -------------------------------------
# Funciones para examinar líneas
# -------------------------------------
def test_Var (list:linea): 
    
    if linea[0] == str and linea[1] == str and linea[2] == (str or int):
        return True
    
    else: return False
    
     
def test_Proc (list: linea):
    d
    
def test_metodo (list:linea):
    met = linea[0]
    
    if met == "jump":
        print(a)
    
    elif met == "walk":
        print(a)
        
    elif met == "leap":
        print(a)
        
    elif met == "turn":
        print(a)
        
    elif met == "turnto":
        print(a)
        
    elif met == "drop":
        print(a)
        
    elif met == "grab":
        print(a)
        
    elif met == "letGo":
        print(a)   
    
    elif met == "nop":
        print(a)
        
    elif met == "if":
        print(a)
        
    elif met == "while":
        print(a)
        
    elif met == "repeat":
        print(a)    
     




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

    
    




















