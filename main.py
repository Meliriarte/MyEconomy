import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime

# Configuración de estilos
COLOR_PRIMARIO = "#2c3e50"
COLOR_SECUNDARIO = "#3498db"
COLOR_TERCIARIO = "#e74c3c"
COLOR_CUARTO = "#2ecc71"
COLOR_FONDO = "#ecf0f1"
COLOR_TEXTO = "#2c3e50"
COLOR_TEXTO_CLARO = "#ecf0f1"
FUENTE_TITULOS = ("Helvetica", 18, "bold")
FUENTE_SUBTITULOS = ("Helvetica", 14)
FUENTE_TEXTO = ("Helvetica", 12)
FUENTE_BOTONES = ("Helvetica", 12, "bold")

# Función para inicializar archivos
def inicializar_archivos():
    # Crear directorio datos si no existe
    if not os.path.exists("datos"):
        os.makedirs("datos")
    
    # Crear archivos si no existen
    archivos = ["usuarios.txt", "transacciones.txt", "tarjetas.txt"]
    for archivo in archivos:
        ruta = os.path.join("datos", archivo)
        if not os.path.exists(ruta):
            open(ruta, "a").close()  # Crear archivo vacío

# Funciones de registro y gestión de datos
def generar_id_usuario(nombre, apellido):
    """Genera un ID único para el usuario."""
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
    """Registra un nuevo usuario."""
    id_usuario = generar_id_usuario(nombre, apellido)
    ruta = os.path.join("datos", "usuarios.txt")
    
    with open(ruta, "a") as archivo:
        archivo.write(f"{id_usuario},{nombre},{apellido},{fecha_nacimiento},{usuario},{contraseña}\n")

    return id_usuario

def registrar_transaccion(tipo, descripcion, monto, id_usuario):
    """Registra una transacción."""
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
    """Registra una tarjeta de crédito."""
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
    """Obtiene las tarjetas de un usuario."""
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
    """Obtiene las transacciones de un usuario."""
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

# Clase base para todas las ventanas con fondo personalizado
class VentanaBase(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg=COLOR_FONDO)
        
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
            self.configure(bg=COLOR_FONDO)

# Ventanas de la aplicación
class VentanaInicio(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # Frame principal con sombra
        frame_principal = tk.Frame(self, bg=COLOR_FONDO, bd=0)
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")
        
        # Frame del formulario con efecto de tarjeta
        frame_form = tk.Frame(frame_principal, bg="white", padx=40, pady=40, 
                            relief="solid", borderwidth=0, 
                            highlightbackground="#bdc3c7", highlightthickness=1)
        frame_form.pack(pady=20, padx=20)
        
        # Logo de la aplicación
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(frame_form, image=self.logo, bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))
        except:
            pass

        # Título
        tk.Label(frame_form, text="Iniciar Sesión", bg="white", fg=COLOR_PRIMARIO,
                font=FUENTE_TITULOS).grid(row=1, column=0, columnspan=2, pady=(0, 30))

        # Campos del formulario
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()
        
        self.crear_campo(frame_form, "Usuario:", 2, self.usuario)
        self.crear_campo(frame_form, "Contraseña:", 3, self.password, show="*")

        # Botón de inicio de sesión
        btn_login = tk.Button(frame_form, text="Iniciar Sesión", command=self.login,
                            bg=COLOR_CUARTO, fg="white", font=FUENTE_BOTONES,
                            width=20, height=2, bd=0, activebackground="#27ae60",
                            activeforeground="white")
        btn_login.grid(row=4, column=0, columnspan=2, pady=(20, 10))
        
        # Botón de registro
        btn_registro = tk.Button(frame_principal, text="Registrarse", 
                               command=lambda: self.controller.mostrar_ventana("VentanaRegistro"),
                               bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                               width=20, height=2, bd=0, activebackground="#2980b9",
                               activeforeground="white")
        btn_registro.pack(pady=(0, 20))

    def crear_campo(self, frame, texto, fila, variable, show=None):
        """Crea un campo de entrada con estilo consistente"""
        tk.Label(frame, text=texto, bg="white", fg=COLOR_TEXTO,
                font=FUENTE_SUBTITULOS, anchor="w").grid(row=fila, column=0, pady=(10, 5), padx=10, sticky="ew")
        
        entry = tk.Entry(frame, textvariable=variable, font=FUENTE_TEXTO, width=25, bd=1, relief="solid",
                        highlightbackground="#bdc3c7", highlightthickness=1)
        if show:
            entry.config(show=show)
        entry.grid(row=fila, column=1, pady=(10, 5), padx=10)
        return entry

    def login(self):
        usuario = self.usuario.get().strip()
        password = self.password.get().strip()

        try:
            ruta = os.path.join("datos", "usuarios.txt")
            with open(ruta, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) >= 6 and datos[4] == usuario and datos[5] == password:
                        self.controller.mostrar_ventana("VentanaPrincipal")
                        return
                messagebox.showerror("Error", "Credenciales incorrectas")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de usuarios")

