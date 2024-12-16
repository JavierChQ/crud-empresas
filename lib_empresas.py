ANCHO = 40

dic_empresas = {}
def cargar_empresas(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    str_empresas = archivo.read()
    archivo.close()

    lista_empresas = str_empresas.splitlines()
    for str_fila in lista_empresas:
        lista_fila = str_fila.split(',')
        dic_registro = {
           'razon_social':lista_fila[1],
           'direccion' :lista_fila[2]
        }
        dic_nueva_empresa = {
            lista_fila[0] : dic_registro
        }
        dic_empresas.update(dic_nueva_empresa)


def grabar_empresas(file_name):
    str_empresas = ""
    for empresa_clave,empresa_valor in dic_empresas.items():
        str_empresas += empresa_clave + ","
        for registro_clave,registro_valor in empresa_valor.items():
            str_empresas += registro_valor
            if registro_clave != 'direccion':
                str_empresas += ','
            else:
                str_empresas += '\n'
    
    fsalida = open(file_name,'w')
    fsalida.write(str_empresas)
    fsalida.close()

def mostrar_mensaje(texto):
    print("*" * ANCHO + "*" * ANCHO)
    if texto != " ":
        print(" " * 20 + texto)
        print("*" * ANCHO + "*" * ANCHO)

def menu():
    mostrar_mensaje("GESTIÓN DE EMPRESAS")
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    mostrar_mensaje(" ")

def mostrar():
    mostrar_mensaje("[2] MOSTRAR EMPRESAS")
    for ruc,datos in dic_empresas.items():
        print(f"RUC : {ruc}")
        print(f"Razon social : {datos['razon_social']}")
        print(f"Direccion : {datos['direccion']}")
        mostrar_mensaje(" ")

def registrar():
    mostrar_mensaje("[1] REGISTRAR EMPRESA")
    ruc = input("RUC    :")
    razon_social = input("RAZON SOCIAL  :")
    direccion = input("DIRECCION    :")
    dic_nueva_empresa = {
        ruc : {
                'razon_social':razon_social,
                'direccion': direccion
                }
    }
    dic_empresas.update(dic_nueva_empresa)
    print("Empresa registrada con exito")

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
    ruc = input("INGRESE EL RUC DE LA EMPRESA A ACTUALIZAR: ")
    if ruc in dic_empresas:
        print(f"EMPRESA A ACTUALIZAR  {dic_empresas[ruc]['razon_social']}")
        nueva_razon_social = input('RAZON SOCIAL : ')
        nueva_direccion = input('DIRECCION :')
        dic_act_empresa = {
            ruc : {
                'razon_social':nueva_razon_social,
                'direccion':nueva_direccion
            }
        }
        dic_empresas.update(dic_act_empresa)
        print("EMPRESA ACTUALIZADO CON EXITO")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR EMPRESA")
    ruc = input("INGRESE EL RUC DE LA EMPRESA A ELIMINAR : ")
    if ruc in dic_empresas:
        dic_empresas.pop(ruc)
        print("EMPRESA ELIMINADA")
    else:
        print("NO SE ENCONTRO LA EMPRESA")