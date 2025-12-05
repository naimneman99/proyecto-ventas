
/*
    Codigo SQL para crear la base de datos de un sistema de ventas en línea y los insert
*/

CREATE DATABASE IF NOT EXISTS SistemaVentasEnLinea;
USE SistemaVentasEnLinea;


-- Tabla Categorias
CREATE TABLE Categorias (
    categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    padre_id INT NULL,
    nombre VARCHAR(100) UNIQUE NOT NULL, -- No debe haber dos categorías con el mismo nombre
    
    -- Relación recursiva para subcategorías
    CONSTRAINT fk_categoria_padre FOREIGN KEY (padre_id) REFERENCES Categorias(categoria_id)
    ON UPDATE CASCADE -- Si el ID de la categoría padre cambia, el ID en las subcategorías se actualiza automáticamente
    ON DELETE RESTRICT -- Si se intenta eliminar una categoría padre, la operación falla si existen subcategorías asociadas
);

-- Tabla Clientes
CREATE TABLE Clientes (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    domicilio VARCHAR(255) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL
);

-- Indice para búsqueda rápida Clientes por nombre y apellido
CREATE INDEX idx_cliente_nombre_completo ON Clientes (nombre, apellido);



-- Tabla Productos
CREATE TABLE Productos (
    producto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) UNIQUE NOT NULL,
    descripcion TEXT NOT NULL,
    categoria_id INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,

    CONSTRAINT fk_producto_categoria FOREIGN KEY (categoria_id) REFERENCES Categorias(categoria_id)
    ON UPDATE CASCADE 
    ON DELETE RESTRICT
);

-- Indice para búsqueda rápida de productos por nombre
CREATE INDEX idx_producto_nombre ON Productos (nombre);

-- Tabla Ordenes
CREATE TABLE Ordenes (
    orden_id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo_pago ENUM('Debito', 'Credito', 'Efectivo') NOT NULL,
    estado ENUM('Pendiente', 'Procesando', 'Enviado', 'Completada', 'Cancelada')  NOT NULL DEFAULT 'Pendiente',
    monto_total DECIMAL(10, 2) NOT NULL,

    CONSTRAINT fk_orden_cliente FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
    ON UPDATE CASCADE   -- Si el ID del cliente cambia, el ID en Ordenes se actualiza automáticamente
    ON DELETE RESTRICT -- Si se intenta eliminar un cliente, la operación falla si existen órdenes asociadas
);

-- Tabla DetallesOrden
CREATE TABLE DetallesOrden (
    orden_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_al_momento DECIMAL(10, 2) NOT NULL, -- Precio del producto al momento de la orden

    PRIMARY KEY (orden_id, producto_id),

    CONSTRAINT fk_detalleorden_orden FOREIGN KEY (orden_id) REFERENCES Ordenes(orden_id)
    ON UPDATE CASCADE -- Si el ID de la orden cambia, el ID en DetallesOrden se actualiza automáticamente
    ON DELETE CASCADE, -- Si se elimina una orden, se eliminan sus detalles automáticamente

    CONSTRAINT fk_detalleorden_producto FOREIGN KEY (producto_id) REFERENCES Productos(producto_id)
    ON UPDATE CASCADE -- Si el ID del producto cambia, el ID en DetallesOrden se actualiza automáticamente
    ON DELETE RESTRICT -- Si se intenta eliminar un producto, la operación falla si existen detalles de orden asociados
);