# Clase para el menú lateral mejorado
class MenuLateral(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=COLOR_PRIMARIO, width=70)  # Menú inicialmente colapsado
        self.pack_propagate(False)
        
        # Logo pequeño
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((40, 40), Image.Resampling.LANCZOS)
            self.logo_pequeno = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(self, image=self.logo_pequeno, bg=COLOR_PRIMARIO)
            logo_label.pack(pady=20)
        except:
            pass

        # Botón para desplegar el menú
        self.boton_menu = tk.Button(self, text="☰", command=self.toggle_menu,
                                  bg=COLOR_PRIMARIO, fg=COLOR_TEXTO_CLARO, font=("Arial", 18),
                                  relief="flat", bd=0, activebackground=COLOR_PRIMARIO,
                                  activeforeground=COLOR_TEXTO_CLARO)
        self.boton_menu.pack(side="top", fill="x", pady=(0, 20))

        # Frame para los botones del menú
        self.frame_botones = tk.Frame(self, bg=COLOR_PRIMARIO)
        self.frame_botones.pack(fill="x", pady=10)

        # Botones del menú con iconos
        botones = [
            ("Ingresos", "ingresos", "💰"),
            ("Egresos", "egresos", "💸"),
            ("Tarjetas", "tarjetas", "💳"),
            ("Resumen", "resumen", "📊"),
            ("Configuración", "config", "⚙️")
        ]

        for texto, comando, icono in botones:
            btn = tk.Button(self.frame_botones, text=f" {icono} {texto}",
                          command=lambda c=comando: self.controller.mostrar_seccion(c),
                          bg=COLOR_PRIMARIO, fg=COLOR_TEXTO_CLARO, font=FUENTE_BOTONES,
                          width=15, height=2, relief="flat", anchor="w",
                          activebackground="#34495e", activeforeground=COLOR_TEXTO_CLARO,
                          bd=0, padx=10)
            btn.pack(pady=2, fill="x")

        # Botón de cerrar sesión al final
        tk.Button(self.frame_botones, text=" 🔒 Cerrar Sesión",
                command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                bg="#c0392b", fg=COLOR_TEXTO_CLARO, font=FUENTE_BOTONES,
                width=15, height=2, relief="flat", anchor="w",
                activebackground="#e74c3c", activeforeground=COLOR_TEXTO_CLARO,
                bd=0, padx=10).pack(pady=(20, 0), fill="x")

    def toggle_menu(self):
        if self.frame_botones.winfo_ismapped():
            self.frame_botones.pack_forget()
            self.config(width=70)
        else:
            self.frame_botones.pack(fill="x", pady=10)
            self.config(width=250)

