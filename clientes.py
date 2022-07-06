archivo = open("Clientes.txt", "r")
clientes = []
for linea in archivo:
    cliente = {}
    linea = linea.strip("\n")
    datos = linea.split(",")
    print("Datos a insertar", datos)
    cliente["firstname"] = datos[0]
    cliente["surname"] = datos[1]
    cliente["country"] = datos[2]
    cliente["language"] = datos[3]
    cliente["airport"] = datos[4]
    clientes.append(cliente)
