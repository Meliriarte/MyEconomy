def login(usuario, contraseña):
    """Verifica si el usuario y la contraseña son correctos."""
    try:
        with open("datos/usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) >= 5:  # Asegurarnos de que la línea tenga todos los campos
                    usuario_guardado = datos[3]  # El usuario está en la posición 3
                    contraseña_guardada = datos[4]  # La contraseña está en la posición 4

                    if usuario == usuario_guardado:
                        if contraseña == contraseña_guardada:
                            return True, "Inicio de sesión exitoso"  # Usuario y contraseña correctos
                        else:
                            return False, "Contraseña incorrecta"  # Usuario existe, pero contraseña incorrecta
            return False, "Usuario no encontrado"  # Usuario no existe
    except FileNotFoundError:
        return False, "El archivo de usuarios no existe"