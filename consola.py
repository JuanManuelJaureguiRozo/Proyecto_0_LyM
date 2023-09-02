import modelo as modelo

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

            marca = modelo.test_Var(linea)

            if marca == False:
                print("False")
                break
            
        elif linea[0] == "{": 
            
            h = 0
            
        elif linea[0] in modelo.lista_noms_metodos:
            
            marca = modelo.test_metodo(linea)

            if marca == False:
                print("False")
                break

        print("True")

    except: print("False")