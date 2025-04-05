import os
from datetime import datetime

def inicializar_archivos():
    if not os.path.exists("datos"):
        os.makedirs("datos")
    
    archivos = ["usuarios.txt", "transacciones.txt", "tarjetas.txt"]
    for archivo in archivos:
        ruta = os.path.join("datos", archivo)
        if not os.path.exists(ruta):
            open(ruta, "a").close()

def generar_id_usuario(nombre, apellido):
    try:
        ruta = os.path.join("datos", "usuarios.txt")
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            inicial_nombre = nombre[0].upper()
            inicial_apellido = apellido[0].upper()
            prefijo = f"{inicial_nombre}{inicial_apellido}"

            ultimo_numero = 0
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) >= 6:
                    id_usuario = datos[0]
                    if id_usuario.startswith(prefijo):
                        try:
                            numero = int(id_usuario[2:])
                            ultimo_numero = max(ultimo_numero, numero)
                        except ValueError:
                            continue

            nuevo_numero = ultimo_numero + 1
            return f"{prefijo}{nuevo_numero:03d}"
    except FileNotFoundError:
        return f"{nombre[0].upper()}{apellido[0].upper()}001"

def registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contraseña):
    id_usuario = generar_id_usuario(nombre, apellido)
    ruta = os.path.join("datos", "usuarios.txt")
    
    with open(ruta, "a") as archivo:
        archivo.write(f"{id_usuario},{nombre},{apellido},{fecha_nacimiento},{usuario},{contraseña}\n")

    return id_usuario

def registrar_transaccion(tipo, descripcion, monto, id_usuario):
    try:
        ruta = os.path.join("datos", "transacciones.txt")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ruta, "a") as archivo:
            archivo.write(f"{id_usuario},{tipo},{descripcion},{monto},{fecha}\n")

        return True
    except Exception as e:
        print(f"Error al registrar transacción: {str(e)}")
        return False

def registrar_tarjeta(id_usuario, banco, limite, fecha_corte):
    try:
        ruta = os.path.join("datos", "tarjetas.txt")
        
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            ultimo_numero = len(lineas) + 1
            numero_tarjeta = f"**** **** **** {ultimo_numero:04d}"

        with open(ruta, "a") as archivo:
            archivo.write(f"{id_usuario},{numero_tarjeta},{banco},{limite},{fecha_corte}\n")

        return True
    except Exception as e:
        print(f"Error al registrar tarjeta: {str(e)}")
        return False

def obtener_tarjetas_usuario(id_usuario):
    try:
        tarjetas = []
        ruta = os.path.join("datos", "tarjetas.txt")
        with open(ruta, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[0] == id_usuario:
                    tarjetas.append({
                        'numero': datos[1],
                        'banco': datos[2],
                        'limite': datos[3],
                        'fecha_corte': datos[4]
                    })
        return tarjetas
    except FileNotFoundError:
        return []

def obtener_transacciones_usuario(id_usuario, tipo=None):
    try:
        transacciones = []
        ruta = os.path.join("datos", "transacciones.txt")
        with open(ruta, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[0] == id_usuario and (tipo is None or datos[1] == tipo):
                    transacciones.append({
                        'tipo': datos[1],
                        'descripcion': datos[2],
                        'monto': datos[3],
                        'fecha': datos[4]
                    })
        return transacciones
    except FileNotFoundError:
        return []