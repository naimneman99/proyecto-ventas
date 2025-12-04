# Justificación del Diseño de la Base de Datos

## Sistema de Ventas en Línea

Este documento presenta la arquitectura de la base de datos para el sistema de ventas en línea y justifica las decisiones tomadas respecto de normalización, restricciones, claves, relaciones e índices.

## 1. Entidades y Relaciones

El sistema se compone de las siguientes tablas:

-   Clientes: información personal y de contacto.
-   Categorias: categorías y subcategorías (relación recursiva vía
    padre_id).
-   Productos: catálogo de productos, cada uno asociado a una categoría.
-   Ordenes: compras realizadas por los clientes.
-   DetallesOrden: ítems incluidos en cada orden.

Relaciones principales:

-   Un cliente puede realizar muchas órdenes (1:N).
-   Una orden puede incluir varios productos y un producto puede estar
    en varias órdenes (N:N), resuelto mediante DetallesOrden.
-   Cada producto pertenece a una categoría (N:1).
-   Las categorías pueden contener subcategorías (1:N recursivo).

## 2. Normalización

El diseño alcanza Tercera Forma Normal (3NF):

-   1NF: todos los atributos son atómicos, sin listas ni valores
    repetitivos.
-   2NF: en DetallesOrden, la única tabla con clave compuesta, todos los
    atributos dependen de la clave completa (orden_id, producto_id).
-   3NF: no existen dependencias transitivas.
    -   El precio histórico se almacena en DetallesOrden
        (precio_al_momento), evitando depender del precio actual del
        producto.
    -   Los datos se encuentran separados por entidad, sin redundancias innecesarias.

## 3. Restricciones y claves

Claves primarias:

-   cliente_id, categoria_id, producto_id, orden_id
-   En DetallesOrden: clave compuesta (orden_id, producto_id)

Claves foráneas:

-   Productos.categoria_id → Categorias
-   Categorias.padre_id → Categorias
-   Ordenes.cliente_id → Clientes
-   DetallesOrden.orden_id → Ordenes
-   DetallesOrden.producto_id → Productos

Las acciones ON DELETE y ON UPDATE fueron seleccionadas para preservar
integridad:

-   RESTRICT en entidades con historial (clientes, productos,
    categorías).
-   CASCADE para eliminar automáticamente los detalles de una orden
    eliminada.

Otras restricciones:

-   Campos NOT NULL en atributos esenciales.
-   UNIQUE en nombres de productos y categorías.
-   ENUM para controlar valores válidos de pago y estado.

## 4. Índices

Los índices fueron definidos según las consultas más comunes:

-   Clientes: búsqueda por nombre y apellido.
-   Productos: búsqueda por nombre y filtrado por categoría.
-   Ordenes: búsqueda de órdenes por cliente.
-   DetallesOrden: consultas por producto dentro de órdenes.

