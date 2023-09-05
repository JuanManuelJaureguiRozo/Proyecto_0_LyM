import modelo as modelo

archivo = open("prueba.txt", "r")

corchetes = 0

params_proc_actual = []

params_cond_actual = []

matriz_archivo = []

for linea in archivo:
    if linea != "\n": 
        linea = modelo.limpiar_linea(linea)
        matriz_archivo.append(linea)

for linea in matriz_archivo:
    for string in linea:
        if string == "{":
            corchetes += 1
        elif string == "}":
            corchetes -= 1

def funcion_consola(matriz_archivo):
    centinela = True
    tam = len(matriz_archivo)
    i = 0
    while centinela == True and i < tam:
        linea_en_una_lista = matriz_archivo[i] 
        numero = matriz_archivo.index(linea_en_una_lista)

        if linea_en_una_lista[0] == "defVar":
            
            marca = modelo.test_Var(linea_en_una_lista)

            if marca == False or marca == None:
                centinela = False
                print(marca)
            
            else:
                i += 1
            
        elif linea_en_una_lista[0] == "defProc" or linea_en_una_lista[0] in modelo.lista_noms_proc: 

            params = modelo.almacenar_parametros(linea_en_una_lista)
            for param in params:
                params_proc_actual.append(param)
            marca = modelo.test_Proc(linea_en_una_lista, params)

            if marca == False or marca == None:
                centinela = False
                print(marca)
            
            else:
                i += 1
            
        elif (linea_en_una_lista[0] == "{") or (linea_en_una_lista[0] == "}" ): 
            
            marca = modelo.test_corchete(linea_en_una_lista)

            if marca == False or marca == None:
                centinela = False
                print(marca)
            
            else:
                i += 1
                     
        elif (linea_en_una_lista[0] in modelo.lista_noms_metodos):
            
            params = modelo.almacenar_parametros(linea_en_una_lista)
            if params != None:
                for v in params:
                    if v in params_proc_actual:
                        marca = modelo.test_metodo(linea_en_una_lista, matriz_archivo, numero, params)
                    else:
                        marca = modelo.test_metodo(linea_en_una_lista, matriz_archivo, numero, params_proc_actual)

            if marca == False or marca == None:
                centinela = False
                print(marca)
            
            else:
                i += 1

        elif linea_en_una_lista[0] in modelo.lista_condicionales:

            marca = modelo.test_condicionales(linea_en_una_lista, matriz_archivo, numero, params_proc_actual)

            if marca == False or marca == None:
                centinela = False
                print(marca)
            
            else:
                i += 1

    if centinela == True:
        print("El programa es correcto")

if corchetes == 0:
    funcion_consola(matriz_archivo)
else: print("False")






