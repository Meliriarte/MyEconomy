# **MyEconomy App**  
**Tu Compañero de Finanzas Personales**  

---

# **¿De qué se trata este proyecto?**  
MyEconomy es una app de escritorio que hice con Python y Tkinter para ayudarte a manejar tu dinero. ¿Qué puedes hacer?:  
- Anotar todos tus ingresos y gastos
- Controlar tus tarjetas de crédito con sus límites y fechas de corte
- Ver de forma visual cómo está tu situación financiera
- Sacar informes mensuales para que sepas en qué gastas tu dinero

---

**¿Cuál es el objetivo?**  
La idea es tener una herramienta sencilla pero útil para controlar tus finanzas. La app tiene una interfaz bonita y moderna para que puedas registrar todo lo que ganas y gastas sin complicarte la vida.

---

# **¿Qué problemas resuelve?**  
- Ya no necesitas usar Excel con fórmulas complicadas para llevar tus cuentas
- Puedes ver claramente si estás gastando más de lo que ganas
- Te ayuda a no olvidarte de las fechas de corte de tus tarjetas
- Te facilita tomar mejores decisiones con tu dinero gracias a los informes visuales

---

# **¿Qué puedes hacer con MyEconomy?**  

- **Registrarte y entrar** con un login muy fácil de usar
- **Anotar tus movimientos** de dinero (lo que ganas y lo que gastas)
- **Controlar tus tarjetas** con una visualización moderna tipo "tarjeta real"
- **Ver informes** con gráficos para entender mejor tus finanzas
- **Personalizar** cómo se ve la app cambiando los colores

---

# **¿Cómo está estructurado el proyecto?**

**Arquitectura**  
- **Frontend:** La parte visual hecha con Tkinter, con estilos personalizados para que se vea bien
- **Backend:** La lógica de la app hecha en Python
- **Almacenamiento:** Archivos de texto para guardar los datos (usuarios.txt, transacciones.txt, tarjetas.txt)
- **Diseño:** Todo pensado para que sea fácil y agradable de usar

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
JU001,ingreso,Salario,2500000,2024-03-15 09:15:30
```

## **3. tarjetas.txt**  
```plaintext

id_usuario,numero_tarjeta,banco,limite,fecha_corte
JU001,**** **** **** 1234,Bancolombia,5000000,25
```

---

# **¿Cómo se ve la interfaz mejorada?**

## **1. Pantalla de Inicio**  
- Te muestra el logo de la app con un efecto visual
- Cambia automáticamente después de 3 segundos

## **2. Ventana de Login**  
- Un formulario de inicio de sesión simple y bonito
- Opción para registrarte si eres nuevo
- Te avisa de forma clara si te equivocas en la contraseña

## **3. Ventana Principal**  
**Menú Lateral:**  
- Un menú con iconos descriptivos
- Se puede expandir o contraer para tener más espacio
- Botones que cambian cuando pasas el ratón por encima
- Si quieres cerrar sesión, te pregunta para confirmar con botones del mismo tamaño

**Área de Contenido:**  
- **Bienvenida:** Un panel inicial con tus tarjetas en un diseño moderno
- **Ingresos:** Formulario fácil y tabla con colores alternados para que se lea mejor
- **Egresos:** Sistema para categorizar en qué gastas con diferentes colores
- **Tarjetas:** Visualización moderna de tus tarjetas
- **Resumen:** Informes con gráficos para entender en qué gastas tu dinero
- **Configuración:** Opciones para personalizar la app a tu gusto

---

# **Mejoras Visuales que he hecho**

- **Mejor contraste:** Ahora el texto es negro sobre fondos claros para que se lea bien
- **Tablas más claras:** Con colores alternados para no perderte entre tantos datos
- **Menús centrados:** Los diálogos de confirmación aparecen en el centro de la pantalla
- **Efectos visuales:** Los botones cambian cuando los pulsas
- **Más bonito:** Se añadieron líneas decorativas y separadores para que todo esté más organizado

---

# **Colores que estoy usando**  
- **Color Primario:** #2c3e50 (Un azul oscuro para las cosas importantes)
- **Color Secundario:** #3498db (Azul medio para elementos secundarios)
- **Color Terciario:** #e74c3c (Rojo para alertas y gastos)
- **Color Cuarto:** #2ecc71 (Verde para los ingresos y cosas positivas)
- **Color Fondo:** #ecf0f1 (Gris muy clarito para el fondo)
- **Color Texto:** #2c3e50 (Azul oscuro para el texto normal)
- **Color Texto Claro:** #ecf0f1 (Blanco para texto sobre fondos oscuros)

---

# **Lo que puedes hacer con la app**  

## **Registro y Login**  
- Registrarte con tus datos básicos
- Iniciar sesión super fácil

## **Control de Movimientos**  
- Registrar lo que ganas (sueldos, ventas, etc.)
- Anotar lo que gastas 
- Ver todo en tablas con colores alternados para no marearte

## **Tarjetas de Crédito**  
- Guardar tus tarjetas con todos sus datos
- Verlas con un diseño tipo "tarjeta real" con diferentes colores según el banco
- Recibir avisos cuando se acerca la fecha de pago
- Ver los números de forma segura (con asteriscos)

## **Informes**  
- Ver un balance de tu situación con colores
- Gráficos para entender en qué gastas más
- Indicadores visuales de tu estado financiero
- Comparativas con meses anteriores

---

# **Validaciones y Control de Errores**

## **Validaciones que tiene la app**  
- Te avisa si te dejas algún campo sin rellenar
- Comprueba que los montos sean números válidos
- Verifica que las fechas tengan el formato correcto
- Asegura que los límites de las tarjetas sean números positivos
- Evita que dos usuarios tengan el mismo nombre

## **Control de Errores**  
- Maneja los casos en que no encuentre los archivos
- Corrige errores de formato en los datos
- Te ayuda si tienes problemas para iniciar sesión
- Comprueba que tengas permisos para usar los archivos

---

# **Alertas Visuales**  
**Te avisa de forma clara cuando:**  
- Tus gastos superan el 70% de tus ingresos
- Se acerca la fecha de pago de tus tarjetas
- Vas a hacer algo importante (con mensajes de confirmación)
- Necesitas tomar decisiones (con opciones claramente visibles)


---

# **Cosas que faltan por mejorar**
- Ahora guardo todo en archivos de texto (pronto lo pasaré a SQLite)
- No cifro las contraseñas todavía
- No tiene backup automático
- Los informes son bastante básicos

---

# **Cosas que quiero añadir en el futuro**
- Usar SQLite para que todo funcione más rápido
- Cifrar las contraseñas y datos sensibles
- Añadir gráficos más atractivos
- Permitir exportar los informes a PDF
- Crear un sistema para personalizar las categorías de gastos
- Añadir presupuestos por categoría con seguimiento visual
- Hacer una versión para el móvil

---

# **Por qué creo que este proyecto es interesante**

- **Fácil de usar:** Interfaz diseñada para que cualquiera pueda manejarla sin manual
- **Tecnología:** Usa Python y Tkinter de forma eficiente con estilos personalizados
- **Visual:** Prioriza los elementos visuales para que entiendas tus finanzas de un vistazo
- **Ampliable:** Está hecho para que sea fácil añadir más cosas en el futuro

---

