# **MyEconomy App**  
**Tu Compañero de Finanzas Personales**  

---

# **¿De qué se trata este proyecto?**  
MyEconomy es una aplicación de escritorio hecha en Python con Tkinter. ¿Qué puedes hacer con ella? Bueno, básicamente te ayuda a:  
- Llevar un registro de tus ingresos y gastos.  
- Gestionar tus tarjetas de crédito, incluyendo límites y fechas de corte.  
- Generar reportes mensuales para que puedas analizar tus finanzas.

---

**¿Cuál es el objetivo?**  
Queremos que tengas una herramienta sencilla para gestionar tus finanzas personales. Con MyEconomy, puedes registrar tus ingresos, gastos, tarjetas de crédito y obtener reportes mensuales para ver cómo va tu salud financiera.

---

# **¿Qué problemas resuelve?**  
- No más excusas para no llevar un control financiero.  
- Te ayuda a ver claramente el balance entre lo que ganas y lo que gastas.  
- Organiza tus tarjetas de crédito y sus fechas de corte para que no te sorprendan.

---

# **¿Qué puedes hacer con MyEconomy?**  

- Registrarte y autenticarte de manera sencilla.  
- Gestionar tus transacciones, ya sean ingresos o egresos.  
- Administrar tus tarjetas de crédito, incluyendo límites y fechas de corte.  
- Generar reportes financieros mensuales para tener todo bajo control.

---

# **¿Cómo está estructurado el proyecto?**

**Arquitectura**  
- **Frontend:** Interfaz gráfica con Tkinter.  
- **Backend:** Lógica de negocio en Python.  
- **Almacenamiento:** Archivos de texto (usuarios.txt, transacciones.txt, tarjetas.txt).  

---

# **¿Cómo se organizan los archivos?**  

## **1. usuarios.txt**  
```plaintext
id,nombre,apellido,fecha_nacimiento,usuario,contraseña
JU001,Juan,Pérez,1990-05-15,juanp,juan123
```

## **2. transacciones.txt**  
```plaintext
id_usuario,tipo,descripcion,monto,fecha
JU001,egreso,Supermercado,350000,2024-03-16 14:30:45
```

## **3. tarjetas.txt**  
```plaintext
id_usuario,numero_tarjeta,banco,limite,fecha_corte
JU001,**** **** **** 1234,Bancolombia,5000000,25
```

---

# **¿Cómo es la interfaz?**

## **1. PantallaInicio**  
- Muestra el logo de la app.  
- Cambia automáticamente después de 3 segundos.  

## **2. VentanaInicio**  
- Aquí inicias sesión.  
- También puedes registrarte si eres nuevo.  

## **3. VentanaPrincipal**  
**Menú Lateral:**  
- Te saluda por tu nombre.  
- Te da opciones para navegar.  

**Área de Contenido:**  
- Te da la bienvenida con tus tarjetas.  
- Puedes ver y gestionar tus ingresos y egresos.  
- También puedes gestionar tus tarjetas.  

---

# **Diseño Visual**

## **Paleta de Colores**  
- **Fondo principal:** #333333  
- **Elementos positivos:** #4CAF50  
- **Elementos negativos:** #E74C3C  
- **Texto claro:** #FFFFFF  
- **Botones de acción:** #4CAF50  
- **Botón cerrar sesión:** #E74C3C  

---

# **¿Qué puedes hacer con MyEconomy?**  

## **Registro y Autenticación**  
- Regístrate con tus datos básicos.  
- Inicia sesión con tus credenciales.  

## **Gestión de Transacciones**  
- Registra tus ingresos como salarios o bonos.  
- Registra tus gastos, ya sean fijos o variables.  
- Filtra y visualiza tu historial por tipo y fecha.  

## **Tarjetas de Crédito**  
- Registra tus tarjetas con detalles importantes.  
- Visualiza tus tarjetas de manera segura.  

## **Reportes Financieros**  
- Obtén un balance mensual de tus finanzas.  
- Recibe alertas si tus gastos superan el 70% de tus ingresos.  

---

# **Validaciones y Control de Errores**

## **Validaciones Implementadas**  
- Asegúrate de llenar todos los campos obligatorios.  
- Verifica que los montos sean números válidos.  
- Asegúrate de que las fechas estén en el formato correcto.  
- Los límites de las tarjetas deben ser positivos.  
- Cada usuario debe tener credenciales únicas.  

## **Control de Errores**  
- Maneja archivos que no se encuentran.  
- Corrige errores de formato en los datos.  
- Soluciona fallos en el registro o inicio de sesión.  
- Asegúrate de tener permisos adecuados para los archivos.  

---

# **Alertas Financieras**  
**Recibe notificaciones cuando:**  
- Tus gastos superan el 70% de tus ingresos.  
- Tus tarjetas están cerca de su fecha de corte.  

---

# **Requisitos Técnicos**
- Python 3.x  
- Tkinter (incluido en Python)  
- Pillow (para manejo de imágenes)  
- Sistema de archivos con permisos de escritura  

---

# **Limitaciones Actuales**
- Almacenamiento en archivos planos.  
- Sin encriptación de contraseñas.  
- Sin respaldo automático de datos.  
- Reportes básicos sin gráficas.  

---

# **Mejoras Futuras**
- Migración a SQLite.  
- Encriptación de datos sensibles.  
- Gráficos estadísticos.  
- Exportación de reportes a PDF.  
- Categorización de gastos.  
- Presupuestos por categoría.  

---

# **Justificación**

- **Impacto Social:** Empodera a los usuarios con control financiero claro y accesible.  
- **Tecnología:** Uso de Python/Tkinter para rápida implementación y bajo costo.  
- **Escalabilidad:** Futura integración con bases de datos (SQLite) y análisis avanzado.  

---
