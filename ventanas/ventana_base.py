import tkinter as tk
from PIL import Image, ImageTk
import os

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

class VentanaBase(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg=COLOR_FONDO)
        
        # Ajustar para ocupar todo el espacio
        self.grid(row=0, column=0, sticky="nsew")
        
        # Cargar el fondo como primera acción
        self.cargar_fondo()
        
        # Bind para actualizar el tamaño del fondo si cambia la ventana
        self.bind("<Configure>", self.actualizar_fondo)
        
    def cargar_fondo(self):
        """Carga la imagen de fondo y la aplica a toda la ventana"""
        try:
            fondo_path = os.path.join("datos", "imagenes", "fondo2.png")
            
            if not os.path.exists(fondo_path):
                print(f"Advertencia: No se encontró la imagen: {fondo_path}")
                print(f"Ruta buscada: {os.path.abspath(fondo_path)}")
                return  # Salir sin error si no encuentra la imagen
                
            # Obtener dimensiones
            self.update_idletasks() # Asegurarse de que las dimensiones estén actualizadas
            width = self.winfo_reqwidth()
            height = self.winfo_reqheight()
            
            # Si las dimensiones son muy pequeñas, usar tamaño de pantalla
            if width < 100 or height < 100:
                width = self.winfo_screenwidth()
                height = self.winfo_screenheight()
            
            print(f"Dimensiones del fondo: {width}x{height}")
            
            # Cargar y redimensionar la imagen
            imagen = Image.open(fondo_path)
            imagen = imagen.resize((width, height), Image.Resampling.LANCZOS)
            
            # Guardar referencia a la imagen (para evitar garbage collection)
            self.fondo = ImageTk.PhotoImage(imagen)
            
            # Crear label de fondo si no existe
            if not hasattr(self, 'background_label'):
                self.background_label = tk.Label(self, image=self.fondo)
                self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            else:
                # Actualizar imagen en label existente
                self.background_label.configure(image=self.fondo)
            
            # Asegurarse de que esté en el fondo
            self.background_label.lower()
            
            print("Fondo cargado correctamente!")
            
        except Exception as e:
            print(f"Error al cargar el fondo: {e}")
            import traceback
            traceback.print_exc()
            # En caso de error, usar color sólido como respaldo
            self.configure(bg=COLOR_FONDO)
    
    def actualizar_fondo(self, event=None):
        """Actualiza el tamaño del fondo si cambia el tamaño de la ventana"""
        # Solo actualizar si el tamaño es razonable
        if event and event.width > 100 and event.height > 100:
            try:
                # Obtener la ruta de la imagen
                fondo_path = os.path.join("datos", "imagenes", "fondo2.png")
                
                if not os.path.exists(fondo_path):
                    return
                
                # Cargar y redimensionar la imagen al nuevo tamaño
                imagen = Image.open(fondo_path)
                imagen = imagen.resize((event.width, event.height), Image.Resampling.LANCZOS)
                
                # Actualizar la imagen
                self.fondo = ImageTk.PhotoImage(imagen)
                self.background_label.configure(image=self.fondo)
                
                # Asegurar que permanezca en el fondo
                self.background_label.lower()
                
                print(f"Fondo actualizado a {event.width}x{event.height}")
            except Exception as e:
                print(f"Error al actualizar el fondo: {e}")
                import traceback
                traceback.print_exc()