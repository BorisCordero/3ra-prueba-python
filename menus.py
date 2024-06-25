from funciones import *
import json

while True:

    print("********************************")
    print("*         Mundo Libro          *")
    print("********************************")

    opciones_menu_biblioteca=['Mantenedor de usuarios','Reportes','Salir']
    contador_menu_biblioteca=0

    for i in opciones_menu_biblioteca:
        contador_menu_biblioteca+=1
        print(f'[{contador_menu_biblioteca}]{i}')

    opcion=int(input('Ingrese el numero de la opcion que desea seleccionar: '))
    if opcion==1:
        print("*********************************")
        print("*    Mantenedor de usuarios     *")
        print("*********************************")

        opciones_menu_mantenedor=[' - Agregar usuario',' - Editar usuario',' - Eliminar usuario',' - Buscar usuario',' - Volver']
        contador_menu_mantenedor=0
        for i in opciones_menu_mantenedor:
                contador_menu_mantenedor+=1
                print(f'[{contador_menu_mantenedor}]{i}')
        
        opcion_mantenedor_usuario=int(input('Ingrese el numero de la opcion que desea seleccionar: '))
        if opcion_mantenedor_usuario == 1:
            agregarUsuario(nombre:str,credito:int):
        elif opcion_mantenedor_usuario == 3:
            agregarUsuario(nombre:str,credito:int):