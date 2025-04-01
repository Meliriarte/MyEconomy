# **MyEconomy App**  
**Plataforma de Gestión Financiera Personal**  

---

# **Descripción del Proyecto**  
MyEconomy es una aplicación de escritorio desarrollada en Python con Tkinter que permite:  
 Registrar y clasificar **transacciones financieras** (ingresos/egresos)  
 Gestionar **tarjetas de crédito** (límites, fechas de corte)  
 Generar **reportes mensuales** para análisis financiero  

---

**Objetivo Principal:**  
Desarrollar una aplicación de escritorio para gestión financiera personal que permita a los usuarios registrar ingresos, egresos, tarjetas de crédito y generar reportes mensuales para evaluar su salud financiera.

---

# **Problemática que resuelve:**  
-Falta de herramientas accesibles para el control financiero personal.
-Dificultad para visualizar el balance entre ingresos y gastos.
-Desorganización en el manejo de tarjetas de crédito y fechas de corte.

---

# **Alcance**  

-Registro de usuarios con autenticación básica.
-Gestión de transacciones (ingresos/egresos).
-Administración de tarjetas de crédito (límites, fechas de corte).
-Generación de reportes financieros mensuales.

---

# **Estructura del proyecto**

**Arquitectura**
-Frontend: Interfaz gráfica con Tkinter.
-Backend: Lógica de negocio en Python.
-Almacenamiento: Archivos de texto (usuarios.txt, transacciones.txt, tarjetas.txt).

---

# **Estructura de Archivos**  

# **1. usuarios.txt**  
```plaintext
id;nombre;apellido;fecha_nacimiento;usuario;contraseña

JU001;Juan;Pérez;1990-05-15;juanp;juan123
```

# **2. transacciones.txt**  
```plaintext
id_usuario;tipo(ingreso/egreso);descripción;monto;fecha

JU001;egreso;Supermercado;350000;2024-09-16
```

# **3. tarjetas.txt**  
```plaintext
id_usuario;número_tarjeta;banco;límite;fecha_corte

JU001;**** **** **** 1234;Bancolombia;5000000;25
```

---

# **Funcionalidades claves**  

# **Registro y Autenticación**

-Los usuarios se registran con nombre, apellido, fecha de nacimiento, usuario y contraseña.
-Inicio de sesión con credenciales almacenadas en usuarios.txt.

# **Gestión de Transacciones**

-Ingresos: Salarios, bonos, etc.
-Egresos: Gastos fijos/variables (alimentos, servicios).
-Visualización: Historial filtrado por tipo y fecha.

# **Tarjetas de Crédito**

-Registro de tarjetas con detalles de banco, límite y fecha de corte.
-Visualización en formato seguro (**** **** **** 1234).

# **Reportes Financieros**
-Balance mensual (Total ingresos - Total egresos).
-Alertas si los egresos superan el 70% de los ingresos.

---

# **Alertas Financieras**  
Notificación automática cuando:  
- Los egresos superan el 70% de los ingresos
- Hay tarjetas próximas a su fecha de corte

---

# **Justificación**

-Impacto Social: Empodera a los usuarios con control financiero claro y accesible.
-Tecnología: Uso de Python/Tkinter para rápida implementación y bajo costo.
-Escalabilidad: Futura integración con bases de datos (SQLite) y análisis avanzado.

---

## **📖 Manual de Usuario**  

### **1. Primeros Pasos**  
1. **Registro**: Completa el formulario inicial  
2. **Login**: Ingresa con tus credenciales  

### **2. Transacciones**  
| **Paso** | **Acción**                          | **Ejemplo**              |
|----------|------------------------------------|--------------------------|
| 1        | Seleccionar "Ingresos/Egresos"     | Click en botón           |
| 2        | Completar formulario               | Descripción: "Salario"   |
| 3        | Confirmar                          | Click en "Registrar"     |

### **3. Tarjetas**  
📌 **Importante**:  
- Usar formato válido para fechas de corte (1-31)  
- Los límites deben ser valores numéricos  
