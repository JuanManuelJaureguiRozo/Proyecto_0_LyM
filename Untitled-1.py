
linea = "hola mundo"



def limpiar_linea(line):

    #quita todo lo 'extra', dejando solo los strings
    line = line.replace("(", ",(,")
    line = line.replace(")", ",),")
    line = line.replace("{", ",{,")
    line = line.replace("}", ",},")
    line = line.replace("\t", ",")
    line = line.replace(" ", ",")
    
    line = line.split(",")

    for elemento in line:
        if elemento == "":
            line.remove(elemento)
        elif elemento == " ":
            line.remove(elemento)

    for elemento in line:
        if elemento == "":
            line.remove(elemento)
        elif elemento == " ":
            line.remove(elemento)

    return line

print(limpiar_linea(linea))