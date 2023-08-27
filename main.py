# Proyecto 0 Lenguajes y Máquinas - Grupo 12

#Integrantes:
#   - Juan Manuel Jáuregui Rozo - 201922481
#   - Adrián Suarez 

# Lectura de archivo que se requiere verificar.
archivo = open('ejemplo.txt', 'r')

# Palabras reservadas del lenguaje.

linea = "a"

"""
LISTA DE DUDAS QUE VAN SURGIENDO 
- monitor dijo que había una línea especial con la que empezaba; no la veo en los ejemplo; omitir de momento
- ¿Siempre, después de un método, hay una "{" sola, o puede que haya código despues, tipo "{ while...."?
- ¿hay algún caso en que se definan variables después de métodos, o incluso dentro? ¿O siempre al principio?     
    
"""

# "linea" es la línea que se está leyendo; de momento no se ha implementado, pero se declaró para que no muestre error
## 
lista_noms_metodos = ["jump", "walk", "leap", "turn", "turnto",
                      "drop", "grab", "letGo", "nop", "if", "else", "while", "repeat"]

def limpiar_linea(str:linea):

    #esto ya quita los espacios, no se si las indentaciones
    ## sino toca quitar lo que no sirva tal que queden solo los strings
    return linea.split(" ")

def test_Var (str:linea): 
    d
     
def test_Proc (str: linea):
    d
    
    
    

prueba = limpiar_linea(linea)

try: 
    if prueba[0] == "defVar":
        
        test_Var(prueba)
        
    elif prueba[0] == "defProc": 
        
        test_Proc(prueba)
        
    elif prueba[0] == "{": 
        
        h = 0
        
    elif prueba[0] in lista_noms_metodos:
        
        d =0

except: print("El código no es válido")

    
    




















