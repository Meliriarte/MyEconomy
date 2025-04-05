import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime
from .ventana_base import VentanaBase
from .menu_lateral import MenuLateral
from funciones import obtener_tarjetas_usuario, obtener_transacciones_usuario, registrar_transaccion, registrar_tarjeta

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

class VentanaPrincipal(VentanaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.id_usuario = "JU001"  # Este ID debería venir del login

        # Frame principal con tamaño fijo
        self.main_container = tk.Frame(self, bg=COLOR_FONDO)
        self.main_container.pack(fill="both", expand=True)
        self.main_container.pack_propagate(False)

        # Menú lateral
        self.menu = MenuLateral(self.main_container, self)
        self.menu.pack(side="left", fill="y")

        # Área de contenido principal
        self.content_area = tk.Frame(self.main_container, bg=COLOR_FONDO)
        self.content_area.pack(side="right", fill="both", expand=True)
        self.content_area.pack_propagate(False)

        # Diccionario para almacenar las secciones
        self.secciones = {}
        
        # Crear todas las secciones
        self.crear_seccion_bienvenida()
        self.crear_seccion_ingresos()
        self.crear_seccion_egresos()
        self.crear_seccion_tarjetas()
        self.crear_seccion_resumen()
        self.crear_seccion_config()

        # Mostrar sección inicial
        self.mostrar_seccion("bienvenida")

    def mostrar_seccion(self, nombre_seccion):
        """Muestra la sección solicitada y oculta las demás"""
        # Ocultar todas las secciones primero
        for seccion in self.secciones.values():
            seccion.pack_forget()
        
        # Mostrar la sección solicitada
        self.secciones[nombre_seccion].pack(fill="both", expand=True)
        
        # Actualizar datos si es necesario
        if nombre_seccion == "resumen":
            self.actualizar_resumen()
        elif nombre_seccion == "tarjetas":
            self.actualizar_lista_tarjetas()

    def crear_seccion_bienvenida(self):
        """Sección de bienvenida con resumen inicial"""
        frame = tk.Frame(self.content_area, bg=COLOR_FONDO)
        
        # Contenedor principal del contenido
        main_content = tk.Frame(frame, bg=COLOR_FONDO)
        main_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Frame de bienvenida con mejor estilo
        welcome_frame = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        welcome_frame.pack(fill="x", pady=10)
        
        # Título con líneas decorativas
        titulo_frame = tk.Frame(welcome_frame, bg="white")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_frame, text="¡Bienvenido a MyEconomy!",
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))
        
        # Subtítulo con mensaje de bienvenida
        tk.Label(welcome_frame, 
                text="Gestiona tus finanzas de manera inteligente",
                font=FUENTE_SUBTITULOS, 
                fg="#7f8c8d", 
                bg="white").pack(anchor="w", pady=10)

        # Frame de tarjetas con mejor estilo
        cards_container = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        cards_container.pack(fill="both", expand=True, pady=10)
        
        # Título con líneas decorativas
        titulo_tarjetas = tk.Frame(cards_container, bg="white")
        titulo_tarjetas.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_tarjetas, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_tarjetas, text="Mis Tarjetas de Crédito",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_tarjetas, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))
        
        # Contenedor para las tarjetas
        self.cards_container = tk.Frame(cards_container, bg="white")
        self.cards_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.actualizar_tarjetas_bienvenida()
        
        # Pie de página
        footer_frame = tk.Frame(main_content, bg=COLOR_FONDO, padx=20, pady=10)
        footer_frame.pack(fill="x", side="bottom")
        
        # Información de última actualización
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        tk.Label(footer_frame, 
                text=f"Última actualización: {current_time}",
                font=("Helvetica", 9),
                fg="#7f8c8d",
                bg=COLOR_FONDO).pack(side="right")
        
        self.secciones["bienvenida"] = frame

    def actualizar_tarjetas_bienvenida(self):
        """Actualiza la lista de tarjetas en la sección de bienvenida con mejor diseño"""
        for widget in self.cards_container.winfo_children():
            widget.destroy()

        tarjetas = obtener_tarjetas_usuario(self.id_usuario)
        
        if not tarjetas:
            # Mejorar el mensaje de no tarjetas
            no_cards_frame = tk.Frame(self.cards_container, bg="white", pady=20)
            no_cards_frame.pack(fill="x")
            
            tk.Label(no_cards_frame, 
                    text="No tienes tarjetas registradas",
                    font=FUENTE_SUBTITULOS, 
                    fg="#7f8c8d", 
                    bg="white").pack(pady=5)
                    
            tk.Label(no_cards_frame, 
                    text="Ve a la sección 'Tarjetas' para añadir una nueva tarjeta",
                    font=FUENTE_TEXTO, 
                    fg="#7f8c8d", 
                    bg="white").pack(pady=5)
            return
        
        # Frame contenedor de todas las tarjetas (scrollable si son muchas)
        cards_scroll_frame = tk.Frame(self.cards_container, bg="white")
        cards_scroll_frame.pack(fill="both", expand=True, pady=5)
        
        # Layout en grid para mejor distribución - ahora 4 tarjetas por fila
        num_columns = 4  # Número de tarjetas por fila
        current_row = 0
        current_col = 0
        
        # Configurar columnas con peso igual
        for i in range(num_columns):
            cards_scroll_frame.columnconfigure(i, weight=1, uniform="cards")
        
        # Estilos de tarjetas
        card_styles = [
            {"bg": "#3498db", "accent": "#2980b9"},  # Azul
            {"bg": "#2ecc71", "accent": "#27ae60"},  # Verde
            {"bg": "#e74c3c", "accent": "#c0392b"},  # Rojo
            {"bg": "#9b59b6", "accent": "#8e44ad"},  # Morado
            {"bg": "#f39c12", "accent": "#d35400"}   # Naranja
        ]
        
        for i, tarjeta in enumerate(tarjetas):
            # Seleccionar estilo de tarjeta
            style = card_styles[i % len(card_styles)]
            bg_color = style["bg"]
            accent_color = style["accent"]
            
            # Crear frame de tarjeta con mejor diseño - más pequeñas
            card_frame = tk.Frame(cards_scroll_frame, bg=bg_color, padx=10, pady=10, relief="raised", bd=1)
            card_frame.grid(row=current_row, column=current_col, sticky="nsew", padx=5, pady=5)
            
            # Encabezado de tarjeta
            header_frame = tk.Frame(card_frame, bg=bg_color)
            header_frame.pack(fill="x", pady=(0, 5))
            
            # Nombre del banco con accento visual
            tk.Frame(header_frame, bg="white", height=2).pack(fill="x", pady=(0, 3))
            tk.Label(header_frame, 
                    text=tarjeta['banco'].upper(), 
                    font=("Helvetica", 11, "bold"), 
                    fg="white", 
                    bg=bg_color).pack(anchor="w")
            
            # Número de tarjeta más compacto
            num_frame = tk.Frame(card_frame, bg=accent_color, padx=5, pady=3)
            num_frame.pack(fill="x", pady=3)
            
            # Formato visual del número como tarjeta real
            numero = tarjeta['numero']
            if len(numero) >= 16:  # Formatear como XXXX-...-XXXX
                formatted_num = f"{numero[:4]}...{numero[-4:]}"
            else:
                formatted_num = numero
                
            tk.Label(num_frame, 
                    text=formatted_num, 
                    font=("Courier", 12, "bold"), 
                    fg="white", 
                    bg=accent_color).pack(anchor="center")
            
            # Detalles de la tarjeta - más compactos
            details_frame = tk.Frame(card_frame, bg=bg_color, pady=3)
            details_frame.pack(fill="x")
            
            # Datos de la tarjeta en formato más compacto
            tk.Label(details_frame, 
                    text=f"Límite: ${float(tarjeta['limite']):,.2f}", 
                    font=("Helvetica", 10), 
                    fg="white", 
                    bg=bg_color).pack(anchor="w")
                    
            tk.Label(details_frame, 
                    text=f"Corte: {tarjeta['fecha_corte']}", 
                    font=("Helvetica", 10), 
                    fg="white", 
                    bg=bg_color).pack(anchor="w", pady=(2, 0))
            
            # Actualizar contador para grid
            current_col += 1
            if current_col >= num_columns:
                current_col = 0
                current_row += 1

    def crear_seccion_ingresos(self):
        """Sección para registrar y ver ingresos"""
        frame = tk.Frame(self.content_area, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True)
        
        # Contenedor principal del contenido
        main_content = tk.Frame(frame, bg=COLOR_FONDO)
        main_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Formulario de registro con mejor estilo
        form_frame = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(fill="x", pady=10)
        
        # Título con líneas decorativas
        titulo_frame = tk.Frame(form_frame, bg="white")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_CUARTO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_frame, text="Registrar Nuevo Ingreso",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_CUARTO).pack(fill="x", pady=(8, 0))

        # Campos de entrada con mejor diseño
        campos_frame = tk.Frame(form_frame, bg="white", padx=10)
        campos_frame.pack(fill="x", pady=10)
        
        self.descripcion_ingreso = tk.StringVar()
        self.monto_ingreso = tk.StringVar()
        
        # Descripción con etiqueta mejorada
        etiqueta_desc = tk.Label(campos_frame, text="Descripción:", 
                                font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_desc.pack(anchor="w", pady=(5, 2))
        
        entry_desc = tk.Entry(campos_frame, textvariable=self.descripcion_ingreso, 
                            font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_desc.pack(fill="x", pady=(0, 10))
        
        # Monto con etiqueta mejorada
        etiqueta_monto = tk.Label(campos_frame, text="Monto:", 
                                font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_monto.pack(anchor="w", pady=(5, 2))
        
        entry_monto = tk.Entry(campos_frame, textvariable=self.monto_ingreso,
                             font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_monto.pack(fill="x", pady=(0, 10))
        
        # Botón de registro con mejor estilo
        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.pack(fill="x", pady=10)
        
        tk.Button(btn_frame, text="Registrar Ingreso", command=self.registrar_ingreso,
                bg=COLOR_CUARTO, fg="white", font=FUENTE_BOTONES,
                padx=15, pady=8, relief="raised", bd=2, width=20).pack(anchor="center")

        # Lista de ingresos con mejor estilo
        list_container = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        list_container.pack(fill="both", expand=True, pady=10)
        
        # Título con líneas decorativas
        titulo_lista = tk.Frame(list_container, bg="white")
        titulo_lista.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_lista, height=2, bg=COLOR_CUARTO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_lista, text="Historial de Ingresos",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_lista, height=2, bg=COLOR_CUARTO).pack(fill="x", pady=(8, 0))

        # Frame para el Treeview con mejor estilo
        list_frame = tk.Frame(list_container, bg="white", padx=5, pady=10)
        list_frame.pack(fill="both", expand=True)
        
        # Estilo personalizado para el Treeview
        style = ttk.Style()
        # Textos en negro más oscuro para total visibilidad
        style.configure("Ingresos.Treeview", 
                       background="black",
                       foreground="#000000",  # Negro puro 
                       rowheight=25,
                       fieldbackground="black")
        # Cabeceras con letras blancas
        style.configure("Ingresos.Treeview.Heading", 
                       font=('Helvetica', 11, 'bold'),  # Fuente más grande y negrita
                       background=COLOR_CUARTO,
                       foreground="black", 
                       relief="raised")
        # Selección con letras blancas
        style.map('Ingresos.Treeview', 
                 background=[('selected', COLOR_CUARTO)],
                 foreground=[('selected', 'black')])
        
        # Crear Treeview para mostrar ingresos con estilo personalizado
        self.ingresos_tree = ttk.Treeview(list_frame, columns=("fecha", "descripcion", "monto"), 
                                         show="headings", style="Ingresos.Treeview")
        self.ingresos_tree.heading("fecha", text="Fecha y Hora")
        self.ingresos_tree.heading("descripcion", text="Categoría")
        self.ingresos_tree.heading("monto", text="Monto")
        self.ingresos_tree.column("fecha", width=150, anchor="center")  # Columna más ancha
        self.ingresos_tree.column("descripcion", width=250)
        self.ingresos_tree.column("monto", width=120, anchor="e")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.ingresos_tree.yview)
        self.ingresos_tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.ingresos_tree.pack(fill="both", expand=True)
        
        # Pie de página
        footer_frame = tk.Frame(main_content, bg=COLOR_FONDO, padx=20, pady=10)
        footer_frame.pack(fill="x", side="bottom")
        
        # Información de última actualización
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        tk.Label(footer_frame, 
                text=f"Última actualización: {current_time}",
                font=("Helvetica", 9),
                fg="#7f8c8d",
                bg=COLOR_FONDO).pack(side="right")
        
        self.actualizar_lista_ingresos()
        
        self.secciones["ingresos"] = frame

    def actualizar_lista_ingresos(self):
        """Actualiza la lista de ingresos en el Treeview"""
        for item in self.ingresos_tree.get_children():
            self.ingresos_tree.delete(item)
            
        ingresos = obtener_transacciones_usuario(self.id_usuario, "ingreso")
        
        # Colores alternos para las filas
        colors = ["white", "#e8f8e8"]  # Blanco y verde muy claro
        
        for idx, ingreso in enumerate(ingresos):
            item_id = self.ingresos_tree.insert("", "end", values=(
                ingreso['fecha'],
                ingreso['descripcion'],
                f"${float(ingreso['monto']):,.2f}"
            ))
            
            # Aplicar color de fondo alternado
            self.ingresos_tree.item(item_id, tags=(f"row_{idx % 2}",))
        
        # Configurar las etiquetas con los colores correspondientes
        self.ingresos_tree.tag_configure("row_0", background=colors[0], foreground="black")
        self.ingresos_tree.tag_configure("row_1", background=colors[1], foreground="black")

    def registrar_ingreso(self):
        """Registra un nuevo ingreso"""
        descripcion = self.descripcion_ingreso.get().strip()
        monto = self.monto_ingreso.get().strip()

        if not descripcion or not monto:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            monto = float(monto)
            if registrar_transaccion("ingreso", descripcion, monto, self.id_usuario):
                messagebox.showinfo("Éxito", "Ingreso registrado correctamente")
                self.descripcion_ingreso.set("")
                self.monto_ingreso.set("")
                self.actualizar_lista_ingresos()
            else:
                messagebox.showerror("Error", "No se pudo registrar el ingreso")
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")

    def crear_seccion_egresos(self):
        """Sección para registrar y ver egresos"""
        frame = tk.Frame(self.content_area, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True)
        
        # Contenedor principal del contenido
        main_content = tk.Frame(frame, bg=COLOR_FONDO)
        main_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Formulario de registro con mejor estilo
        form_frame = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(fill="x", pady=10)
        
        # Título con líneas decorativas
        titulo_frame = tk.Frame(form_frame, bg="white")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_TERCIARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_frame, text="Registrar Nuevo Egreso",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_TERCIARIO).pack(fill="x", pady=(8, 0))

        # Campos de entrada con mejor diseño
        campos_frame = tk.Frame(form_frame, bg="white", padx=10)
        campos_frame.pack(fill="x", pady=10)
        
        self.descripcion_egreso = tk.StringVar()
        self.monto_egreso = tk.StringVar()
        
        # Descripción con etiqueta mejorada
        etiqueta_desc = tk.Label(campos_frame, text="Descripción:", 
                                font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_desc.pack(anchor="w", pady=(5, 2))
        
        entry_desc = tk.Entry(campos_frame, textvariable=self.descripcion_egreso, 
                            font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_desc.pack(fill="x", pady=(0, 10))
        
        # Monto con etiqueta mejorada
        etiqueta_monto = tk.Label(campos_frame, text="Monto:", 
                                font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_monto.pack(anchor="w", pady=(5, 2))
        
        entry_monto = tk.Entry(campos_frame, textvariable=self.monto_egreso,
                             font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_monto.pack(fill="x", pady=(0, 10))
        
        # Botón de registro con mejor estilo
        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.pack(fill="x", pady=10)
        
        tk.Button(btn_frame, text="Registrar Egreso", command=self.registrar_egreso,
                bg=COLOR_TERCIARIO, fg="white", font=FUENTE_BOTONES,
                padx=15, pady=8, relief="raised", bd=2, width=20).pack(anchor="center")

        # Lista de egresos con mejor estilo
        list_container = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        list_container.pack(fill="both", expand=True, pady=10)
        
        # Título con líneas decorativas
        titulo_lista = tk.Frame(list_container, bg="white")
        titulo_lista.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_lista, height=2, bg=COLOR_TERCIARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_lista, text="Historial de Egresos",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_lista, height=2, bg=COLOR_TERCIARIO).pack(fill="x", pady=(8, 0))

        # Frame para el Treeview con mejor estilo
        list_frame = tk.Frame(list_container, bg="white", padx=5, pady=10)
        list_frame.pack(fill="both", expand=True)
        
        # Estilo personalizado para el Treeview de egresos
        style = ttk.Style()
        style.configure("Egresos.Treeview", 
                       background="black",
                       foreground="#000000",  # Negro puro para mayor visibilidad
                       rowheight=25,
                       fieldbackground="black")
        style.configure("Egresos.Treeview.Heading", 
                       font=('Helvetica', 11, 'bold'),  # Fuente más grande y negrita
                       background=COLOR_TERCIARIO,
                       foreground="black",
                       relief="raised")
        style.map('Egresos.Treeview', 
                 background=[('selected', COLOR_TERCIARIO)],
                 foreground=[('selected', 'black')])
        
        # Crear Treeview para mostrar egresos con estilo personalizado
        self.egresos_tree = ttk.Treeview(list_frame, columns=("fecha", "descripcion", "monto"), 
                                        show="headings", style="Egresos.Treeview")
        self.egresos_tree.heading("fecha", text="Fecha y Hora")
        self.egresos_tree.heading("descripcion", text="Categoría")
        self.egresos_tree.heading("monto", text="Monto")
        self.egresos_tree.column("fecha", width=150, anchor="center")  
        self.egresos_tree.column("descripcion", width=250)
        self.egresos_tree.column("monto", width=120, anchor="e")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.egresos_tree.yview)
        self.egresos_tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.egresos_tree.pack(fill="both", expand=True)
        
        # Pie de página
        footer_frame = tk.Frame(main_content, bg=COLOR_FONDO, padx=20, pady=10)
        footer_frame.pack(fill="x", side="bottom")
        
        # Información de última actualización
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        tk.Label(footer_frame, 
                text=f"Última actualización: {current_time}",
                font=("Helvetica", 9),
                fg="#7f8c8d",
                bg=COLOR_FONDO).pack(side="right")
        
        self.actualizar_lista_egresos()
        
        self.secciones["egresos"] = frame

    def actualizar_lista_egresos(self):
        """Actualiza la lista de egresos en el Treeview"""
        for item in self.egresos_tree.get_children():
            self.egresos_tree.delete(item)
            
        egresos = obtener_transacciones_usuario(self.id_usuario, "egreso")
        
        # Colores alternos para las filas
        colors = ["white", "#f8e8e8"]  # Blanco y rojo muy claro
        
        for idx, egreso in enumerate(egresos):
            item_id = self.egresos_tree.insert("", "end", values=(
                egreso['fecha'],
                egreso['descripcion'],
                f"${float(egreso['monto']):,.2f}"
            ))
            
            # Aplicar color de fondo alternado
            self.egresos_tree.item(item_id, tags=(f"row_{idx % 2}",))
        
        # Configurar las etiquetas con los colores correspondientes
        self.egresos_tree.tag_configure("row_0", background=colors[0], foreground="black")
        self.egresos_tree.tag_configure("row_1", background=colors[1], foreground="black")

    def registrar_egreso(self):
        """Registra un nuevo egreso"""
        descripcion = self.descripcion_egreso.get().strip()
        monto = self.monto_egreso.get().strip()

        if not descripcion or not monto:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            monto = float(monto)
            if registrar_transaccion("egreso", descripcion, monto, self.id_usuario):
                messagebox.showinfo("Éxito", "Egreso registrado correctamente")
                self.descripcion_egreso.set("")
                self.monto_egreso.set("")
                self.actualizar_lista_egresos()
            else:
                messagebox.showerror("Error", "No se pudo registrar el egreso")
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")

    def crear_seccion_tarjetas(self):
        """Sección para gestionar tarjetas de crédito"""
        frame = tk.Frame(self.content_area, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True)
        
        # Contenedor principal del contenido
        main_content = tk.Frame(frame, bg=COLOR_FONDO)
        main_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Formulario de registro con mejor estilo
        form_frame = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        form_frame.pack(fill="x", pady=10)
        
        # Título con líneas decorativas
        titulo_frame = tk.Frame(form_frame, bg="white")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_frame, text="Registrar Nueva Tarjeta",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))

        # Campos de entrada con mejor diseño
        campos_frame = tk.Frame(form_frame, bg="white", padx=10)
        campos_frame.pack(fill="x", pady=10)
        
        self.banco_tarjeta = tk.StringVar()
        self.limite_tarjeta = tk.StringVar()
        self.fecha_corte_tarjeta = tk.StringVar()
        
        # Banco con etiqueta mejorada
        etiqueta_banco = tk.Label(campos_frame, text="Banco:", 
                                font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_banco.pack(anchor="w", pady=(5, 2))
        
        entry_banco = tk.Entry(campos_frame, textvariable=self.banco_tarjeta, 
                             font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_banco.pack(fill="x", pady=(0, 10))
        
        # Límite con etiqueta mejorada
        etiqueta_limite = tk.Label(campos_frame, text="Límite de crédito:", 
                                 font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_limite.pack(anchor="w", pady=(5, 2))
        
        entry_limite = tk.Entry(campos_frame, textvariable=self.limite_tarjeta,
                              font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_limite.pack(fill="x", pady=(0, 10))
        
        # Fecha de corte con etiqueta mejorada
        etiqueta_fecha = tk.Label(campos_frame, text="Fecha de corte:", 
                                font=FUENTE_TEXTO, fg=COLOR_TEXTO, bg="white")
        etiqueta_fecha.pack(anchor="w", pady=(5, 2))
        
        entry_fecha = tk.Entry(campos_frame, textvariable=self.fecha_corte_tarjeta,
                             font=FUENTE_TEXTO, relief="solid", bd=1)
        entry_fecha.pack(fill="x", pady=(0, 10))
        
        # Botón de registro con mejor estilo
        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.pack(fill="x", pady=10)
        
        tk.Button(btn_frame, text="Agregar Tarjeta", command=self.registrar_tarjeta,
                bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                padx=15, pady=8, relief="raised", bd=2, width=20).pack(anchor="center")

        # Lista de tarjetas con mejor estilo
        list_container = tk.Frame(main_content, bg="white", padx=20, pady=20, relief="groove", bd=1)
        list_container.pack(fill="both", expand=True, pady=10)
        
        # Título con líneas decorativas
        titulo_lista = tk.Frame(list_container, bg="white")
        titulo_lista.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_lista, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_lista, text="Mis Tarjetas",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_lista, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))

        # Frame para el Treeview con mejor estilo
        list_frame = tk.Frame(list_container, bg="white", padx=5, pady=10)
        list_frame.pack(fill="both", expand=True)
        
        # Estilo personalizado para el Treeview de tarjetas
        style = ttk.Style()
        style.configure("Tarjetas.Treeview", 
                       background="black",
                       foreground="#000000",  # Negro puro para máxima visibilidad
                       rowheight=25,
                       fieldbackground="black")
        style.configure("Tarjetas.Treeview.Heading", 
                       font=('Helvetica', 11, 'bold'),  # Fuente más grande y negrita
                       background=COLOR_SECUNDARIO,
                       foreground="black",
                       relief="raised")
        style.map('Tarjetas.Treeview', 
                 background=[('selected', COLOR_SECUNDARIO)],
                 foreground=[('selected', 'black')])
        
        # Crear Treeview para mostrar tarjetas con estilo personalizado
        self.tarjetas_tree = ttk.Treeview(list_frame, columns=("banco", "limite", "corte"), 
                                         show="headings", style="Tarjetas.Treeview")
        self.tarjetas_tree.heading("banco", text="Banco")
        self.tarjetas_tree.heading("limite", text="Límite")
        self.tarjetas_tree.heading("corte", text="Fecha de Corte")
        self.tarjetas_tree.column("banco", width=200)
        self.tarjetas_tree.column("limite", width=150, anchor="e")
        self.tarjetas_tree.column("corte", width=150, anchor="center")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tarjetas_tree.yview)
        self.tarjetas_tree.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        self.tarjetas_tree.pack(fill="both", expand=True)
        
        # Información sobre tarjetas de crédito
        info_frame = tk.Frame(list_container, bg="white", relief="groove", bd=1, padx=15, pady=15)
        info_frame.pack(fill="x", pady=15)
        
        tk.Label(info_frame, 
                text="Consejos para el uso de tarjetas:",
                font=FUENTE_SUBTITULOS,
                fg=COLOR_PRIMARIO, 
                bg="white").pack(anchor="w", pady=(0, 10))
                
        consejos = [
            "• Paga siempre el total de tu deuda para evitar intereses",
            "• No utilices más del 30% de tu límite de crédito",
            "• Mantén un registro de tus gastos con tarjeta"
        ]
        
        for consejo in consejos:
            tk.Label(info_frame, 
                    text=consejo,
                    font=FUENTE_TEXTO,
                    fg=COLOR_TEXTO, 
                    bg="white").pack(anchor="w", pady=2)
        
        # Pie de página
        footer_frame = tk.Frame(main_content, bg=COLOR_FONDO, padx=20, pady=10)
        footer_frame.pack(fill="x", side="bottom")
        
        # Información de última actualización
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        tk.Label(footer_frame, 
                text=f"Última actualización: {current_time}",
                font=("Helvetica", 9),
                fg="#7f8c8d",
                bg=COLOR_FONDO).pack(side="right")
        
        self.actualizar_lista_tarjetas()
        
        self.secciones["tarjetas"] = frame

    def actualizar_lista_tarjetas(self):
        """Actualiza la lista de tarjetas en el Treeview"""
        for item in self.tarjetas_tree.get_children():
            self.tarjetas_tree.delete(item)
            
        tarjetas = obtener_tarjetas_usuario(self.id_usuario)
        
        # Colores alternos para las filas
        colors = ["white", "#e8f0f8"]  # Blanco y azul muy claro
        
        for idx, tarjeta in enumerate(tarjetas):
            item_id = self.tarjetas_tree.insert("", "end", values=(
                tarjeta['banco'],
                f"${float(tarjeta['limite']):,.2f}",
                tarjeta['fecha_corte']
            ))
            
            # Aplicar color de fondo alternado
            self.tarjetas_tree.item(item_id, tags=(f"row_{idx % 2}",))
        
        # Configurar las etiquetas con los colores correspondientes
        self.tarjetas_tree.tag_configure("row_0", background=colors[0], foreground="black")
        self.tarjetas_tree.tag_configure("row_1", background=colors[1], foreground="black")

    def registrar_tarjeta(self):
        """Registra una nueva tarjeta de crédito"""
        banco = self.banco_tarjeta.get().strip()
        limite = self.limite_tarjeta.get().strip()
        fecha_corte = self.fecha_corte_tarjeta.get().strip()

        if not banco or not limite or not fecha_corte:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            limite = float(limite)
            if registrar_tarjeta(self.id_usuario, banco, limite, fecha_corte):
                messagebox.showinfo("Éxito", "Tarjeta registrada correctamente")
                self.banco_tarjeta.set("")
                self.limite_tarjeta.set("")
                self.fecha_corte_tarjeta.set("")
                self.actualizar_lista_tarjetas()
                self.actualizar_tarjetas_bienvenida()
            else:
                messagebox.showerror("Error", "No se pudo registrar la tarjeta")
        except ValueError:
            messagebox.showerror("Error", "El límite debe ser un número válido")

    def crear_seccion_resumen(self):
        """Sección de resumen financiero"""
        frame = tk.Frame(self.content_area, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True)  # Asegurar que ocupe todo el espacio
        
        # Contenedor principal con scroll
        canvas = tk.Canvas(frame, bg=COLOR_FONDO, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=COLOR_FONDO)
        
        # Configuración del scroll
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=canvas.winfo_width())
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Forzar el ancho del canvas al ancho del frame
        def configure_canvas(event):
            canvas.itemconfig(window_id, width=event.width)
        
        window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.bind('<Configure>', configure_canvas)
        
        # Empaquetado del canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Obtener datos financieros
        ingresos = obtener_transacciones_usuario(self.id_usuario, "ingreso")
        egresos = obtener_transacciones_usuario(self.id_usuario, "egreso")
        total_ingresos = sum(float(t['monto']) for t in ingresos)
        total_egresos = sum(float(t['monto']) for t in egresos)
        balance = total_ingresos - total_egresos
        
        # Contenedor principal del contenido
        main_content = tk.Frame(scrollable_frame, bg=COLOR_FONDO)
        main_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Asegurar que main_content ocupe todo el ancho
        scrollable_frame.columnconfigure(0, weight=1)
        scrollable_frame.rowconfigure(0, weight=1)
        
        # Sección de métricas - usar todo el ancho
        metrics_container = tk.Frame(main_content, bg="white", padx=20, pady=20)
        metrics_container.pack(fill="x", pady=10)
        
        # Título centrado con línea decorativa
        titulo_frame = tk.Frame(metrics_container, bg="white")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_frame, 
                 text="Resumen Financiero",
                 font=FUENTE_TITULOS, 
                 fg=COLOR_PRIMARIO, 
                 bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))
        
        # Frame para las 3 métricas
        metrics_grid = tk.Frame(metrics_container, bg="white")
        metrics_grid.pack(fill="x", padx=40, pady=10)
        
        # Configurar columnas con peso igual
        for i in range(3):
            metrics_grid.columnconfigure(i, weight=1, uniform="metric_cols")
        
        # Crear las 3 métricas con tamaño más equilibrado
        metrics_data = [
            ("Total Ingresos", f"${total_ingresos:,.2f}", COLOR_CUARTO),
            ("Total Egresos", f"${total_egresos:,.2f}", COLOR_TERCIARIO),
            ("Balance", f"${balance:,.2f}", COLOR_CUARTO if balance >= 0 else COLOR_TERCIARIO)
        ]
        
        for col, (title, value, color) in enumerate(metrics_data):
            metric_frame = tk.Frame(metrics_grid, bg=color, padx=15, pady=15, relief="groove", bd=1)
            metric_frame.grid(row=0, column=col, sticky="nsew", padx=10)
            
            tk.Label(metric_frame, text=title,
                    font=FUENTE_SUBTITULOS,
                    fg="white", bg=color).pack(anchor="center")
            
            tk.Label(metric_frame, text=value,
                    font=("Helvetica", 16, "bold"),
                    fg="white", bg=color).pack(anchor="center", pady=5)
        
        # Sección de distribución de gastos con mejor diseño
        chart_container = tk.Frame(main_content, bg="white", padx=20, pady=20)
        chart_container.pack(fill="x", pady=10)
        
        # Título centrado con línea decorativa
        titulo_chart_frame = tk.Frame(chart_container, bg="white")
        titulo_chart_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_chart_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_chart_frame,
                 text="Distribución de Gastos",
                 font=FUENTE_SUBTITULOS,
                 fg=COLOR_PRIMARIO,
                 bg="white").pack(fill="x")
        tk.Frame(titulo_chart_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))
        
        # Obtener distribución de gastos por categoría
        categorias = {
            "Comida": 0,
            "Transporte": 0,
            "Entretenimiento": 0,
            "Servicios": 0,
            "Otros": 0
        }
        
        for egreso in egresos:
            desc = egreso['descripcion'].lower()
            monto = float(egreso['monto'])
            
            if "comida" in desc or "restaurante" in desc or "super" in desc:
                categorias["Comida"] += monto
            elif "transporte" in desc or "taxi" in desc or "gasolina" in desc:
                categorias["Transporte"] += monto
            elif "cine" in desc or "netflix" in desc or "entretenimiento" in desc:
                categorias["Entretenimiento"] += monto
            elif "luz" in desc or "agua" in desc or "internet" in desc:
                categorias["Servicios"] += monto
            else:
                categorias["Otros"] += monto
        
        # Calcular porcentajes
        total_gastos = sum(categorias.values())
        if total_gastos > 0:
            categorias = {k: (v/total_gastos)*100 for k, v in categorias.items()}
        
        # Filtrar categorías con valor > 0
        categorias_filtradas = {k: v for k, v in categorias.items() if v > 0}
        
        if not categorias_filtradas:
            tk.Label(chart_container, 
                     text="No hay datos de gastos para mostrar",
                     font=FUENTE_TEXTO,
                     fg="#7f8c8d",
                     bg="white").pack(pady=20)
        else:
            max_val = max(categorias_filtradas.values())
            
            # Frame para título explicativo y leyenda de colores
            chart_info_frame = tk.Frame(chart_container, bg="white")
            chart_info_frame.pack(fill="x", pady=(0, 15))
            
            # Texto explicativo
            tk.Label(chart_info_frame,
                    text="El siguiente gráfico muestra la distribución porcentual de tus gastos:",
                    font=FUENTE_TEXTO,
                    fg=COLOR_TEXTO,
                    bg="white").pack(anchor="w", pady=(0, 10))
            
            # Frame contenedor de barras para centrar todo
            barras_container = tk.Frame(chart_container, bg="white")
            barras_container.pack(fill="both", expand=True, padx=30)
            
            # Definir colores para categorías
            colores_categoria = {
                "Comida": "#3498db",
                "Transporte": "#2ecc71",
                "Entretenimiento": "#e74c3c",
                "Servicios": "#f39c12",
                "Otros": "#9b59b6"
            }
            
            # Mostrar cada categoría con su barra de progreso
            for i, (categoria, porcentaje) in enumerate(categorias_filtradas.items()):
                row_frame = tk.Frame(barras_container, bg="white")
                row_frame.pack(fill="x", pady=8)  # Espacio ajustado entre filas
                
                # Nombre de la categoría
                tk.Label(row_frame, 
                        text=categoria,
                        width=12,
                        anchor="w",
                        font=FUENTE_TEXTO,  # Fuente más pequeña
                        fg=COLOR_TEXTO,
                        bg="white").pack(side="left")
                
                # Barra de progreso con borde y esquinas redondeadas visuales
                bar_container = tk.Frame(row_frame, bg="white")
                bar_container.pack(side="left", fill="x", expand=True, padx=10)
                
                bar_bg = tk.Frame(bar_container, 
                                height=24,  # Altura ajustada
                                bg="#eeeeee",
                                bd=1,
                                relief="solid",
                                width=350)  # Ancho ajustado
                bar_bg.pack(side="left")
                
                bar_width = int((porcentaje/max_val) * 350)  # Ancho proporcional
                bar_color = colores_categoria[categoria]
                
                # Barra coloreada dentro del fondo gris
                tk.Frame(bar_bg,
                        width=bar_width,
                        height=24,  
                        bg=bar_color).place(x=0, y=0)
                
                # Porcentaje
                tk.Label(row_frame,
                        text=f"{porcentaje:.1f}%",
                        font=FUENTE_TEXTO,  # Fuente más pequeña
                        fg=COLOR_TEXTO,
                        bg="white",
                        width=8,
                        anchor="e").pack(side="left", padx=10)
            
            # Añadir estadísticas adicionales
            stats_frame = tk.Frame(chart_container, bg="white", relief="groove", bd=1, padx=15, pady=15)
            stats_frame.pack(fill="x", pady=15)
            
            # Determinar categoría con mayor gasto
            if categorias_filtradas:
                max_category = max(categorias_filtradas.items(), key=lambda x: x[1])[0]
                max_percent = max(categorias_filtradas.values())
                categoria_color = colores_categoria.get(max_category, "#3498db")
                
                # Título de estadísticas
                tk.Label(stats_frame,
                        text="Resumen Estadístico",
                        font=FUENTE_SUBTITULOS,
                        fg=COLOR_PRIMARIO,
                        bg="white").pack(anchor="w", pady=(0, 10))
                
                # Estadísticas de gastos
                stats_data = tk.Frame(stats_frame, bg="white")
                stats_data.pack(fill="x")
                
                # Columna izquierda
                left_stats = tk.Frame(stats_data, bg="white")
                left_stats.pack(side="left", fill="x", expand=True)
                
                tk.Label(left_stats,
                        text=f"Mayor categoría de gasto: {max_category} ({max_percent:.1f}%)",
                        font=FUENTE_TEXTO,
                        fg=categoria_color,
                        bg="white").pack(anchor="w", pady=2)
                
                tk.Label(left_stats,
                        text=f"Total de categorías: {len(categorias_filtradas)}",
                        font=FUENTE_TEXTO,
                        fg=COLOR_TEXTO,
                        bg="white").pack(anchor="w", pady=2)
                
                # Columna derecha
                right_stats = tk.Frame(stats_data, bg="white")
                right_stats.pack(side="right", fill="x", expand=True)
                
                # Calcular proporción ingresos/egresos
                if total_egresos > 0:
                    proporcion = total_ingresos / total_egresos
                    tk.Label(right_stats,
                            text=f"Ingresos/Egresos: {proporcion:.2f}x",
                            font=FUENTE_TEXTO,
                            fg=COLOR_TEXTO,
                            bg="white").pack(anchor="e", pady=2)
                    
                    # Calcular días restantes del mes
                    dias_mes = 30
                    dias_restantes = dias_mes - datetime.now().day
                    gasto_diario = total_egresos / (dias_mes - dias_restantes) if (dias_mes - dias_restantes) > 0 else 0
                    
                    tk.Label(right_stats,
                            text=f"Gasto promedio diario: ${gasto_diario:.2f}",
                            font=FUENTE_TEXTO,
                            fg=COLOR_TEXTO,
                            bg="white").pack(anchor="e", pady=2)
            
            # Añadir pie con información adicional
            footer_frame = tk.Frame(main_content, bg=COLOR_FONDO, padx=20, pady=10)
            footer_frame.pack(fill="x", side="bottom")
            
            # Información de última actualización
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
            tk.Label(footer_frame, 
                    text=f"Última actualización: {current_time}",
                    font=("Helvetica", 9),
                    fg="#7f8c8d",
                    bg=COLOR_FONDO).pack(side="right")
        
        self.secciones["resumen"] = frame

    def actualizar_resumen(self):
        """Actualiza los datos del resumen financiero"""
        # Esta función puede ser llamada para refrescar los datos
        pass

    def crear_seccion_config(self):
        """Sección de configuración de la aplicación"""
        frame = tk.Frame(self.content_area, bg=COLOR_FONDO)
        frame.pack(fill="both", expand=True)
        
        # Contenedor principal del contenido
        main_content = tk.Frame(frame, bg=COLOR_FONDO)
        main_content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Contenedor principal
        content_frame = tk.Frame(main_content, bg="white", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True, pady=10)
        
        # Frame para el título con líneas decorativas
        titulo_frame = tk.Frame(content_frame, bg="white")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(0, 8))
        tk.Label(titulo_frame, text="Configuración",
                font=FUENTE_TITULOS, fg=COLOR_PRIMARIO, bg="white").pack(fill="x")
        tk.Frame(titulo_frame, height=2, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(8, 0))
        
        # Separación visual
        tk.Frame(content_frame, height=15, bg="white").pack(fill="x")
        
        # Configuración de notificaciones
        notif_frame = tk.Frame(content_frame, bg="white", relief="groove", bd=1, padx=15, pady=15)
        notif_frame.pack(fill="x", pady=15)
        
        # Título de notificaciones con líneas decorativas
        titulo_notif_frame = tk.Frame(notif_frame, bg="white")
        titulo_notif_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(titulo_notif_frame, text="Configuración de notificaciones",
                font=FUENTE_SUBTITULOS, fg=COLOR_PRIMARIO, bg="white").pack(anchor="w")
        tk.Frame(titulo_notif_frame, height=1, bg=COLOR_SECUNDARIO).pack(fill="x", pady=(5, 0))
        
        # Descripción de notificaciones
        tk.Label(notif_frame, 
                text="Las notificaciones te ayudarán a mantenerte informado sobre tu situación financiera:",
                font=FUENTE_TEXTO,
                fg=COLOR_TEXTO,
                bg="white").pack(anchor="w", pady=(5, 10))
        
        # Frame para checkbuttons con mejor presentación
        check_container = tk.Frame(notif_frame, bg="white")
        check_container.pack(fill="x", pady=5)
        
        # Variables para las opciones
        self.notif_var = tk.IntVar(value=1)
        self.recordatorio_var = tk.IntVar(value=1)
        self.alerta_var = tk.IntVar(value=1)
        
        # Checkbuttons con mejor estilo
        tk.Checkbutton(check_container, text="Recibir notificaciones generales",
                      variable=self.notif_var, font=FUENTE_TEXTO,
                      fg=COLOR_TEXTO, bg="white", selectcolor=COLOR_FONDO,
                      padx=5, pady=3).pack(anchor="w", pady=3)
                      
        tk.Checkbutton(check_container, text="Recordatorios de gastos fijos",
                      variable=self.recordatorio_var, font=FUENTE_TEXTO,
                      fg=COLOR_TEXTO, bg="white", selectcolor=COLOR_FONDO,
                      padx=5, pady=3).pack(anchor="w", pady=3)
                      
        tk.Checkbutton(check_container, text="Alertas de presupuesto",
                      variable=self.alerta_var, font=FUENTE_TEXTO,
                      fg=COLOR_TEXTO, bg="white", selectcolor=COLOR_FONDO,
                      padx=5, pady=3).pack(anchor="w", pady=3)
        
        # Botón de guardar con mejor estilo
        boton_frame = tk.Frame(content_frame, bg="white")
        boton_frame.pack(fill="x", pady=20)
        
        # Separación visual
        tk.Frame(boton_frame, height=1, bg="#bdc3c7").pack(fill="x", pady=(0, 15))
        
        guardar_btn = tk.Button(boton_frame, text="Guardar Configuración",
                  command=self.guardar_configuracion,
                  bg=COLOR_SECUNDARIO, fg="white", font=FUENTE_BOTONES,
                  padx=50, pady=10, relief="raised", bd=2, width=10)
        guardar_btn.pack(side="top", anchor="center", pady=5)
        
        # Pie de página
        footer_frame = tk.Frame(main_content, bg=COLOR_FONDO, padx=20, pady=10)
        footer_frame.pack(fill="x", side="bottom")
        
        # Información de última actualización
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        tk.Label(footer_frame, 
                text=f"Última actualización: {current_time}",
                font=("Helvetica", 9),
                fg="#7f8c8d",
                bg=COLOR_FONDO).pack(side="right")
        
        self.secciones["config"] = frame

    def guardar_configuracion(self):
        """Guarda la configuración del usuario"""
        # Mostrar efecto visual en el botón de guardar
        self.boton_guardar_efecto()
        
        # Guardar cada preferencia
        config_guardada = {
            "notificaciones": {
                "generales": bool(self.notif_var.get()),
                "recordatorios": bool(self.recordatorio_var.get()),
                "alertas": bool(self.alerta_var.get())
            },
            "ultima_actualizacion": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        # Aquí se guardaría realmente la configuración en un archivo o base de datos
        
        # Mensajes según configuración
        if self.notif_var.get():
            mensaje = f"Configuración guardada con éxito. Las notificaciones están activadas."
        else:
            mensaje = f"Configuración guardada con éxito. Las notificaciones están desactivadas."
            
        messagebox.showinfo("Configuración guardada", mensaje)
    
    def boton_guardar_efecto(self):
        """Efecto visual al guardar configuración"""
        # Referencia al botón
        boton = None
        for widget in self.secciones["config"].winfo_children():
            if isinstance(widget, tk.Frame):
                for w in widget.winfo_children():
                    if isinstance(w, tk.Frame):
                        for b in w.winfo_children():
                            if isinstance(b, tk.Button) and b.cget("text") == "Guardar Configuración":
                                boton = b
                                break
        
        if not boton:
            return
            
        # Cambiar color por un momento
        color_original = boton.cget("bg")
        boton.config(bg=COLOR_CUARTO)
        self.after(100, lambda: boton.config(bg=color_original))

    def actualizar_tabla_ingresos(self):
        """Actualizar la tabla de ingresos con datos de la base de datos"""
        # Limpiar la tabla actual
        for item in self.ingresos_tree.get_children():
            self.ingresos_tree.delete(item)
        
        # Obtener ingresos de la base de datos
        ingresos = self.controlador.obtener_ingresos()
        
        # Definir colores alternados para las filas
        colors = ["#f2f2f2", "#e6f2ff"]  # Colores muy claros para buen contraste
        
        # Configurar tags para colorear filas
        self.ingresos_tree.tag_configure("row_0", background=colors[0], foreground="#000000")
        self.ingresos_tree.tag_configure("row_1", background=colors[1], foreground="#000000")
        
        # Insertar ingresos en la tabla con colores alternados
        for i, ingreso in enumerate(ingresos):
            # Formatear el monto como moneda
            monto_formateado = f"${ingreso['monto']:,.2f}"
            fecha_hora = f"{ingreso['fecha']} {ingreso['hora']}"
            
            # Insertar con el tag correspondiente para alternar colores
            tag = f"row_{i % 2}"
            self.ingresos_tree.insert("", "end", values=(fecha_hora, ingreso['categoria'], monto_formateado), tags=(tag,))
        
        # Calcular y mostrar el total
        total = sum(ingreso['monto'] for ingreso in ingresos)
        total_formateado = f"${total:,.2f}"
        self.total_ingresos_var.set(f"Total Ingresos: {total_formateado}")
    
    def actualizar_tabla_egresos(self):
        """Actualizar la tabla de egresos con datos de la base de datos"""
        # Limpiar la tabla actual
        for item in self.egresos_tree.get_children():
            self.egresos_tree.delete(item)
        
        # Obtener egresos de la base de datos
        egresos = self.controlador.obtener_egresos()
        
        # Definir colores alternados para las filas
        colors = ["#f2f2f2", "#fde6e6"]  # Colores muy claros para buen contraste
        
        # Configurar tags para colorear filas
        self.egresos_tree.tag_configure("row_0", background=colors[0], foreground="#000000")
        self.egresos_tree.tag_configure("row_1", background=colors[1], foreground="#000000")
        
        # Insertar egresos en la tabla con colores alternados
        for i, egreso in enumerate(egresos):
            # Formatear el monto como moneda
            monto_formateado = f"${egreso['monto']:,.2f}"
            fecha_hora = f"{egreso['fecha']} {egreso['hora']}"
            
            # Insertar con el tag correspondiente para alternar colores
            tag = f"row_{i % 2}"
            self.egresos_tree.insert("", "end", values=(fecha_hora, egreso['categoria'], monto_formateado), tags=(tag,))
        
        # Calcular y mostrar el total
        total = sum(egreso['monto'] for egreso in egresos)
        total_formateado = f"${total:,.2f}"
        self.total_egresos_var.set(f"Total Egresos: {total_formateado}")
    
    def actualizar_tabla_tarjetas(self):
        """Actualizar la tabla de tarjetas con datos de la base de datos"""
        # Limpiar la tabla actual
        for item in self.tarjetas_tree.get_children():
            self.tarjetas_tree.delete(item)
        
        # Obtener tarjetas de la base de datos
        tarjetas = self.controlador.obtener_tarjetas()
        
        # Definir colores alternados para las filas
        colors = ["#f2f2f2", "#e6f9f2"]  # Colores muy claros para buen contraste
        
        # Configurar tags para colorear filas
        self.tarjetas_tree.tag_configure("row_0", background=colors[0], foreground="#000000")
        self.tarjetas_tree.tag_configure("row_1", background=colors[1], foreground="#000000")
        
        # Insertar tarjetas en la tabla con colores alternados
        for i, tarjeta in enumerate(tarjetas):
            # Formatear el límite como moneda
            limite_formateado = f"${tarjeta['limite']:,.2f}"
            
            # Insertar con el tag correspondiente para alternar colores
            tag = f"row_{i % 2}"
            self.tarjetas_tree.insert("", "end", values=(tarjeta['banco'], limite_formateado, tarjeta['fecha_corte']), tags=(tag,))