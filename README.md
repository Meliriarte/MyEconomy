# **MyEconomy App**  
**Plataforma de Gestión Financiera Personal**  

---

# **Descripción del Proyecto**  
MyEconomy es una aplicación de escritorio desarrollada en Python con Tkinter que permite:  
-Registrar y clasificar transacciones financieras (ingresos/egresos). <br>
-Gestionar tarjetas de crédito (límites, fechas de corte). <br>
-Generar reportes mensuales para análisis financiero.

---

**Objetivo Principal:**  
Desarrollar una aplicación de escritorio para gestión financiera personal que permita a los usuarios registrar ingresos, egresos, tarjetas de crédito y generar reportes mensuales para evaluar su salud financiera.

---

# **Problemática que resuelve:**  
-Falta de herramientas accesibles para el control financiero personal. <br>
-Dificultad para visualizar el balance entre ingresos y gastos. <br>
-Desorganización en el manejo de tarjetas de crédito y fechas de corte. <br>

---

# **Alcance**  

-Registro de usuarios con autenticación básica. <br>
-Gestión de transacciones (ingresos/egresos). <br>
-Administración de tarjetas de crédito (límites, fechas de corte). <br>
-Generación de reportes financieros mensuales. <br>

---

# **Estructura del proyecto**

**Arquitectura** <br>
-Frontend: Interfaz gráfica con Tkinter. <br>
-Backend: Lógica de negocio en Python. <br>
-Almacenamiento: Archivos de texto (usuarios.txt, transacciones.txt, tarjetas.txt). <br>

---

# **Estructura de Archivos**  

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

# **Estructura de Interfaz**

## **1. PantallaInicio** <br>
-Logo de la aplicación <br>
-Transición automática (3 segundos) <br>

## **2. VentanaInicio** <br>
-Formulario de login <br>
-Botón de registro <br>

## **3. VentanaPrincipal** <br>
**Menú Lateral:** <br>
-Saludo personalizado <br>
-Opciones de navegación <br>

**Área de Contenido:** <br>
-Vista de bienvenida con tarjetas <br>
-Secciones para ingresos/egresos <br>
-Gestión de tarjetas <br>

---

# **Diseño Visual**

## **Paleta de Colores** <br>
-Fondo principal: **#333333** <br>
-Elementos positivos: **#4CAF50** <br>
-Elementos negativos: **#E74C3C** <br>
-Texto claro: **#FFFFFF** <br>
-Botones de acción: **#4CAF50** <br>
-Botón cerrar sesión: **#E74C3C** <br>

---

# **Funcionalidades claves**  

## **Registro y Autenticación** <br>
-Los usuarios se registran con nombre, apellido, fecha de nacimiento, usuario y contraseña. <br>
-Inicio de sesión con credenciales almacenadas en usuarios.txt. <br>

## **Gestión de Transacciones** <br>
-Ingresos: Salarios, bonos, etc. <br>
-Egresos: Gastos fijos/variables (alimentos, servicios). <br>
-Visualización: Historial filtrado por tipo y fecha. <br>

## **Tarjetas de Crédito** <br>
-Registro de tarjetas con detalles de banco, límite y fecha de corte. <br>
-Visualización en formato seguro (**** **** **** 1234). <br>

## **Reportes Financieros** <br>
-Balance mensual (Total ingresos - Total egresos). <br>
-Alertas si los egresos superan el 70% de los ingresos. <br>

---

# **Validaciones y Control de Errores**

## **Validaciones Implementadas** <br>
-Campos obligatorios en formularios <br>
-Montos numéricos válidos <br>
-Fechas en formato correcto <br>
-Límites de tarjetas positivos <br>
-Credenciales de usuario únicas <br>

## **Control de Errores** <br>
-Archivos no encontrados <br>
-Errores de formato en datos <br>
-Fallos en registro/login <br>
-Problemas de permisos en archivos <br>

---

# **Alertas Financieras**  
**Notificación automática cuando:** <br>
-Los egresos superan el 70% de los ingresos. <br>
-Hay tarjetas próximas a su fecha de corte. <br>

---

# **Requisitos Técnicos**
-Python 3.x <br>
-Tkinter (incluido en Python) <br>
-Pillow (para manejo de imágenes) <br>
-Sistema de archivos con permisos de escritura <br>

---

# **Limitaciones Actuales**
-Almacenamiento en archivos planos <br>
-Sin encriptación de contraseñas <br>
-Sin respaldo automático de datos <br>
-Reportes básicos sin gráficas <br>

---

# **Mejoras Futuras**
-Migración a SQLite <br>
-Encriptación de datos sensibles <br>
-Gráficos estadísticos <br>
-Exportación de reportes a PDF <br>
-Categorización de gastos <br>
-Presupuestos por categoría <br>

---

# **Justificación**

-Impacto Social: Empodera a los usuarios con control financiero claro y accesible. <br>
-Tecnología: Uso de Python/Tkinter para rápida implementación y bajo costo. <br>
-Escalabilidad: Futura integración con bases de datos (SQLite) y análisis avanzado. <br>

---
