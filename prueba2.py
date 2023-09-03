import modelo as modelo
archivo = open("prueba.txt", "r")
archivo = archivo.readlines()
for linea in archivo:
    linea = modelo.limpiar_linea(linea)
    param = modelo.almacenar_parametros(linea)