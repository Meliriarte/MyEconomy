import tkinter as tk
import os
from ventanas import PantallaInicio, VentanaInicio, VentanaPrincipal, VentanaRegistro
from funciones import inicializar_archivos

class MyEconomyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyEconomy")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.state("zoomed")

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
    inicializar_archivos()
    
    if not os.path.exists(os.path.join("datos", "imagenes")):
        os.makedirs(os.path.join("datos", "imagenes"))
    
    app = MyEconomyApp()
    app.mainloop()