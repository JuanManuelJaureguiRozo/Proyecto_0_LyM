import modelo as modelo



#l = ['if','facing','(','n',')','{','walk','(','1','w',')','}','else','{', 'walk','(','2','east',')','}']
lili = [ 'if','can','(','walk','(','1','west',')',')','{','walk','(','1','west',')','}','else','{','nop','(',')','}' ]


l = ['if','facing','(','n',')','{','if','facing','(','n',')','{','walk','(','1','w',')','}','else','{', 'walk','(','2','east',')','}',"}",'else','{', 'walk','(','2','east',')','}']


if (l[5] == "{") and (l[6] in modelo.lista_condicionales):
                            l.reverse()
                            index_alreves = l.index("else")
                            l.reverse()
                            index_alderecho = len(l) - (index_alreves+2)
                            
                            lim1 = 5
                            lim2 = index_alderecho
                            
                            h = modelo.partir(lim1,lim2,l)
                            lil = h[0] #aquello dentro de paréntesis que toca verificar
                            l = h[1]
                            print(lil)
                            print(l)



"""
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

limi1 = 2
limi2 = lili.index(")") +1


h =partir(limi1,limi2,lili)
n = h[0]
lili = h[1]

limii1 = 2
limii2 = lili.index("}")
print(limii1)
print(limii2)

print(partir(limii1,limii2,lili))
"""

"""
if (l[2] == "(") and (l[3] in modelo.lista_parametros_turn2) and (l[4] == ")"):
    if (l[5] == "{") :
        
        lim1 = 5
        lim2 = l.index("}")
        
        h = partir(lim1,lim2,l)
        lil = h[0]
        l = h[1]
        
        if (lil[0] in modelo.lista_noms_metodos) or (lil[0] in modelo.lista_noms_proc):
            if (modelo.test_metodo(lil) == True) and (l[5] == "else") and (l[6] == "{"):
                lim1 = 6
                lim2 = l.index("}")
                lil = []
                # esto saca la cadena entre los parentesis y la evalúa como un método
                i=0
                while i < (lim2-lim1):
                    lil.append(l[lim1])
                    l.pop(lim1)
                    i += 1
                l.pop(lim1)
                lil.pop(0)
                lil.append(";")
                if modelo.test_metodo(lil) == True:
                    #return True
                    print("a")
                
        elif lil[0] in modelo.lista_condicionales:
            print("me corchó")
        """    
                                
                                

                                   
                                
                                