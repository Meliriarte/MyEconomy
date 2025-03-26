import random
from datetime import datetime, timedelta
import os

def crear_directorio_datos():
    """Crea el directorio datos si no existe."""
    if not os.path.exists("datos"):
        os.makedirs("datos")
        print("Directorio 'datos' creado exitosamente")

def generar_datos_prueba():
    """Genera datos de prueba para la aplicación."""
    crear_directorio_datos()

    # Crear usuario de prueba
    try:
        with open("datos/usuarios.txt", "w") as archivo:
            archivo.write("JU001,Juan,Pérez,1990-01-15,juanperez,1234\n")
            print("Usuario creado exitosamente")
    except Exception as e:
        print(f"Error al crear el usuario: {str(e)}")

    # Generar transacciones
    tipos_transaccion = ["ingreso", "egreso"]
    descripciones_ingresos = [
        "Salario mensual",
        "Freelance",
        "Inversiones",
        "Venta de artículos",
        "Reembolso"
    ]
    descripciones_egresos = [
        "Alquiler",
        "Servicios",
        "Supermercado",
        "Transporte",
        "Entretenimiento",
        "Salud",
        "Educación",
        "Ropa",
        "Electrónicos"
    ]

    try:
        with open("datos/transacciones.txt", "w") as archivo:
            # Generar 20 transacciones
            for _ in range(20):
                tipo = random.choice(tipos_transaccion)
                if tipo == "ingreso":
                    descripcion = random.choice(descripciones_ingresos)
                    monto = random.randint(1000, 5000)
                else:
                    descripcion = random.choice(descripciones_egresos)
                    monto = random.randint(100, 1000)

                # Generar fecha aleatoria en los últimos 30 días
                fecha = datetime.now() - timedelta(days=random.randint(0, 30))
                fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")

                archivo.write(f"JU001,{tipo},{descripcion},{monto},{fecha_str}\n")
        print("Transacciones creadas exitosamente")
    except Exception as e:
        print(f"Error al crear transacciones: {str(e)}")

    # Generar tarjetas de crédito
    bancos = [
        "Banco Nacional",
        "Banco Popular",
        "Banco de Crédito",
        "Banco Interamericano",
        "Banco Continental"
    ]

    try:
        with open("datos/tarjetas.txt", "w") as archivo:
            # Generar 3 tarjetas
            for i in range(3):
                banco = random.choice(bancos)
                limite = random.randint(5000, 20000)
                fecha_corte = str(random.randint(1, 31))
                numero_tarjeta = f"**** **** **** {i+1:04d}"

                archivo.write(f"JU001,{numero_tarjeta},{banco},{limite},{fecha_corte}\n")
        print("Tarjetas creadas exitosamente")
    except Exception as e:
        print(f"Error al crear tarjetas: {str(e)}")

if __name__ == "__main__":
    generar_datos_prueba()
    print("Proceso completado.") 