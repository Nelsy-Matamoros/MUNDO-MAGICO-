#metoro #01
""
file = open(" my_notes.txt.01", "r")
print(file)
lineas=file.readline()
print(lineas)
file.close()     #cerrar el documento.
""
#metrodo #02
with open(" my_notes.txt.01", "r") as archivo:
    line = archivo.readline()
    print(lineas)
