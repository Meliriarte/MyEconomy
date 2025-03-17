def registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contraseña):
    """Registra un nuevo usuario en el archivo de texto."""
    with open("datos/usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{apellido},{fecha_nacimiento},{usuario},{contraseña}\n")