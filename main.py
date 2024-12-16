import os
from time import sleep
from lib_empresas import *



cargar_empresas('empresas.txt')
opcion = 0

while(opcion < 5):
    os.system("cls")
    menu()
    opcion = int(input("INGRESE OPCION : "))
    os.system("cls")
    if opcion == 1:
        registrar()
    elif opcion == 2:
        mostrar()
        input("Presion ENTER para continuar...")
    elif opcion == 3:
        actualizar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        grabar_empresas('empresas.txt')
        mostrar_mensaje("[5] SALIR")
        print("Hasta pronto")
    else:
        mostrar_mensaje("OPCIÓN INVÁLIDA!!!")
    sleep(1)