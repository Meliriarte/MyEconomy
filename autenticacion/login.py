def login(usuario, contraseña):
    """Verifica si el usuario y la contraseña son correctos."""
    try:
        with open("datos/usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) >= 6:  # Asegurarnos de que la línea tenga todos los campos
                    usuario_guardado = datos[4]  # El usuario está ahora en la posición 4
                    contraseña_guardada = datos[5]  # La contraseña está ahora en la posición 5
                    id_usuario = datos[0]  # El ID está en la posición 0

                    if usuario == usuario_guardado:
                        if contraseña == contraseña_guardada:
                            return True, f"Inicio de sesión exitoso. ID: {id_usuario}"  # Usuario y contraseña correctos
                        else:
                            return False, "Contraseña incorrecta"  # Usuario existe, pero contraseña incorrecta
            return False, "Usuario no encontrado"  # Usuario no existe
    except FileNotFoundError:
        return False, "El archivo de usuarios no existe"