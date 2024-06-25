import json

with open("biblioteca.json", mode="r") as agregarUsuario:
    leerJson=json.loads
    print(leerJson('Usuario'))