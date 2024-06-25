import json


with open("biblioteca.json", mode="r") as archivoJson:
    datos=json.load(archivoJson)


def agregarUsuario(nombre:str,credito:int):
    with open("biblioteca.json", mode="r") as archivoJson:
        datos=json.loads(archivoJson)
        
        usuario={
            "id":len(datos["UsuarioID"])+1,
            "nombre":"badsahgsdjada",
            "credito":23112312
        }
        datos["usuario"].append(usuario)

def eliminarUsuario(UsuarioID:int):
    with open("biblioteca.json", mode="r") as archivoJson:
        datos=json.load(archivoJson)
    usuario=datos["Usuario"]
    for i in usuario:
        if usuario == UsuarioID:
            Usuario.remove(usuario)
            break

with open("biblioteca.json", mode="r") as archivoJson:
    datos=json.load(archivoJson)
