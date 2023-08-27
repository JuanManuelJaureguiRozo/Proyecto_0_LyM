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
    return linea.split(" ")

"""
LISTA DE DUDAS QUE VAN SURGIENDO 
- monitor dijo que había una línea especial con la que empezaba; no la veo en los ejemplos; omitir de momento
- Cuando lee los números en el txt, ¿los toma como str?
- ¿Siempre, después de un método, hay una "{" sola, o puede que haya código despues, tipo "{ while...."?
- ¿hay algún caso en que se definan variables después de métodos, o incluso dentro? ¿O siempre al principio?     
    
"""

# -------------------------------------
# Listas de palabras reservadas
# -------------------------------------

# nombres de métodos, para verificar si un método es válido; para c/u toca hacer un caso, con sus parámetros y eso
# Crear función para agregar un método, así se puede hacer recursión
lista_noms_metodos = ["jump", "walk", "leap", "turn", "turnto",
                      "drop", "grab", "letGo", "nop", "if", "else", "while", "repeat"]

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
    
    if met == 
    

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

    
    




















