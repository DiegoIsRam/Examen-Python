

# clientes = [
#     {"firstname": "Diego Israel", "surname": "Ramirez Martinez",
#         "airport": "Santa Lucía", "language": "Español"},
#     {"firstname": "Gloria Marlene", "surname": "Ramirez Martinez",
#         "airport": "Santa Lucía", "language": "Español"}

# ]
clientes = []
cliente = {}
archivo = open("Clientes.txt", "r")
for linea in archivo:
    linea = linea.strip("\n")
    datos = linea.split(",")
    cliente["firstname"] = datos[0]
    cliente["surname"] = datos[1]
    clientes.append(cliente)

print(clientes)
