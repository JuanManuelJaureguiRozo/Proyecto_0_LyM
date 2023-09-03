import modelo as modelo

#recordar que solo pueden aparecer solos, o dentro de un condición
corchetes =[]
"""
archivo = open("prueba.txt", "r")

for linea in archivo:
    linea = modelo.limpiar_linea(linea)
    
    try: 
        if linea[0] == "defVar":
            
            marca = modelo.test_Var(linea)

            if marca == False:
                print("False")
                break
            
        elif linea[0] == "defProc": 

            marca = modelo.test_Proc(linea)

            if marca == False:
                print("False")
                break
            
        elif (linea[0] == "{") or (linea[0] == "}" ): 
            
            marca = modelo.test_corchete(linea)

            if marca == False:
                print("False")
                break
            
            elif marca == True:
                if linea[0] == "{":
                    corchetes.append("{")
                    
                elif linea[0] == "}":
                    corchetes.pop(-1)
                    if len(corchetes) < 0:
                        print("False")
                        break
                     
        elif linea[0] in modelo.lista_noms_metodos:
            
            marca = modelo.test_metodo(linea)

            if marca == False:
                print("False")
                break
        
        elif linea[0] == "":
            print("a")
            

    except: print("False")
    """
#------------------------------------------
#Intento leer varias líneas al tiempo
#------------------------------------------

archivo = open("prueba.txt", "r")

matriz_archivo = []

for linea in archivo:
    linea = modelo.limpiar_linea(linea)
    
    matriz_archivo.append(linea)
    
print(matriz_archivo)

for linea_en_una_lista in matriz_archivo:
    numero = matriz_archivo.index(linea_en_una_lista)
    
    try: 
        if linea[0] == "defVar":
            
            marca = modelo.test_Var(linea_en_una_lista)

            if marca == False:
                print("False")
                break
            
        elif linea[0] == "defProc": 

            marca = modelo.test_Proc(linea_en_una_lista)

            if marca == False:
                print("False")
                break
            
        elif (linea[0] == "{") or (linea[0] == "}" ): 
            
            marca = modelo.test_corchete(linea_en_una_lista)

            if marca == False:
                print("False")
                break
            
            elif marca == True:
                if linea[0] == "{":
                    corchetes.append("{")
                    
                elif linea[0] == "}":
                    corchetes.pop(-1)
                    if len(corchetes) < 0:
                        print("False")
                        break
                     
        elif linea[0] in modelo.lista_noms_metodos:
            
            marca = modelo.test_metodo(linea_en_una_lista)

            if marca == False:
                print("False")
                break
        
        elif linea[0] == "":
            print("a")
            

    except: print("False")




