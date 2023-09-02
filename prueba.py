import modelo as modelo
archivo = open("prueba.txt", "r")

#print(archivo[0])

with open('prueba.txt', 'r') as archivo:
    # Crea un iterador a partir del archivo
    lineas = iter(archivo)
    
    # Itera a través de las líneas del archivo
    for ln in lineas:
        # Procesa la línea actual
        linea1 = modelo.limpiar_linea(ln)
        print("Línea actual:", linea1)
        
        try:
            linea2 = modelo.limpiar_linea(next(lineas))
        except StopIteration:
            pass
        
        print(linea2)
        
        


# linea1 es la del for
# linea2 es "next(lineas)"
