"""
import modelo as modelo
archivo = open("prueba.txt", "r")
archivo = archivo.readlines()
for linea in archivo:
    linea = modelo.limpiar_linea(linea)
    param = modelo.almacenar_parametros(linea)

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

linea = ["while", "facing", "(", "north", ")", "{", "walk", "(", "1", "north", ")", "}"]
"""

lista = [1,2]
lista.reverse()
print(lista)
