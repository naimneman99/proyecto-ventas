Proyecto Final de la materia Bases de Datos I
Implementación mínima del proyecto
Entrega
La entrega consiste subir a una carpeta del GIT del grupo de al menos cuatro
archivos:
• Justificación del diseño. Este archivo puede ser un documento estándar
(Mardown o PDF) donde se justifique el diseño de la base de datos que
debe corresponder al menos hasta 3NF, de forma similar al TP5.
• Fuente SQL. Este archivo debe contener todo el código SQL necesario
para crear las tablas y cargar datos inicales para el testing del proyecto
(e.g. INSERT’s)
• Archivo de código Python. Este archivo debe corresponder con las
consignas que se detallan abajo el proyecto elegido por el grupo.
• Archivo de Diseño de Esquema de Tablas. Puede ser una captura
de la imagen del diseño (e.g. imagen JPG, PNG, etc) o alternativamente
puede ser un archivo DBML con el diseño.
Características Mínimas Exigidas
El proyecto debe contener cada una de estas caracteríticas mínimas.
• Diseño esperado. Identifica entidades fuertes y débiles, atributos, relaciones y cardinalidades.
• Normalización: Debes aplicar las formas normales (1NF, 2NF y 3NF)
para optimizar el diseño de la base de datos y eliminar redundancias.
• Restricciones de Integridad: Define llaves primarias y foráneas. Aplica
restricciones NOT NULL, UNIQUE.
• Operaciones en cascada Define operaciones en cascada convenientes usando ON UPDATE CASCADE, ON DELETE RESTRICT, etc. donde sea necesario
para prevenir errores de consistencia.
• Consultas Avanzadas: Implementa INNER JOIN, LEFT JOIN y RIGHT
JOIN para recuperar datos relacionados. Utiliza cunando sea necesario
funciones agregadas y cláusulas como GROUP BY, HAVING, ORDER BY.
• Transacciones y Manejo de Errores: Utiliza transacciones para garantizar la consistencia de los datos en operaciones críticas.
• Procedimientos Almacenados y Funciones: Crea procedimientos
para manejar operaciones complejas como préstamos y devoluciones. Implementa funciones para cálculos específicos, como multas por retraso.
• Índices: Crea índices para mejorar el rendimiento de las consultas más
frecuentes. El diseño debe contener al menos un (1) índice.
• Python y mysql.connector: Desarrolla una aplicación en Python que
interactúe con la base de datos MySQL. Implementa una interfaz de usuario
(CLI) para facilitar la interacción con la aplicación.


Proyecto 2: Sistema de Ventas en Línea
Descripción:
Crea una plataforma de ventas en línea que gestione productos, clientes y órdenes
de compras. Las órdenes de compra deben contener el producto, la fecha y la
cantidad de unidades de ese producto.
• Modelo del Sistema. Diseña entidades como Productos, Clientes y
Órdenes.
• Datos inciales La base de datos inicial debe contener al menos diez (10)
productos y diez (10) clientes. La cantidad promedio de las órdenes debe
ser de diez (10) órdenes por cada cliente.
Consignas para el Menú del CLI
1. Gestión de Productos: Agregar, actualizar, ver o eliminar productos,
incluyendo categorías y niveles de stock.
2. Gestión de Clientes: Registrar, actualizar y ver detalles de clientes,
gestionar contactos.
3. Procesamiento de Órdenes: Mostrar las órdenes pedidas por un cliente
dado.
4. Búsquedas Avanzadas: Recuperar productos o clientes con filtros (e.g.,
productos más vendidos).
5. Reporte de productos más vendidos: Generar un reporte del producto
más vendido indicando la cantidad total pedida de ese producto.
6. Modificiación de valor de un producto: Modificar las órdenes de un
producto dado para ajustarse una cierta cantidad máxima.

