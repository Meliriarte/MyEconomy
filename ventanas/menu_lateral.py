import tkinter as tk
import os
from PIL import Image, ImageTk
from .ventana_base import VentanaBase

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

class MenuLateral(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=COLOR_PRIMARIO, width=250)  # Ancho inicial amplio para mostrar todo el menú
        self.pack_propagate(False)
        
        try:
            logo_img = Image.open(os.path.join("datos", "imagenes", "logo1.png"))
            logo_img = logo_img.resize((40, 40), Image.Resampling.LANCZOS)
            self.logo_pequeno = ImageTk.PhotoImage(logo_img)
            logo_button = tk.Button(self, image=self.logo_pequeno, bg=COLOR_PRIMARIO,
                                   command=lambda: self.controller.mostrar_seccion("bienvenida"),
                                   relief="flat", bd=0, activebackground=COLOR_PRIMARIO,
                                   cursor="hand2")
            logo_button.pack(pady=20)
        except:
            pass

        self.boton_menu = tk.Button(self, text="☰", command=self.toggle_menu,
                                  bg=COLOR_PRIMARIO, fg=COLOR_TEXTO_CLARO, font=("Arial", 18),
                                  relief="flat", bd=0, activebackground=COLOR_PRIMARIO,
                                  activeforeground=COLOR_TEXTO_CLARO)
        self.boton_menu.pack(side="top", fill="x", pady=(0, 20))

        self.frame_botones = tk.Frame(self, bg=COLOR_PRIMARIO)
        self.frame_botones.pack(fill="x", pady=10)

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

        # Botón de cerrar sesión con menú de confirmación
        self.boton_cerrar_sesion = tk.Button(self.frame_botones, text=" 🔒 Cerrar Sesión",
                command=self.mostrar_confirmacion_cierre,
                bg="#c0392b", fg=COLOR_TEXTO_CLARO, font=FUENTE_BOTONES,
                width=15, height=2, relief="flat", anchor="w",
                activebackground="#e74c3c", activeforeground=COLOR_TEXTO_CLARO,
                bd=0, padx=10)
        self.boton_cerrar_sesion.pack(pady=(20, 0), fill="x")
        
        # Crear frame para el menú de confirmación (inicialmente oculto) - ahora es hijo de winfo_toplevel()
        self.frame_confirmacion = tk.Frame(self.winfo_toplevel(), bg="white", bd=2, relief="groove")
        
        # Título con líneas decorativas
        titulo_frame = tk.Frame(self.frame_confirmacion, bg="white")
        titulo_frame.pack(fill="x", pady=(20, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_TERCIARIO).pack(fill="x", pady=(0, 10))
        tk.Label(titulo_frame, text="¿Cerrar sesión?", 
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_TERCIARIO).pack(fill="x", pady=(10, 0))
        
        # Frame para los botones
        frame_botones_confirmacion = tk.Frame(self.frame_confirmacion, bg="white")
        frame_botones_confirmacion.pack(fill="x", expand=True, pady=20)
        
        # Botones exactamente del mismo tamaño y centrados
        botones_center = tk.Frame(frame_botones_confirmacion, bg="white")
        botones_center.pack(anchor="center")
        
        # Crear primero los botones de texto igual
        self.btn_si = tk.Button(botones_center, text="Sí", 
                command=self.cerrar_sesion,
                bg=COLOR_TERCIARIO, fg="white", 
                font=FUENTE_TEXTO,
                bd=1, 
                relief="raised", 
                padx=20, 
                pady=8,
                width=6)  # Ancho reducido para que ambos botones tengan el mismo tamaño visual
        
        self.btn_no = tk.Button(botones_center, text="No", 
                command=self.ocultar_confirmacion_cierre,
                bg=COLOR_PRIMARIO, fg="white", 
                font=FUENTE_TEXTO,
                bd=1, 
                relief="raised", 
                padx=20, 
                pady=8,
                width=6)  # Mismo ancho que el botón Sí
        
        # Empaquetar botones en orden
        self.btn_si.pack(side="left", padx=20)
        self.btn_no.pack(side="left", padx=20)
        
        # Estado inicial del menú (expandido)
        self.menu_expandido = True

    def mostrar_confirmacion_cierre(self):
        """Muestra el menú de confirmación de cierre de sesión"""
        # Calcular posición del menú (centrado en la ventana principal)
        self.update_idletasks()  # Asegurarse de que las dimensiones son correctas
        
        # Obtener dimensiones y posición de la ventana principal
        main_window = self.winfo_toplevel()
        main_width = main_window.winfo_width()
        main_height = main_window.winfo_height()
        
        # Tamaño del menú de confirmación
        ancho_menu = 300
        alto_menu = 200
        
        # Centrar en la ventana principal
        x = (main_width - ancho_menu) // 2
        y = (main_height - alto_menu) // 2
        
        # Posicionar y mostrar el menú de confirmación
        self.frame_confirmacion.place(x=x, y=y, width=ancho_menu, height=alto_menu)
        
        # Traer al frente
        self.frame_confirmacion.lift()
    
    def ocultar_confirmacion_cierre(self):
        """Oculta el menú de confirmación de cierre de sesión"""
        self.frame_confirmacion.place_forget()
    
    def cerrar_sesion(self):
        """Cierra la sesión y limpia los campos del formulario de inicio"""
        # Ocultar confirmación primero
        self.ocultar_confirmacion_cierre()
        
        # Cerrar sesión (navegar a ventana de inicio)
        app = self.controller.controller
        
        # Limpiar campos de inicio de sesión si existen
        if "VentanaInicio" in app.frames:
            ventana_inicio = app.frames["VentanaInicio"]
            # Si tienen atributos de usuario y contraseña, limpiarlos
            if hasattr(ventana_inicio, 'usuario'):
                ventana_inicio.usuario.set("")
            if hasattr(ventana_inicio, 'password'):
                ventana_inicio.password.set("")
        
        # Mostrar ventana de inicio
        app.mostrar_ventana("VentanaInicio")

    def toggle_menu(self):
        if self.menu_expandido:
            self.frame_botones.pack_forget()
            self.config(width=70)
            self.menu_expandido = False
        else:
            self.frame_botones.pack(fill="x", pady=10)
            self.config(width=250)
            self.menu_expandido = True