def generar_id_usuario(nombre, apellido):
    """Genera un ID único para el usuario basado en las iniciales y un número secuencial."""
    try:
        with open("datos/usuarios.txt", "r") as archivo:
            lineas = archivo.readlines()
            # Obtener las iniciales
            inicial_nombre = nombre[0].upper()
            inicial_apellido = apellido[0].upper()
            prefijo = f"{inicial_nombre}{inicial_apellido}"
            
            # Encontrar el último número usado para este prefijo
            ultimo_numero = 0
            for linea in lineas:
                datos = linea.strip().split(",")
                if len(datos) >= 6:  # Asegurarnos de que la línea tenga el campo ID
                    id_usuario = datos[0]
                    if id_usuario.startswith(prefijo):
                        try:
                            numero = int(id_usuario[2:])
                            ultimo_numero = max(ultimo_numero, numero)
                        except ValueError:
                            continue
            
            # Generar el nuevo número
            nuevo_numero = ultimo_numero + 1
            # Formatear el número con ceros a la izquierda (3 dígitos)
            return f"{prefijo}{nuevo_numero:03d}"
    except FileNotFoundError:
        # Si el archivo no existe, empezar desde 001
        return f"{nombre[0].upper()}{apellido[0].upper()}001"

def registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contraseña):
    """Registra un nuevo usuario en el archivo de texto."""
    # Generar ID único
    id_usuario = generar_id_usuario(nombre, apellido)
    
    # Verificar si el archivo existe, si no, crearlo
    try:
        with open("datos/usuarios.txt", "r"):
            pass
    except FileNotFoundError:
        with open("datos/usuarios.txt", "w"):
            pass
    
    # Agregar el nuevo usuario
    with open("datos/usuarios.txt", "a") as archivo:
        archivo.write(f"{id_usuario},{nombre},{apellido},{fecha_nacimiento},{usuario},{contraseña}\n")
    
    return id_usuario