# Ventana principal de la aplicación mejorada
class VentanaPrincipal(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.id_usuario = "JU001"  # Este ID debería venir del login

        frame_principal = tk.Frame(self)
        frame_principal.pack(fill="both", expand=True)

        self.menu = MenuLateral(frame_principal, self)
        self.menu.pack(side="left", fill="y")

        self.area_contenido = tk.Frame(frame_principal, bg=COLOR_FONDO)
        self.area_contenido.pack(side="right", fill="both", expand=True)

        self.secciones = {}
        
        self.crear_seccion_bienvenida()
        self.crear_seccion_ingresos()
        self.crear_seccion_egresos()
        self.crear_seccion_tarjetas()
        self.crear_seccion_resumen()
        self.crear_seccion_config()

        self.mostrar_seccion("bienvenida")

    def crear_seccion_bienvenida(self):
        frame = tk.Frame(self.area_contenido, bg=COLOR_FONDO, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Frame superior para el saludo
        frame_saludo = tk.Frame(frame, bg="white", padx=30, pady=30, 
                              relief="solid", borderwidth=0,
                              highlightbackground="#bdc3c7", highlightthickness=1)
        frame_saludo.pack(fill="x", pady=(0, 30))

        tk.Label(frame_saludo, text="¡Bienvenido a MyEconomy!", 
                font=FUENTE_TITULOS, 
                fg=COLOR_PRIMARIO, bg="white").pack(anchor="w")

        tk.Label(frame_saludo, text="Gestiona tus finanzas de manera inteligente", 
                font=FUENTE_SUBTITULOS, 
                fg="#7f8c8d", bg="white").pack(anchor="w", pady=(10,0))

        # Frame para mostrar las tarjetas
        frame_tarjetas = tk.Frame(frame, bg=COLOR_FONDO)
        frame_tarjetas.pack(fill="both", expand=True)

        tk.Label(frame_tarjetas, text="Mis Tarjetas de Crédito", 
                font=FUENTE_TITULOS, 
                fg=COLOR_PRIMARIO, bg=COLOR_FONDO).pack(anchor="w", pady=(0,20))

        # Frame contenedor para las tarjetas
        self.contenedor_tarjetas = tk.Frame(frame_tarjetas, bg=COLOR_FONDO)
        self.contenedor_tarjetas.pack(fill="both", expand=True)

        self.actualizar_tarjetas_bienvenida()

        self.secciones["bienvenida"] = frame

    def actualizar_tarjetas_bienvenida(self):
        # Limpiar tarjetas existentes
        for widget in self.contenedor_tarjetas.winfo_children():
            widget.destroy()

        # Obtener tarjetas del usuario
        tarjetas = obtener_tarjetas_usuario(self.id_usuario)
        
        if not tarjetas:
            tk.Label(self.contenedor_tarjetas, text="No tienes tarjetas registradas", 
                    font=FUENTE_SUBTITULOS, fg="#7f8c8d", bg=COLOR_FONDO).pack(pady=50)
            return
        
        # Frame para contener las filas de tarjetas
        frame_filas = tk.Frame(self.contenedor_tarjetas, bg=COLOR_FONDO)
        frame_filas.pack(fill="both", expand=True)
        
        # Mostrar tarjetas en filas de 2
        for i in range(0, len(tarjetas), 2):
            frame_fila = tk.Frame(frame_filas, bg=COLOR_FONDO)
            frame_fila.pack(fill="x", pady=10)
            
            # Primera tarjeta de la fila
            if i < len(tarjetas):
                self.crear_tarjeta_ui(frame_fila, tarjetas[i], i % 2 == 0)
            
            # Segunda tarjeta de la fila
            if i + 1 < len(tarjetas):
                self.crear_tarjeta_ui(frame_fila, tarjetas[i+1], False)

    def crear_tarjeta_ui(self, parent, tarjeta, is_first=True):
        """Crea una UI de tarjeta de crédito con estilo"""
        padx = (0, 10) if is_first else (10, 0)
        
        frame_tarjeta = tk.Frame(parent, bg=COLOR_SECUNDARIO, 
                               relief="solid", borderwidth=0,
                               highlightbackground="#bdc3c7", highlightthickness=1)
        frame_tarjeta.pack(side="left", fill="both", expand=True, padx=padx, pady=5)
        
        # Contenido de la tarjeta
        tk.Label(frame_tarjeta, text=tarjeta['banco'],
                font=("Helvetica", 16, "bold"),
                bg=COLOR_SECUNDARIO, fg="white").pack(anchor="w", padx=20, pady=(20,5))
        
        tk.Label(frame_tarjeta, text=tarjeta['numero'],
                font=("Helvetica", 14),
                bg=COLOR_SECUNDARIO, fg="white").pack(anchor="w", padx=20, pady=(0,5))
        
        tk.Label(frame_tarjeta, text=f"Límite: ${tarjeta['limite']}",
                font=("Helvetica", 12),
                bg=COLOR_SECUNDARIO, fg="white").pack(anchor="w", padx=20, pady=(0,5))
        
        tk.Label(frame_tarjeta, text=f"Fecha de corte: {tarjeta['fecha_corte']}",
                font=("Helvetica", 12),
                bg=COLOR_SECUNDARIO, fg="white").pack(anchor="w", padx=20, pady=(0,20))

    def crear_seccion_ingresos(self):
        frame = tk.Frame(self.area_contenido, bg=COLOR_FONDO, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(frame, text="Registro de Ingresos", 
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg=COLOR_FONDO).pack(pady=(0, 30))

        # Frame para el formulario
        form_frame = tk.Frame(frame, padx=30, pady=30, 
                            relief="solid", borderwidth=0, bg="white",
                            highlightbackground="#bdc3c7", highlightthickness=1)
        form_frame.pack(fill="x", pady=20)

        tk.Label(form_frame, text="Nuevo Ingreso", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(anchor="w", pady=(0, 20))

        # Campos del formulario
        self.descripcion_ingreso = tk.StringVar()
        self.monto_ingreso = tk.StringVar()
        
        self.crear_campo_formulario(form_frame, "Descripción:", self.descripcion_ingreso)
        self.crear_campo_formulario(form_frame, "Monto:", self.monto_ingreso)

        # Botón de registro
        tk.Button(form_frame, text="Registrar Ingreso", 
                 command=self.registrar_ingreso,
                 bg=COLOR_CUARTO, fg="white", font=FUENTE_BOTONES,
                 width=20, height=2, bd=0, activebackground="#27ae60",
                 activeforeground="white").pack(pady=20)

        # Frame para la lista de ingresos
        lista_frame = tk.Frame(frame, padx=30, pady=30,
                             relief="solid", borderwidth=0, bg="white",
                             highlightbackground="#bdc3c7", highlightthickness=1)
        lista_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(lista_frame, text="Historial de Ingresos", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(pady=(0, 20))

        # Crear un frame para los encabezados
        headers_frame = tk.Frame(lista_frame, bg="white")
        headers_frame.pack(fill="x", padx=10)

        # Encabezados
        tk.Label(headers_frame, text="Fecha", width=20, 
                font=FUENTE_BOTONES, fg=COLOR_PRIMARIO, 
                bg="white").pack(side="left")
        tk.Label(headers_frame, text="Descripción", width=30,
                font=FUENTE_BOTONES, fg=COLOR_PRIMARIO,
                bg="white").pack(side="left")
        tk.Label(headers_frame, text="Monto", width=15,
                font=FUENTE_BOTONES, fg=COLOR_PRIMARIO,
                bg="white").pack(side="left")

        # Lista de ingresos
        self.lista_ingresos = tk.Frame(lista_frame, bg="white")
        self.lista_ingresos.pack(fill="both", expand=True, pady=10)

        # Scrollbar y Canvas para la lista
        self.canvas_ingresos = tk.Canvas(self.lista_ingresos, bg="white", 
                                       highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.lista_ingresos, orient="vertical", 
                               command=self.canvas_ingresos.yview)
        self.frame_ingresos_scroll = tk.Frame(self.canvas_ingresos, bg="white")

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
        frame = tk.Frame(self.area_contenido, bg=COLOR_FONDO, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(frame, text="Registro de Egresos", 
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg=COLOR_FONDO).pack(pady=(0, 30))

        # Frame para el formulario
        form_frame = tk.Frame(frame, padx=30, pady=30, 
                            relief="solid", borderwidth=0, bg="white",
                            highlightbackground="#bdc3c7", highlightthickness=1)
        form_frame.pack(fill="x", pady=20)

        tk.Label(form_frame, text="Nuevo Egreso", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(anchor="w", pady=(0, 20))

        # Campos del formulario
        self.descripcion_egreso = tk.StringVar()
        self.monto_egreso = tk.StringVar()
        
        self.crear_campo_formulario(form_frame, "Descripción:", self.descripcion_egreso)
        self.crear_campo_formulario(form_frame, "Monto:", self.monto_egreso)

        # Botón de registro
        tk.Button(form_frame, text="Registrar Egreso", 
                 command=self.registrar_egreso,
                 bg=COLOR_TERCIARIO, fg="white", font=FUENTE_BOTONES,
                 width=20, height=2, bd=0, activebackground="#c0392b",
                 activeforeground="white").pack(pady=20)

        # Frame para la lista de egresos
        lista_frame = tk.Frame(frame, padx=30, pady=30,
                             relief="solid", borderwidth=0, bg="white",
                             highlightbackground="#bdc3c7", highlightthickness=1)
        lista_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(lista_frame, text="Historial de Egresos", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(pady=(0, 20))

        # Crear un frame para los encabezados
        headers_frame = tk.Frame(lista_frame, bg="white")
        headers_frame.pack(fill="x", padx=10)

        # Encabezados
        tk.Label(headers_frame, text="Fecha", width=20, 
                font=FUENTE_BOTONES, fg=COLOR_PRIMARIO, 
                bg="white").pack(side="left")
        tk.Label(headers_frame, text="Descripción", width=30,
                font=FUENTE_BOTONES, fg=COLOR_PRIMARIO,
                bg="white").pack(side="left")
        tk.Label(headers_frame, text="Monto", width=15,
                font=FUENTE_BOTONES, fg=COLOR_PRIMARIO,
                bg="white").pack(side="left")

        # Lista de egresos
        self.lista_egresos = tk.Frame(lista_frame, bg="white")
        self.lista_egresos.pack(fill="both", expand=True, pady=10)

        # Scrollbar y Canvas para la lista
        self.canvas_egresos = tk.Canvas(self.lista_egresos, bg="white",
                                      highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.lista_egresos, orient="vertical",
                               command=self.canvas_egresos.yview)
        self.frame_egresos_scroll = tk.Frame(self.canvas_egresos, bg="white")

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
        frame = tk.Frame(self.area_contenido, bg=COLOR_FONDO, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(frame, text="Gestión de Tarjetas", 
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg=COLOR_FONDO).pack(pady=(0, 30))

        # Frame para el formulario
        form_frame = tk.Frame(frame, padx=30, pady=30, 
                            relief="solid", borderwidth=0, bg="white",
                            highlightbackground="#bdc3c7", highlightthickness=1)
        form_frame.pack(fill="x", pady=20)

        tk.Label(form_frame, text="Nueva Tarjeta", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(anchor="w", pady=(0, 20))

        # Campos del formulario
        self.banco_tarjeta = tk.StringVar()
        self.limite_tarjeta = tk.StringVar()
        self.corte_tarjeta = tk.StringVar()
        
        self.crear_campo_formulario(form_frame, "Banco:", self.banco_tarjeta)
        self.crear_campo_formulario(form_frame, "Límite:", self.limite_tarjeta)
        self.crear_campo_formulario(form_frame, "Fecha de Corte:", self.corte_tarjeta)

        # Botón de registro
        tk.Button(form_frame, text="Agregar Tarjeta", 
                 command=self.agregar_tarjeta,
                 bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                 width=20, height=2, bd=0, activebackground="#2980b9",
                 activeforeground="white").pack(pady=20)

        # Frame para la lista de tarjetas
        lista_frame = tk.Frame(frame, padx=30, pady=30,
                             relief="solid", borderwidth=0, bg="white",
                             highlightbackground="#bdc3c7", highlightthickness=1)
        lista_frame.pack(fill="both", expand=True, pady=20)

        tk.Label(lista_frame, text="Mis Tarjetas", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(pady=(0, 20))

        # Crear Treeview para mostrar las tarjetas
        self.tree_tarjetas = ttk.Treeview(lista_frame, columns=("banco", "limite", "corte"), show="headings")
        
        # Configurar columnas
        self.tree_tarjetas.heading("banco", text="Banco")
        self.tree_tarjetas.heading("limite", text="Límite")
        self.tree_tarjetas.heading("corte", text="Fecha de Corte")
        
        self.tree_tarjetas.column("banco", width=200)
        self.tree_tarjetas.column("limite", width=150, anchor="e")
        self.tree_tarjetas.column("corte", width=150, anchor="center")
        
        # Añadir scrollbar
        scrollbar = ttk.Scrollbar(lista_frame, orient="vertical", command=self.tree_tarjetas.yview)
        self.tree_tarjetas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.tree_tarjetas.pack(fill="both", expand=True)

        self.actualizar_lista_tarjetas()

        self.secciones["tarjetas"] = frame

    def crear_seccion_resumen(self):
        frame = tk.Frame(self.area_contenido, bg=COLOR_FONDO, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(frame, text="Resumen Financiero", 
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg=COLOR_FONDO).pack(pady=(0, 30))

        # Frame para el contenido
        content_frame = tk.Frame(frame, padx=30, pady=30, 
                               relief="solid", borderwidth=0, bg="white",
                               highlightbackground="#bdc3c7", highlightthickness=1)
        content_frame.pack(fill="both", expand=True)

        # Obtener datos para el resumen
        ingresos = obtener_transacciones_usuario(self.id_usuario, "ingreso")
        egresos = obtener_transacciones_usuario(self.id_usuario, "egreso")
        
        total_ingresos = sum(float(t['monto']) for t in ingresos)
        total_egresos = sum(float(t['monto']) for t in egresos)
        balance = total_ingresos - total_egresos
        
        # Crear métricas
        self.crear_metrica(content_frame, "Total Ingresos", f"${total_ingresos:,.2f}", COLOR_CUARTO, 0)
        self.crear_metrica(content_frame, "Total Egresos", f"${total_egresos:,.2f}", COLOR_TERCIARIO, 1)
        self.crear_metrica(content_frame, "Balance", f"${balance:,.2f}", 
                          COLOR_SECUNDARIO if balance >= 0 else COLOR_TERCIARIO, 2)

        # Gráfico de barras simple (simulado)
        chart_frame = tk.Frame(content_frame, bg="white")
        chart_frame.grid(row=3, column=0, columnspan=3, pady=(30, 0), sticky="nsew")
        
        tk.Label(chart_frame, text="Distribución de Gastos", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(pady=(0, 20))
        
        # Simular un gráfico con frames coloreados
        if egresos:
            # Agrupar gastos por categoría (simulado)
            categorias = {
                "Comida": 0,
                "Transporte": 0,
                "Entretenimiento": 0,
                "Servicios": 0,
                "Otros": 0
            }
            
            for egreso in egresos:
                desc = egreso['descripcion'].lower()
                if "comida" in desc or "restaurante" in desc or "super" in desc:
                    categorias["Comida"] += float(egreso['monto'])
                elif "transporte" in desc or "taxi" in desc or "gasolina" in desc:
                    categorias["Transporte"] += float(egreso['monto'])
                elif "cine" in desc or "netflix" in desc or "entretenimiento" in desc:
                    categorias["Entretenimiento"] += float(egreso['monto'])
                elif "luz" in desc or "agua" in desc or "internet" in desc:
                    categorias["Servicios"] += float(egreso['monto'])
                else:
                    categorias["Otros"] += float(egreso['monto'])
            
            # Crear barras para cada categoría
            max_val = max(categorias.values()) if max(categorias.values()) > 0 else 1
            
            for i, (categoria, valor) in enumerate(categorias.items()):
                if valor == 0:
                    continue
                    
                row_frame = tk.Frame(chart_frame, bg="white")
                row_frame.pack(fill="x", pady=5)
                
                tk.Label(row_frame, text=categoria, width=15, 
                        font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white",
                        anchor="w").pack(side="left")
                
                # Barra de progreso
                bar_width = int((valor / max_val) * 200)
                bar_color = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"][i % 5]
                
                bar_frame = tk.Frame(row_frame, bg="#ecf0f1", height=20, width=200)
                bar_frame.pack(side="left", padx=10)
                tk.Frame(bar_frame, bg=bar_color, height=20, width=bar_width).pack(side="left", anchor="w")
                
                tk.Label(row_frame, text=f"${valor:,.2f}", 
                        font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white").pack(side="left", padx=10)
        else:
            tk.Label(chart_frame, text="No hay datos de gastos para mostrar", 
                    font=FUENTE_TEXTO, fg="#7f8c8d", bg="white").pack(pady=20)

        self.secciones["resumen"] = frame

    def crear_seccion_config(self):
        frame = tk.Frame(self.area_contenido, bg=COLOR_FONDO, padx=40, pady=40)
        frame.pack(fill="both", expand=True)

        # Título
        tk.Label(frame, text="Configuración", 
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg=COLOR_FONDO).pack(pady=(0, 30))

        # Frame para el contenido
        content_frame = tk.Frame(frame, padx=30, pady=30, 
                               relief="solid", borderwidth=0, bg="white",
                               highlightbackground="#bdc3c7", highlightthickness=1)
        content_frame.pack(fill="both", expand=True)

        # Configuración de tema
        tk.Label(content_frame, text="Tema de la aplicación", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(anchor="w", pady=(0, 10))

        theme_frame = tk.Frame(content_frame, bg="white")
        theme_frame.pack(fill="x", pady=10)

        themes = [
            ("Claro", COLOR_FONDO, COLOR_PRIMARIO),
            ("Oscuro", "#2c3e50", "#ecf0f1"),
            ("Azul", "#3498db", "#ecf0f1"),
            ("Verde", "#27ae60", "#ecf0f1")
        ]

        for name, bg, fg in themes:
            btn = tk.Button(theme_frame, text=name, 
                          command=lambda b=bg, f=fg: self.cambiar_tema(b, f),
                          bg=bg, fg=fg, font=FUENTE_TEXTO,
                          width=10, height=2, bd=0)
            btn.pack(side="left", padx=5)

        # Configuración de notificaciones
        tk.Label(content_frame, text="Notificaciones", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(anchor="w", pady=(20, 10))

        notif_frame = tk.Frame(content_frame, bg="white")
        notif_frame.pack(fill="x", pady=10)

        self.notif_var = tk.IntVar(value=1)
        tk.Checkbutton(notif_frame, text="Recibir notificaciones", 
                      variable=self.notif_var, font=FUENTE_TEXTO,
                      fg=COLOR_TEXTO, bg="white", selectcolor=COLOR_FONDO).pack(anchor="w")

        # Botón de guardar configuración
        tk.Button(content_frame, text="Guardar Configuración", 
                 command=self.guardar_configuracion,
                 bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                 width=20, height=2, bd=0, activebackground="#2980b9",
                 activeforeground="white").pack(pady=30)

        self.secciones["config"] = frame

    def crear_campo_formulario(self, frame, texto, variable):
        """Crea un campo de formulario con estilo consistente"""
        field_frame = tk.Frame(frame, bg="white")
        field_frame.pack(fill="x", pady=10)
        
        tk.Label(field_frame, text=texto, bg="white", fg=COLOR_TEXTO,
                font=FUENTE_TEXTO, anchor="w").pack(side="left", padx=(0, 10))
        
        entry = tk.Entry(field_frame, textvariable=variable, font=FUENTE_TEXTO, width=30, bd=1, relief="solid",
                        highlightbackground="#bdc3c7", highlightthickness=1)
        entry.pack(side="right", expand=True, fill="x")
        return entry

    def crear_metrica(self, parent, titulo, valor, color, columna):
        """Crea una tarjeta de métrica visual"""
        metric_frame = tk.Frame(parent, bg=color, padx=20, pady=20,
                              relief="solid", borderwidth=0)
        metric_frame.grid(row=0, column=columna, padx=10, sticky="nsew")
        
        tk.Label(metric_frame, text=titulo, 
                font=FUENTE_TEXTO, fg="white", bg=color).pack(anchor="w")
        
        tk.Label(metric_frame, text=valor, 
                font=("Helvetica", 24, "bold"), fg="white", bg=color).pack(anchor="w", pady=(10,0))
        
        parent.columnconfigure(columna, weight=1)

    def mostrar_seccion(self, nombre_seccion):
        for seccion in self.secciones.values():
            seccion.pack_forget()
        
        self.secciones[nombre_seccion].pack(fill="both", expand=True)
        
        if nombre_seccion == "tarjetas":
            self.actualizar_lista_tarjetas()
        elif nombre_seccion == "resumen":
            # Actualizar datos del resumen cada vez que se muestra
            frame = self.secciones["resumen"]
            for widget in frame.winfo_children():
                widget.destroy()
            self.crear_seccion_resumen()

    def actualizar_lista_ingresos(self):
        # Limpiar lista actual
        for widget in self.frame_ingresos_scroll.winfo_children():
            widget.destroy()

        # Obtener ingresos del usuario
        ingresos = obtener_transacciones_usuario(self.id_usuario, "ingreso")
        
        # Mostrar cada ingreso
        for i, ingreso in enumerate(ingresos):
            bg_color = "#f5f5f5" if i % 2 == 0 else "white"
            
            frame_item = tk.Frame(self.frame_ingresos_scroll, bg=bg_color)
            frame_item.pack(fill="x", pady=1)
            
            tk.Label(frame_item, text=ingreso['fecha'], width=20,
                    font=FUENTE_TEXTO, fg=COLOR_TEXTO,
                    bg=bg_color).pack(side="left", padx=5)
            tk.Label(frame_item, text=ingreso['descripcion'], width=30,
                    font=FUENTE_TEXTO, fg=COLOR_TEXTO,
                    bg=bg_color).pack(side="left", padx=5)
            tk.Label(frame_item, text=f"${float(ingreso['monto']):,.2f}", width=15,
                    font=FUENTE_TEXTO, fg=COLOR_CUARTO,
                    bg=bg_color).pack(side="left", padx=5)

    def actualizar_lista_egresos(self):
        # Limpiar lista actual
        for widget in self.frame_egresos_scroll.winfo_children():
            widget.destroy()

        # Obtener egresos del usuario
        egresos = obtener_transacciones_usuario(self.id_usuario, "egreso")
        
        # Mostrar cada egreso
        for i, egreso in enumerate(egresos):
            bg_color = "#f5f5f5" if i % 2 == 0 else "white"
            
            frame_item = tk.Frame(self.frame_egresos_scroll, bg=bg_color)
            frame_item.pack(fill="x", pady=1)
            
            tk.Label(frame_item, text=egreso['fecha'], width=20,
                    font=FUENTE_TEXTO, fg=COLOR_TEXTO,
                    bg=bg_color).pack(side="left", padx=5)
            tk.Label(frame_item, text=egreso['descripcion'], width=30,
                    font=FUENTE_TEXTO, fg=COLOR_TEXTO,
                    bg=bg_color).pack(side="left", padx=5)
            tk.Label(frame_item, text=f"${float(egreso['monto']):,.2f}", width=15,
                    font=FUENTE_TEXTO, fg=COLOR_TERCIARIO,
                    bg=bg_color).pack(side="left", padx=5)

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
                self.descripcion_ingreso.set("")
                self.monto_ingreso.set("")
                self.actualizar_lista_ingresos()
                
                # Actualizar el resumen si está visible
                if "resumen" in self.secciones and self.secciones["resumen"].winfo_ismapped():
                    frame = self.secciones["resumen"]
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.crear_seccion_resumen()
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
                self.descripcion_egreso.set("")
                self.monto_egreso.set("")
                self.actualizar_lista_egresos()
                
                # Actualizar el resumen si está visible
                if "resumen" in self.secciones and self.secciones["resumen"].winfo_ismapped():
                    frame = self.secciones["resumen"]
                    for widget in frame.winfo_children():
                        widget.destroy()
                    self.crear_seccion_resumen()
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
                self.banco_tarjeta.set("")
                self.limite_tarjeta.set("")
                self.corte_tarjeta.set("")
                self.actualizar_lista_tarjetas()
                self.actualizar_tarjetas_bienvenida()
            else:
                messagebox.showerror("Error", "No se pudo agregar la tarjeta")
        except ValueError:
            messagebox.showerror("Error", "El límite debe ser un número válido")

    def actualizar_lista_tarjetas(self):
        # Limpiar lista actual
        for item in self.tree_tarjetas.get_children():
            self.tree_tarjetas.delete(item)
            
        # Obtener tarjetas del usuario
        tarjetas = obtener_tarjetas_usuario(self.id_usuario)
        
        # Agregar tarjetas al Treeview
        for tarjeta in tarjetas:
            self.tree_tarjetas.insert("", "end", values=(
                tarjeta['banco'],
                f"${float(tarjeta['limite']):,.2f}",
                tarjeta['fecha_corte']
            ))

    def cambiar_tema(self, bg_color, fg_color):
        """Cambia el tema de la aplicación"""
        global COLOR_FONDO, COLOR_TEXTO
        COLOR_FONDO = bg_color
        COLOR_TEXTO = fg_color
        
        # Actualizar colores en todas las secciones
        for seccion in self.secciones.values():
            seccion.config(bg=COLOR_FONDO)
            for widget in seccion.winfo_children():
                if isinstance(widget, tk.Frame):
                    widget.config(bg=COLOR_FONDO)
        
        messagebox.showinfo("Tema cambiado", "El tema se aplicará completamente al reiniciar la aplicación")

    def guardar_configuracion(self):
        """Guarda la configuración del usuario"""
        # Aquí podrías guardar las preferencias en un archivo
        messagebox.showinfo("Configuración guardada", "Tus preferencias han sido guardadas")

class VentanaRegistro(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Frame principal
        frame_principal = tk.Frame(self, bg=COLOR_FONDO, bd=0)
        frame_principal.place(relx=0.5, rely=0.5, anchor="center")

        # Frame del formulario con efecto de tarjeta
        frame_form = tk.Frame(frame_principal, bg="white", padx=40, pady=40, 
                            relief="solid", borderwidth=0, 
                            highlightbackground="#bdc3c7", highlightthickness=1)
        frame_form.pack(pady=20, padx=20)

        # Logo de la aplicación
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((100, 100), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(frame_form, image=self.logo, bg="white").grid(row=0, column=0, columnspan=2, pady=(0, 20))
        except:
            pass

        # Título
        tk.Label(frame_form, text="Registro de Usuario", bg="white", fg=COLOR_PRIMARIO,
                font=FUENTE_TITULOS).grid(row=1, column=0, columnspan=2, pady=(0, 30))

        # Campos del formulario
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.fecha_nacimiento = tk.StringVar()
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()
        
        self.crear_campo(frame_form, "Nombre:", 2, self.nombre)
        self.crear_campo(frame_form, "Apellido:", 3, self.apellido)
        self.crear_campo(frame_form, "Fecha de Nacimiento:", 4, self.fecha_nacimiento)
        self.crear_campo(frame_form, "Usuario:", 5, self.usuario)
        self.crear_campo(frame_form, "Contraseña:", 6, self.password, show="*")

        # Botón de registro
        btn_registro = tk.Button(frame_form, text="Registrar", command=self.registrar_usuario,
                               bg=COLOR_CUARTO, fg="white", font=FUENTE_BOTONES,
                               width=20, height=2, bd=0, activebackground="#27ae60",
                               activeforeground="white")
        btn_registro.grid(row=7, column=0, columnspan=2, pady=(20, 10))

        # Botón para volver
        btn_volver = tk.Button(frame_principal, text="Volver", 
                              command=lambda: self.controller.mostrar_ventana("VentanaInicio"),
                              bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                              width=20, height=2, bd=0, activebackground="#2980b9",
                              activeforeground="white")
        btn_volver.pack(pady=(0, 20))

    def crear_campo(self, frame, texto, fila, variable, show=None):
        """Crea un campo de entrada con estilo consistente"""
        tk.Label(frame, text=texto, bg="white", fg=COLOR_TEXTO,
                font=FUENTE_SUBTITULOS, anchor="w").grid(row=fila, column=0, pady=(10, 5), padx=10, sticky="ew")
        
        entry = tk.Entry(frame, textvariable=variable, font=FUENTE_TEXTO, width=25, bd=1, relief="solid",
                        highlightbackground="#bdc3c7", highlightthickness=1)
        if show:
            entry.config(show=show)
        entry.grid(row=fila, column=1, pady=(10, 5), padx=10)
        return entry

    def registrar_usuario(self):
        nombre = self.nombre.get().strip()
        apellido = self.apellido.get().strip()
        fecha_nacimiento = self.fecha_nacimiento.get().strip()
        usuario = self.usuario.get().strip()
        contrasena = self.password.get().strip()

        if not (nombre and apellido and fecha_nacimiento and usuario and contrasena):
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            id_usuario = registrar_usuario(nombre, apellido, fecha_nacimiento, usuario, contrasena)
            messagebox.showinfo("Éxito", f"Usuario registrado con éxito. ID: {id_usuario}")
            self.nombre.set("")
            self.apellido.set("")
            self.fecha_nacimiento.set("")
            self.usuario.set("")
            self.password.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al registrar el usuario: {str(e)}")

class PantallaInicio(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="white")
        
        # Frame para centrar el contenido
        center_frame = tk.Frame(self, bg="white")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((300, 300), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            tk.Label(center_frame, image=self.logo, bg="white").pack()
        except FileNotFoundError:
            tk.Label(center_frame, text="MYECONOMY", bg="white", 
                    font=("Helvetica", 48, "bold"), fg=COLOR_PRIMARIO).pack()
        
        # Texto de carga
        tk.Label(center_frame, text="Cargando aplicación...", bg="white", 
                font=FUENTE_SUBTITULOS, fg="#7f8c8d").pack(pady=20)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(center_frame, orient="horizontal", 
                                      length=300, mode="determinate")
        self.progress.pack(pady=10)
        self.progress.start()
        
        self.after(3000, lambda: controller.mostrar_ventana("VentanaInicio"))

class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.state("zoomed")

        # Configurar el icono de la aplicación
        try:
            icon_path = os.path.join("datos", "imagenes", "icono.ico")
            self.iconbitmap(icon_path)
        except:
            pass

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
    # Inicializar archivos necesarios
    inicializar_archivos()
    
    # Crear directorio de imágenes si no existe
    if not os.path.exists(os.path.join("datos", "imagenes")):
        os.makedirs(os.path.join("datos", "imagenes"))
    
    app = MyEconomyApp()
    app.mainloop()