import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime

# Clase base para todas las ventanas con fondo personalizado
class VentanaBase(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#333333')  # Color de fondo por defecto
        
        # Cargar imagen de fondo
        self.cargar_fondo()
        
    def cargar_fondo(self):
        try:
            # Ruta a la imagen de fondo
            fondo_path = os.path.join("datos", "imagenes", "fondo2.jpg")
            
            if not os.path.exists(fondo_path):
                raise FileNotFoundError(f"No se encontró la imagen: {fondo_path}")
                
            # Abrir y redimensionar la imagen
            imagen = Image.open(fondo_path)
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            imagen = imagen.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
            
            self.fondo = ImageTk.PhotoImage(imagen)
            
            # Crear label con la imagen de fondo
            self.background_label = tk.Label(self, image=self.fondo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.background_label.lower()  # Enviar al fondo
            
        except Exception as e:
            print(f"Error al cargar el fondo: {e}")
            # Fondo alternativo si hay error
            self.configure(bg='#333333')

# Funciones de registro y gestión de datos
def generar_id_usuario(nombre, apellido):
    """Genera un ID único para el usuario."""
    try:
        with open("datos/usuarios.txt", "r") as archivo:
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
    """Registra un nuevo usuario."""
    id_usuario = generar_id_usuario(nombre, apellido)

    try:
        with open("datos/usuarios.txt", "r"):
            pass
    except FileNotFoundError:
        with open("datos/usuarios.txt", "w"):
            pass

    with open("datos/usuarios.txt", "a") as archivo:
        archivo.write(f"{id_usuario},{nombre},{apellido},{fecha_nacimiento},{usuario},{contraseña}\n")

    return id_usuario

def registrar_transaccion(tipo, descripcion, monto, id_usuario):
    """Registra una transacción."""
    try:
        try:
            with open("datos/transacciones.txt", "r"):
                pass
        except FileNotFoundError:
            with open("datos/transacciones.txt", "w"):
                pass

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("datos/transacciones.txt", "a") as archivo:
            archivo.write(f"{id_usuario},{tipo},{descripcion},{monto},{fecha}\n")

        return True
    except Exception as e:
        print(f"Error al registrar transacción: {str(e)}")
        return False

def registrar_tarjeta(id_usuario, banco, limite, fecha_corte):
    """Registra una tarjeta de crédito."""
    try:
        try:
            with open("datos/tarjetas.txt", "r"):
                pass
        except FileNotFoundError:
            with open("datos/tarjetas.txt", "w"):
                pass

        with open("datos/tarjetas.txt", "r") as archivo:
            lineas = archivo.readlines()
            ultimo_numero = len(lineas) + 1
            numero_tarjeta = f"**** **** **** {ultimo_numero:04d}"

        with open("datos/tarjetas.txt", "a") as archivo:
            archivo.write(f"{id_usuario},{numero_tarjeta},{banco},{limite},{fecha_corte}\n")

        return True
    except Exception as e:
        print(f"Error al registrar tarjeta: {str(e)}")
        return False

def obtener_tarjetas_usuario(id_usuario):
    """Obtiene las tarjetas de un usuario."""
    try:
        tarjetas = []
        with open("datos/tarjetas.txt", "r") as archivo:
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
    """Obtiene las transacciones de un usuario.
    Si se especifica el tipo, solo devuelve las transacciones de ese tipo (ingreso/egreso)."""
    try:
        transacciones = []
        with open("datos/transacciones.txt", "r") as archivo:
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

# Ventanas de la aplicación
class VentanaInicio(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame_form = tk.Frame(self, bg="#333333", padx=40, pady=40, relief="solid", borderwidth=2)
        frame_form.pack(pady=100)

        tk.Label(frame_form, text="Iniciar Sesión", bg="#333333", fg="white",
                 font=("Sans Serif", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        tk.Label(frame_form, text="Usuario:", bg="#333333", fg="white",
                 font=("Sans Serif", 14)).grid(row=1, column=0, pady=10, padx=10)
        self.usuario = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.usuario.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(frame_form, text="Contraseña:", bg="#333333", fg="white",
                 font=("Sans Serif", 14)).grid(row=2, column=0, pady=10, padx=10)
        self.password = tk.Entry(frame_form, show="*", font=("Sans Serif", 14), width=25)
        self.password.grid(row=2, column=1, pady=10, padx=10)

        tk.Button(frame_form, text="Iniciar Sesión", command=self.login,
                  bg="#4CAF50", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).grid(row=3, column=0, columnspan=2, pady=20)

        tk.Button(self, text="Registrarse", command=lambda: self.controller.mostrar_ventana("VentanaRegistro"),
                  bg="#2196F3", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).pack(pady=20)

    def login(self):
        usuario = self.usuario.get().strip()
        password = self.password.get().strip()

        try:
            with open("datos/usuarios.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) >= 6 and datos[4] == usuario and datos[5] == password:
                        self.controller.mostrar_ventana("VentanaPrincipal")
                        return
                messagebox.showerror("Error", "Credenciales incorrectas")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de usuarios")

class MenuLateral(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#333333", width=300)  # Color oscuro para el menú
        self.pack_propagate(False)  # Mantener el ancho fijo

        # Frame superior para el título
        frame_titulo = tk.Frame(self, bg="#333333")
        frame_titulo.pack(fill="x", pady=(30, 20))
        
        tk.Label(frame_titulo, text="MyEconomy", 
                font=("Sans Serif", 24, "bold"), 
                bg="#333333", fg="white").pack()

        # Frame para el saludo
        frame_info = tk.Frame(self, bg="#333333")
        frame_info.pack(fill="x", pady=20, padx=20)
        
        # Saludo al usuario
        tk.Label(frame_info, text="¡Hola Juan!", 
                font=("Sans Serif", 18, "bold"), 
                bg="#333333", fg="#4CAF50").pack(anchor="w")

        # Frame para los botones del menú
        frame_botones = tk.Frame(self, bg="#333333")
        frame_botones.pack(fill="x", pady=20)

        # Botones del menú
        botones = [
            ("Ingresos", "ingresos"),
            ("Egresos", "egresos"),
            ("Tarjetas", "tarjetas"),
            ("Resumen", "resumen"),
            ("Configuración", "config")
        ]

        for texto, comando in botones:
            btn = tk.Button(frame_botones, text=texto,
                          command=lambda c=comando: self.controller.mostrar_seccion(c),
                          bg="#4CAF50", fg="white",
                          font=("Sans Serif", 12),
                          width=20, height=2,
                          relief="flat",
                          activebackground="#45a049",
                          activeforeground="white")
            btn.pack(pady=5)

        # Botón de cerrar sesión al final
        tk.Button(frame_botones, text="Cerrar Sesión",
                 command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                 bg="#E74C3C", fg="white",
                 font=("Sans Serif", 12),
                 width=20, height=2,
                 relief="flat",
                 activebackground="#c0392b",
                 activeforeground="white").pack(pady=5)

class VentanaPrincipal(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.id_usuario = "JU001"  # Este ID debería venir del login

        frame_principal = tk.Frame(self)
        frame_principal.pack(fill="both", expand=True)

        self.menu = MenuLateral(frame_principal, self)
        self.menu.pack(side="left", fill="y")

        self.area_contenido = tk.Frame(frame_principal)
        self.area_contenido.pack(side="right", fill="both", expand=True)

        self.secciones = {}
        
        self.crear_seccion_bienvenida()  # Nueva sección de bienvenida
        self.crear_seccion_ingresos()
        self.crear_seccion_egresos()
        self.crear_seccion_tarjetas()
        self.crear_seccion_resumen()
        self.crear_seccion_config()

        self.mostrar_seccion("bienvenida")  # Mostrar la sección de bienvenida por defecto

    def crear_seccion_bienvenida(self):
        frame = tk.Frame(self.area_contenido, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Frame superior para el saludo
        frame_saludo = tk.Frame(frame, bg="#333333", padx=20, pady=20)
        frame_saludo.pack(fill="x", pady=(0, 30))

        tk.Label(frame_saludo, text="¡Bienvenido a MyEconomy!", 
                font=("Sans Serif", 28, "bold"), 
                fg="#4CAF50", bg="#333333").pack(anchor="w")

        tk.Label(frame_saludo, text="Gestiona tus finanzas de manera inteligente", 
                font=("Sans Serif", 16), 
                fg="white", bg="#333333").pack(anchor="w", pady=(10,0))

        # Frame para mostrar las tarjetas
        frame_tarjetas = tk.Frame(frame, bg="#333333", padx=20, pady=20)
        frame_tarjetas.pack(fill="both", expand=True)

        tk.Label(frame_tarjetas, text="Mis Tarjetas de Crédito", 
                font=("Sans Serif", 20, "bold"), 
                fg="#4CAF50", bg="#333333").pack(anchor="w", pady=(0,20))

        # Frame contenedor para las tarjetas
        self.contenedor_tarjetas = tk.Frame(frame_tarjetas, bg="#333333")
        self.contenedor_tarjetas.pack(fill="both", expand=True)

        self.actualizar_tarjetas_bienvenida()

        self.secciones["bienvenida"] = frame

    def actualizar_tarjetas_bienvenida(self):
        # Limpiar tarjetas existentes
        for widget in self.contenedor_tarjetas.winfo_children():
            widget.destroy()

        # Obtener tarjetas del usuario
        tarjetas = obtener_tarjetas_usuario(self.id_usuario)
        
        # Frame para contener las filas de tarjetas
        frame_filas = tk.Frame(self.contenedor_tarjetas, bg="#333333")
        frame_filas.pack(fill="both", expand=True)
        
        # Mostrar tarjetas en filas de 2
        for i in range(0, len(tarjetas), 2):
            frame_fila = tk.Frame(frame_filas, bg="#333333")
            frame_fila.pack(fill="x", pady=10)
            
            # Primera tarjeta de la fila
            frame_tarjeta = tk.Frame(frame_fila, bg="#4CAF50", 
                                   relief="solid", borderwidth=1)
            frame_tarjeta.pack(side="left", fill="both", expand=True, padx=10)
            
            tk.Label(frame_tarjeta, text=tarjetas[i]['banco'],
                    font=("Sans Serif", 16, "bold"),
                    bg="#4CAF50", fg="white").pack(anchor="w", padx=20, pady=(20,5))
            
            tk.Label(frame_tarjeta, text=tarjetas[i]['numero'],
                    font=("Sans Serif", 14),
                    bg="#4CAF50", fg="white").pack(anchor="w", padx=20, pady=(0,5))
            
            tk.Label(frame_tarjeta, text=f"Límite: ${tarjetas[i]['limite']}",
                    font=("Sans Serif", 12),
                    bg="#4CAF50", fg="white").pack(anchor="w", padx=20, pady=(0,20))
            
            # Segunda tarjeta de la fila (si existe)
            if i + 1 < len(tarjetas):
                frame_tarjeta2 = tk.Frame(frame_fila, bg="#4CAF50", 
                                        relief="solid", borderwidth=1)
                frame_tarjeta2.pack(side="left", fill="both", expand=True, padx=10)
                
                tk.Label(frame_tarjeta2, text=tarjetas[i+1]['banco'],
                        font=("Sans Serif", 16, "bold"),
                        bg="#4CAF50", fg="white").pack(anchor="w", padx=20, pady=(20,5))
                
                tk.Label(frame_tarjeta2, text=tarjetas[i+1]['numero'],
                        font=("Sans Serif", 14),
                        bg="#4CAF50", fg="white").pack(anchor="w", padx=20, pady=(0,5))
                
                tk.Label(frame_tarjeta2, text=f"Límite: ${tarjetas[i+1]['limite']}",
                        font=("Sans Serif", 12),
                        bg="#4CAF50", fg="white").pack(anchor="w", padx=20, pady=(0,20))

    def crear_seccion_ingresos(self):
        frame = tk.Frame(self.area_contenido, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Registro de Ingresos", 
                font=("Sans Serif", 24, "bold"), fg="#4CAF50").pack(pady=(0, 30))

        # Frame para el formulario
        form_frame = tk.Frame(frame, padx=20, pady=20, 
                            relief="solid", borderwidth=1, bg="#333333")
        form_frame.pack(fill="x", pady=20)

        tk.Label(form_frame, text="Descripción:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.descripcion_ingreso = tk.Entry(form_frame, font=("Sans Serif", 12),
                                          width=40)
        self.descripcion_ingreso.pack(pady=5)

        tk.Label(form_frame, text="Monto:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.monto_ingreso = tk.Entry(form_frame, font=("Sans Serif", 12),
                                    width=40)
        self.monto_ingreso.pack(pady=5)

        tk.Button(form_frame, text="Registrar Ingreso", 
                 command=self.registrar_ingreso,
                 bg="#4CAF50", fg="white", font=("Sans Serif", 12),
                 width=20, height=2).pack(pady=20)

        # Frame para la lista de ingresos
        lista_frame = tk.Frame(frame, padx=20, pady=20,
                             relief="solid", borderwidth=1, bg="#333333")
        lista_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(lista_frame, text="Historial de Ingresos", 
                font=("Sans Serif", 16, "bold"), fg="#4CAF50", bg="#333333").pack(pady=(0, 10))

        # Crear un frame para los encabezados
        headers_frame = tk.Frame(lista_frame, bg="#333333")
        headers_frame.pack(fill="x", padx=10)

        # Encabezados
        tk.Label(headers_frame, text="Fecha", width=20, 
                font=("Sans Serif", 12, "bold"), fg="#4CAF50", 
                bg="#333333").pack(side="left")
        tk.Label(headers_frame, text="Descripción", width=30,
                font=("Sans Serif", 12, "bold"), fg="#4CAF50",
                bg="#333333").pack(side="left")
        tk.Label(headers_frame, text="Monto", width=15,
                font=("Sans Serif", 12, "bold"), fg="#4CAF50",
                bg="#333333").pack(side="left")

        # Lista de ingresos
        self.lista_ingresos = tk.Frame(lista_frame, bg="#333333")
        self.lista_ingresos.pack(fill="both", expand=True, pady=10)

        # Scrollbar y Canvas para la lista
        self.canvas_ingresos = tk.Canvas(self.lista_ingresos, bg="#333333", 
                                       highlightthickness=0)
        scrollbar = tk.Scrollbar(self.lista_ingresos, orient="vertical", 
                               command=self.canvas_ingresos.yview)
        self.frame_ingresos_scroll = tk.Frame(self.canvas_ingresos, bg="#333333")

        self.canvas_ingresos.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas_ingresos.pack(side="left", fill="both", expand=True)
        self.canvas_ingresos.create_window((0, 0), window=self.frame_ingresos_scroll, 
                                         anchor="nw", width=self.canvas_ingresos.winfo_width())

        self.frame_ingresos_scroll.bind("<Configure>", 
            lambda e: self.canvas_ingresos.configure(
                scrollregion=self.canvas_ingresos.bbox("all")))

        self.actualizar_lista_ingresos()

        self.secciones["ingresos"] = frame

    def crear_seccion_egresos(self):
        frame = tk.Frame(self.area_contenido, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Registro de Egresos", 
                font=("Sans Serif", 24, "bold"), fg="#4CAF50").pack(pady=(0, 30))

        # Frame para el formulario
        form_frame = tk.Frame(frame, padx=20, pady=20, 
                            relief="solid", borderwidth=1, bg="#333333")
        form_frame.pack(fill="x", pady=20)

        tk.Label(form_frame, text="Descripción:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.descripcion_egreso = tk.Entry(form_frame, font=("Sans Serif", 12),
                                         width=40)
        self.descripcion_egreso.pack(pady=5)

        tk.Label(form_frame, text="Monto:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.monto_egreso = tk.Entry(form_frame, font=("Sans Serif", 12),
                                   width=40)
        self.monto_egreso.pack(pady=5)

        tk.Button(form_frame, text="Registrar Egreso", 
                 command=self.registrar_egreso,
                 bg="#4CAF50", fg="white", font=("Sans Serif", 12),
                 width=20, height=2).pack(pady=20)

        # Frame para la lista de egresos
        lista_frame = tk.Frame(frame, padx=20, pady=20,
                             relief="solid", borderwidth=1, bg="#333333")
        lista_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(lista_frame, text="Historial de Egresos", 
                font=("Sans Serif", 16, "bold"), fg="#4CAF50", bg="#333333").pack(pady=(0, 10))

        # Crear un frame para los encabezados
        headers_frame = tk.Frame(lista_frame, bg="#333333")
        headers_frame.pack(fill="x", padx=10)

        # Encabezados
        tk.Label(headers_frame, text="Fecha", width=20, 
                font=("Sans Serif", 12, "bold"), fg="#4CAF50", 
                bg="#333333").pack(side="left")
        tk.Label(headers_frame, text="Descripción", width=30,
                font=("Sans Serif", 12, "bold"), fg="#4CAF50",
                bg="#333333").pack(side="left")
        tk.Label(headers_frame, text="Monto", width=15,
                font=("Sans Serif", 12, "bold"), fg="#4CAF50",
                bg="#333333").pack(side="left")

        # Lista de egresos
        self.lista_egresos = tk.Frame(lista_frame, bg="#333333")
        self.lista_egresos.pack(fill="both", expand=True, pady=10)

        # Scrollbar y Canvas para la lista
        self.canvas_egresos = tk.Canvas(self.lista_egresos, bg="#333333",
                                      highlightthickness=0)
        scrollbar = tk.Scrollbar(self.lista_egresos, orient="vertical",
                               command=self.canvas_egresos.yview)
        self.frame_egresos_scroll = tk.Frame(self.canvas_egresos, bg="#333333")

        self.canvas_egresos.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas_egresos.pack(side="left", fill="both", expand=True)
        self.canvas_egresos.create_window((0, 0), window=self.frame_egresos_scroll,
                                        anchor="nw", width=self.canvas_egresos.winfo_width())

        self.frame_egresos_scroll.bind("<Configure>",
            lambda e: self.canvas_egresos.configure(
                scrollregion=self.canvas_egresos.bbox("all")))

        self.actualizar_lista_egresos()

        self.secciones["egresos"] = frame

    def crear_seccion_tarjetas(self):
        frame = tk.Frame(self.area_contenido, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Gestión de Tarjetas", 
                font=("Sans Serif", 24, "bold"), fg="#4CAF50").pack(pady=(0, 30))

        form_frame = tk.Frame(frame, padx=20, pady=20, 
                            relief="solid", borderwidth=1, bg="#333333")
        form_frame.pack(fill="x", pady=20)

        tk.Label(form_frame, text="Nueva Tarjeta", 
                font=("Sans Serif", 16, "bold"), fg="#4CAF50", bg="#333333").pack(pady=(0, 10))

        tk.Label(form_frame, text="Banco:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.banco_tarjeta = tk.Entry(form_frame, font=("Sans Serif", 12),
                                    width=40)
        self.banco_tarjeta.pack(pady=5)

        tk.Label(form_frame, text="Límite:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.limite_tarjeta = tk.Entry(form_frame, font=("Sans Serif", 12),
                                     width=40)
        self.limite_tarjeta.pack(pady=5)

        tk.Label(form_frame, text="Fecha de Corte:", 
                font=("Sans Serif", 12), fg="#4CAF50", bg="#333333").pack(anchor="w")
        self.corte_tarjeta = tk.Entry(form_frame, font=("Sans Serif", 12),
                                    width=40)
        self.corte_tarjeta.pack(pady=5)

        tk.Button(form_frame, text="Agregar Tarjeta", 
                 command=self.agregar_tarjeta,
                 bg="#4CAF50", fg="white", font=("Sans Serif", 12),
                 width=20, height=2).pack(pady=20)

        lista_frame = tk.Frame(frame, padx=20, pady=20,
                             relief="solid", borderwidth=1, bg="#333333")
        lista_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(lista_frame, text="Mis Tarjetas", 
                font=("Sans Serif", 16, "bold"), fg="#4CAF50", bg="#333333").pack(pady=(0, 10))

        self.lista_tarjetas = tk.Listbox(lista_frame, font=("Sans Serif", 12),
                                       width=50, height=8)
        self.lista_tarjetas.pack(pady=10)

        self.secciones["tarjetas"] = frame

    def crear_seccion_resumen(self):
        frame = tk.Frame(self.area_contenido, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Resumen Financiero", 
                font=("Sans Serif", 24, "bold"), fg="#4CAF50").pack(pady=(0, 30))

        tk.Label(frame, text="Próximamente...", 
                font=("Sans Serif", 16), fg="#4CAF50").pack(pady=20)

        self.secciones["resumen"] = frame

    def crear_seccion_config(self):
        frame = tk.Frame(self.area_contenido, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Configuración", 
                font=("Sans Serif", 24, "bold"), fg="#4CAF50").pack(pady=(0, 30))

        tk.Label(frame, text="Próximamente...", 
                font=("Sans Serif", 16), fg="#4CAF50").pack(pady=20)

        self.secciones["config"] = frame

    def mostrar_seccion(self, nombre_seccion):
        for seccion in self.secciones.values():
            seccion.pack_forget()
        
        self.secciones[nombre_seccion].pack(fill="both", expand=True)
        
        if nombre_seccion == "tarjetas":
            self.actualizar_lista_tarjetas()

    def actualizar_lista_ingresos(self):
        # Limpiar lista actual
        for widget in self.frame_ingresos_scroll.winfo_children():
            widget.destroy()

        # Obtener ingresos del usuario
        ingresos = obtener_transacciones_usuario(self.id_usuario, "ingreso")
        
        # Mostrar cada ingreso
        for ingreso in ingresos:
            frame_item = tk.Frame(self.frame_ingresos_scroll, bg="#333333")
            frame_item.pack(fill="x", pady=2)
            
            tk.Label(frame_item, text=ingreso['fecha'], width=20,
                    font=("Sans Serif", 11), fg="white",
                    bg="#333333").pack(side="left")
            tk.Label(frame_item, text=ingreso['descripcion'], width=30,
                    font=("Sans Serif", 11), fg="white",
                    bg="#333333").pack(side="left")
            tk.Label(frame_item, text=f"${ingreso['monto']}", width=15,
                    font=("Sans Serif", 11), fg="#4CAF50",
                    bg="#333333").pack(side="left")

    def actualizar_lista_egresos(self):
        # Limpiar lista actual
        for widget in self.frame_egresos_scroll.winfo_children():
            widget.destroy()

        # Obtener egresos del usuario
        egresos = obtener_transacciones_usuario(self.id_usuario, "egreso")
        
        # Mostrar cada egreso
        for egreso in egresos:
            frame_item = tk.Frame(self.frame_egresos_scroll, bg="#333333")
            frame_item.pack(fill="x", pady=2)
            
            tk.Label(frame_item, text=egreso['fecha'], width=20,
                    font=("Sans Serif", 11), fg="white",
                    bg="#333333").pack(side="left")
            tk.Label(frame_item, text=egreso['descripcion'], width=30,
                    font=("Sans Serif", 11), fg="white",
                    bg="#333333").pack(side="left")
            tk.Label(frame_item, text=f"${egreso['monto']}", width=15,
                    font=("Sans Serif", 11), fg="#E74C3C",
                    bg="#333333").pack(side="left")

    def registrar_ingreso(self):
        descripcion = self.descripcion_ingreso.get().strip()
        monto = self.monto_ingreso.get().strip()

        if not descripcion or not monto:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        try:
            monto = float(monto)
            if registrar_transaccion("ingreso", descripcion, monto, self.id_usuario):
                messagebox.showinfo("Éxito", "Ingreso registrado correctamente")
                self.descripcion_ingreso.delete(0, tk.END)
                self.monto_ingreso.delete(0, tk.END)
                self.actualizar_lista_ingresos()
            else:
                messagebox.showerror("Error", "No se pudo registrar el ingreso")
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")

    def registrar_egreso(self):
        descripcion = self.descripcion_egreso.get().strip()
        monto = self.monto_egreso.get().strip()

        if not descripcion or not monto:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        try:
            monto = float(monto)
            if registrar_transaccion("egreso", descripcion, monto, self.id_usuario):
                messagebox.showinfo("Éxito", "Egreso registrado correctamente")
                self.descripcion_egreso.delete(0, tk.END)
                self.monto_egreso.delete(0, tk.END)
                self.actualizar_lista_egresos()
            else:
                messagebox.showerror("Error", "No se pudo registrar el egreso")
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")

    def agregar_tarjeta(self):
        banco = self.banco_tarjeta.get().strip()
        limite = self.limite_tarjeta.get().strip()
        fecha_corte = self.corte_tarjeta.get().strip()

        if not banco or not limite or not fecha_corte:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return

        try:
            limite = float(limite)
            if registrar_tarjeta(self.id_usuario, banco, limite, fecha_corte):
                messagebox.showinfo("Éxito", "Tarjeta agregada correctamente")
                self.banco_tarjeta.delete(0, tk.END)
                self.limite_tarjeta.delete(0, tk.END)
                self.corte_tarjeta.delete(0, tk.END)
                self.actualizar_lista_tarjetas()
                self.actualizar_tarjetas_bienvenida()
            else:
                messagebox.showerror("Error", "No se pudo agregar la tarjeta")
        except ValueError:
            messagebox.showerror("Error", "El límite debe ser un número válido")

    def actualizar_lista_tarjetas(self):
        self.lista_tarjetas.delete(0, tk.END)
        tarjetas = obtener_tarjetas_usuario(self.id_usuario)
        for tarjeta in tarjetas:
            self.lista_tarjetas.insert(tk.END, 
                f"Banco: {tarjeta['banco']} | Límite: ${tarjeta['limite']} | Corte: {tarjeta['fecha_corte']}")

class VentanaRegistro(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame_form = tk.Frame(self, bg="#FFFFFF", padx=40, pady=40, relief="solid", borderwidth=2)
        frame_form.pack(pady=40)

        tk.Label(frame_form, text="Registro de Usuario", bg="#FFFFFF",
                 font=("Sans Serif", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 30))

        tk.Label(frame_form, text="Nombre:", bg="#FFFFFF", 
                 font=("Sans Serif", 14)).grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.nombre_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.nombre_entry.grid(row=1, column=1, pady=10, padx=10)

        tk.Label(frame_form, text="Apellido:", bg="#FFFFFF", 
                 font=("Sans Serif", 14)).grid(row=2, column=0, pady=10, padx=10, sticky="e")
        self.apellido_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.apellido_entry.grid(row=2, column=1, pady=10, padx=10)

        tk.Label(frame_form, text="Fecha de Nacimiento:", bg="#FFFFFF", 
                 font=("Sans Serif", 14)).grid(row=3, column=0, pady=10, padx=10, sticky="e")
        self.fecha_nacimiento_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.fecha_nacimiento_entry.grid(row=3, column=1, pady=10, padx=10)

        tk.Label(frame_form, text="Usuario:", bg="#FFFFFF", 
                 font=("Sans Serif", 14)).grid(row=4, column=0, pady=10, padx=10, sticky="e")
        self.usuario_entry = tk.Entry(frame_form, font=("Sans Serif", 14), width=25)
        self.usuario_entry.grid(row=4, column=1, pady=10, padx=10)

        tk.Label(frame_form, text="Contraseña:", bg="#FFFFFF", 
                 font=("Sans Serif", 14)).grid(row=5, column=0, pady=10, padx=10, sticky="e")
        self.contrasena_entry = tk.Entry(frame_form, show="*", font=("Sans Serif", 14), width=25)
        self.contrasena_entry.grid(row=5, column=1, pady=10, padx=10)

        tk.Button(frame_form, text="Registrar", command=self.registrar_usuario, 
                  bg="#4CAF50", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).grid(row=6, column=0, columnspan=2, pady=20)

        tk.Button(self, text="Volver", command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                  bg="#2196F3", fg="white", font=("Sans Serif", 14),
                  width=20, height=2).pack(pady=20)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get().strip()
        apellido = self.apellido_entry.get().strip()
        fecha_nacimiento = self.fecha_nacimiento_entry.get().strip()
        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not (nombre and apellido and fecha_nacimiento and usuario and contrasena):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            id_usuario = registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contrasena)
            messagebox.showinfo("Éxito", f"Usuario registrado con éxito. ID: {id_usuario}")
            self.nombre_entry.delete(0, tk.END)
            self.apellido_entry.delete(0, tk.END)
            self.fecha_nacimiento_entry.delete(0, tk.END)
            self.usuario_entry.delete(0, tk.END)
            self.contrasena_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al registrar el usuario: {str(e)}")

class PantallaInicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((200, 200), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(self, image=self.logo, bg="white").place(relx=0.5, rely=0.5, anchor="center")
        except FileNotFoundError:
            tk.Label(self, text="LOGO NO DISPONIBLE", bg="white", font=("Sans Serif", 20)).pack(expand=True)
        self.after(3000, lambda: controller.mostrar_ventana("VentanaInicio"))

class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.state("zoomed")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PantallaInicio, VentanaInicio, VentanaPrincipal, VentanaRegistro):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.mostrar_ventana("PantallaInicio")

    def mostrar_ventana(self, nombre_ventana):
        self.frames[nombre_ventana].tkraise()

if __name__ == "__main__":
    # Crear directorios si no existen
    if not os.path.exists("datos"):
        os.makedirs("datos")
    if not os.path.exists(os.path.join("datos", "imagenes")):
        os.makedirs(os.path.join("datos", "imagenes"))
    
    app = MyEconomyApp()
    app.mainloop()