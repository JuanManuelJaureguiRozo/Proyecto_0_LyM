import modelo as modelo

archivo = open("prueba.txt", "r")

corchetes =[]

matriz_archivo = []

for linea in archivo:
    if linea != "\n": 
        linea = modelo.limpiar_linea(linea)
        matriz_archivo.append(linea)

def funcion_consola(linea_en_una_lista, matriz_archivo, numero):
    
    try: 

        if linea_en_una_lista[0] == "defVar":
            
            marca = modelo.test_Var(linea_en_una_lista)

            if marca == True:
                pass
            
        elif linea_en_una_lista[0] == "defProc" or linea_en_una_lista[0] in modelo.lista_noms_proc: 

            params = modelo.almacenar_parametros(linea_en_una_lista)
            marca = modelo.test_Proc(linea_en_una_lista, params)

            if marca == True:
                pass
            
        elif (linea_en_una_lista[0] == "{") or (linea_en_una_lista[0] == "}" ): 
            
            marca = modelo.test_corchete(linea_en_una_lista)

            if marca == True:
                pass
            
            elif marca == True:
                if linea_en_una_lista[0] == "{":
                    corchetes.append("{")
                    
                elif linea_en_una_lista[0] == "}":
                    try:
                        corchetes.pop(-1)
                    except: print("False")
                     
        elif (linea_en_una_lista[0] in modelo.lista_noms_metodos):
            
            marca = modelo.test_metodo(linea_en_una_lista, matriz_archivo, numero)

            if marca == True:
                pass

        elif linea_en_una_lista[0] in modelo.lista_condicionales:
            
            for elemento in linea_en_una_lista:
                if elemento == "{":
            
                    marca = modelo.test_Proc(linea_en_una_lista, matriz_archivo, numero)
                    #print(marca)

            if marca == True:
                pass

    except: print("False")

for linea_en_una_lista in matriz_archivo:
    try:
        print(linea_en_una_lista)
        numero = matriz_archivo.index(linea_en_una_lista)
        funcion_consola(linea_en_una_lista, matriz_archivo, numero)

    except: print("False")






