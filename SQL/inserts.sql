-- 1. Insertar categorías
INSERT INTO Categorias (padre_id, nombre) VALUES
(NULL, 'Electrónica'),
(NULL, 'Hogar'),
(NULL, 'Ropa'),
(NULL, 'Juguetes'),
(NULL, 'Librería'),
(1, 'Celulares'),
(1, 'Computación'),
(2, 'Cocina'),
(2, 'Decoración'),
(3, 'Calzado');


-- 2. Insertar Clientes (10 clientes de ejemplo)
INSERT INTO Clientes (nombre, apellido, domicilio, telefono, correo_electronico) VALUES
('Juan', 'Pérez', 'Av. Siempreviva 123', '1122334455', 'juan.perez@mail.com'),
('María', 'Gómez', 'Calle Mitre 456', '1133445566', 'maria.gomez@mail.com'),
('Lucía', 'Martínez', 'San Martín 789', '1144556677', 'lucia.martinez@mail.com'),
('Carlos', 'Rodríguez', 'Belgrano 321', '1155667788', 'carlos.rod@mail.com'),
('Ana', 'Fernández', 'Rivadavia 654', '1166778899', 'ana.fer@mail.com'),
('Pedro', 'López', 'Urquiza 987', '1177889900', 'pedro.lopez@mail.com'),
('Jorge', 'Sosa', 'Estrada 159', '1188990011', 'jorge.sosa@mail.com'),
('Laura', 'Díaz', 'Alsina 357', '1199001122', 'laura.diaz@mail.com'),
('Marta', 'Suárez', 'Moreno 753', '1100112233', 'marta.suarez@mail.com'),
('Diego', 'Castro', 'Irigoyen 258', '1111223344', 'diego.castro@mail.com');


-- 3. Insertar Productos (10 productos de ejemplo)
-- Se mantienen los precios altos, pero se usarán precios unitarios inferidos en DetallesOrden
INSERT INTO Productos (nombre, descripcion, categoria_id, precio_unitario, stock) VALUES
('Notebook Lenovo', 'Notebook 15 pulgadas, 8GB RAM', 7, 500000.00, 50),
('Smartphone Samsung A34', 'Pantalla AMOLED 6.5"', 6, 350000.00, 70),
('Auriculares Sony', 'Auriculares Bluetooth', 1, 85000.00, 100),
('Zapatillas Nike Air', 'Running livianas', 10, 120000.00, 40),
('Licuadora Philips', '600W, vaso de vidrio', 8, 65000.00, 30),
('Lámpara LED Deco', 'Lámpara decorativa cálida', 9, 15000.00, 120),
('Camiseta Adidas', 'Camiseta deportiva', 3, 30000.00, 80),
('Mouse Logitech', 'Mouse inalámbrico', 7, 20000.00, 150),
('Cuaderno Rivadavia', 'Tapa dura 84 hojas', 5, 3500.00, 300),
('Robot de juguete', 'Robot interactivo con luces', 4, 28000.00, 60);


-- 4. Insertar Ordenes (100 órdenes de ejemplo) 
INSERT INTO Ordenes (cliente_id, tipo_pago, estado, monto_total) VALUES
(1,'Efectivo','Pendiente',2700.00), -- 1: 2x1200 + 1x300 = 2700
(1,'Credito','Pendiente',850.00), -- 2: 1x850 = 850
(1,'Debito','Pendiente',1200.00), -- 3: 2x600 = 1200
(1,'Credito','Pendiente',2250.00), -- 4: 1x1500 + 3x250 = 2250
(1,'Efectivo','Pendiente',300.00), -- 5: 1x300 = 300
(1,'Debito','Pendiente',4500.00), -- 6: 1x4500 = 4500
(1,'Credito','Pendiente',500.00), -- 7: 2x250 = 500
(1,'Debito','Pendiente',999.00), -- 8: 1x999 = 999
(1,'Efectivo','Pendiente',3450.00), -- 9: 1x1750 + 2x850 = 3450
(1,'Credito','Pendiente',600.00), -- 10: 3x200 = 600

(2,'Debito','Pendiente',1200.00), -- 11: 1x1200 = 1200
(2,'Credito','Pendiente',2300.00), -- 12: 2x850 + 1x600 = 2300
(2,'Efectivo','Pendiente',600.00), -- 13: 1x600 = 600
(2,'Debito','Pendiente',3000.00), -- 14: 2x1500 = 3000
(2,'Debito','Pendiente',1299.00), -- 15: 1x300 + 1x999 = 1299
(2,'Credito','Pendiente',4500.00), -- 16: 1x4500 = 4500
(2,'Debito','Pendiente',500.00), -- 17: 2x250 = 500
(2,'Credito','Pendiente',1599.00), -- 18: 1x999 + 3x200 = 1599. Error de cálculo en tu original, se ajusta a 1x999 + 1x600 = 1599
(2,'Debito','Pendiente',1750.00), -- 19: 1x1750 = 1750
(2,'Efectivo','Pendiente',200.00), -- 20: 1x200 = 200

(3,'Debito','Pendiente',1200.00), -- 21: 1x1200 = 1200
(3,'Efectivo','Pendiente',2550.00), -- 22: 3x850 = 2550
(3,'Debito','Pendiente',600.00), -- 23: 1x600 = 600
(3,'Credito','Pendiente',1800.00), -- 24: 1x1500 + 1x300 = 1800
(3,'Debito','Pendiente',600.00), -- 25: 2x300 = 600
(3,'Credito','Pendiente',4500.00), -- 26: 1x4500 = 4500
(3,'Efectivo','Pendiente',2248.00), -- 27: 1x250 + 2x999 = 2248
(3,'Efectivo','Pendiente',999.00), -- 28: 1x999 = 999
(3,'Credito','Pendiente',3500.00), -- 29: 2x1750 = 3500
(3,'Debito','Pendiente',200.00), -- 30: 1x200 = 200

(4,'Debito','Pendiente',3900.00), -- 31: 3x1200 + 1x300 = 3900
(4,'Credito','Pendiente',850.00), -- 32: 1x850 = 850
(4,'Debito','Pendiente',600.00), -- 33: 1x600 = 600
(4,'Credito','Pendiente',4500.00), -- 34: 3x1500 = 4500
(4,'Efectivo','Pendiente',600.00), -- 35: 2x300 = 600
(4,'Debito','Pendiente',4500.00), -- 36: 1x4500 = 4500
(4,'Efectivo','Pendiente',250.00), -- 37: 1x250 = 250
(4,'Credito','Pendiente',2749.00), -- 38: 1x1500 + 1x999 + 1x250 = 2749
(4,'Efectivo','Pendiente',1750.00), -- 39: 1x1750 = 1750
(4,'Debito','Pendiente',400.00), -- 40: 2x200 = 400

(5,'Efectivo','Pendiente',1200.00), -- 41: 1x1200 = 1200
(5,'Efectivo','Pendiente',5350.00), -- 42: 1x850 + 1x4500 = 5350
(5,'Debito','Pendiente',1200.00), -- 43: 2x600 = 1200
(5,'Credito','Pendiente',1500.00), -- 44: 1x1500 = 1500
(5,'Debito','Pendiente',300.00), -- 45: 1x300 = 300
(5,'Credito','Pendiente',9250.00), -- 46: 2x4500 + 1x250 = 9250
(5,'Debito','Pendiente',250.00), -- 47: 1x250 = 250
(5,'Debito','Pendiente',999.00), -- 48: 1x999 = 999
(5,'Efectivo','Pendiente',1750.00), -- 49: 1x1750 = 1750
(5,'Credito','Pendiente',200.00), -- 50: 1x200 = 200

(6,'Efectivo','Pendiente',2199.00), -- 51: 1x1200 + 1x999 = 2199
(6,'Credito','Pendiente',2550.00), -- 52: 3x850 = 2550
(6,'Debito','Pendiente',600.00), -- 53: 1x600 = 600
(6,'Debito','Pendiente',1500.00), -- 54: 1x1500 = 1500
(6,'Credito','Pendiente',2050.00), -- 55: 1x300 + 1x1750 = 2050
(6,'Efectivo','Pendiente',4500.00), -- 56: 1x4500 = 4500
(6,'Credito','Pendiente',500.00), -- 57: 2x250 = 500
(6,'Debito','Pendiente',1199.00), -- 58: 1x999 + 1x200 = 1199
(6,'Debito','Pendiente',3500.00), -- 59: 2x1750 = 3500
(6,'Credito','Pendiente',200.00), -- 60: 1x200 = 200

(7,'Credito','Pendiente',1200.00), -- 61: 1x1200 = 1200
(7,'Credito','Pendiente',850.00), -- 62: 1x850 = 850
(7,'Debito','Pendiente',1800.00), -- 63: 3x600 = 1800
(7,'Debito','Pendiente',3000.00), -- 64: 2x1500 = 3000
(7,'Efectivo','Pendiente',300.00), -- 65: 1x300 = 300
(7,'Credito','Pendiente',9000.00), -- 66: 2x4500 = 9000
(7,'Debito','Pendiente',1249.00), -- 67: 1x250 + 1x999 = 1249
(7,'Credito','Pendiente',1998.00), -- 68: 2x999 = 1998
(7,'Efectivo','Pendiente',3250.00), -- 69: 1x1750 + 1x1500 = 3250
(7,'Debito','Pendiente',600.00), -- 70: 3x200 = 600

(8,'Debito','Pendiente',2400.00), -- 71: 2x1200 = 2400
(8,'Efectivo','Pendiente',1450.00), -- 72: 1x850 + 1x600 = 1450
(8,'Credito','Pendiente',600.00), -- 73: 1x600 = 600
(8,'Credito','Pendiente',1500.00), -- 74: 1x1500 = 1500
(8,'Debito','Pendiente',600.00), -- 75: 2x300 = 600
(8,'Credito','Pendiente',4500.00), -- 76: 1x4500 = 4500
(8,'Credito','Pendiente',500.00), -- 77: 2x250 = 500
(8,'Debito','Pendiente',2749.00), -- 78: 1x999 + 1x1750 = 2749
(8,'Debito','Pendiente',1750.00), -- 79: 1x1750 = 1750
(8,'Debito','Pendiente',400.00), -- 80: 2x200 = 400

(9,'Efectivo','Pendiente',1200.00), -- 81: 1x1200 = 1200
(9,'Debito','Pendiente',1700.00), -- 82: 2x850 = 1700
(9,'Credito','Pendiente',600.00), -- 83: 1x600 = 600
(9,'Credito','Pendiente',3000.00), -- 84: 2x1500 = 3000
(9,'Efectivo','Pendiente',550.00), -- 85: 1x300 + 1x250 = 550
(9,'Debito','Pendiente',4500.00), -- 86: 1x4500 = 4500
(9,'Credito','Pendiente',250.00), -- 87: 1x250 = 250
(9,'Debito','Pendiente',1199.00), -- 88: 1x999 + 1x200 = 1199
(9,'Credito','Pendiente',3500.00), -- 89: 2x1750 = 3500
(9,'Debito','Pendiente',200.00), -- 90: 1x200 = 200

(10,'Debito','Pendiente',1500.00), -- 91: 1x1200 + 1x300 = 1500
(10,'Credito','Pendiente',850.00), -- 92: 1x850 = 850
(10,'Debito','Pendiente',1200.00), -- 93: 2x600 = 1200
(10,'Efectivo','Pendiente',1500.00), -- 94: 1x1500 = 1500
(10,'Credito','Pendiente',1299.00), -- 95: 1x300 + 1x999 = 1299
(10,'Efectivo','Pendiente',4500.00), -- 96: 1x4500 = 4500
(10,'Debito','Pendiente',250.00), -- 97: 1x250 = 250
(10,'Credito','Pendiente',999.00), -- 98: 1x999 = 999
(10,'Debito','Pendiente',1750.00), -- 99: 1x1750 = 1750
(10,'Efectivo','Pendiente',200.00); -- 100: 1x200 = 200


-- 5. Insertar DetallesOrden (Asegurando que la suma sea igual a monto_total de la Orden)
INSERT INTO DetallesOrden (orden_id, producto_id, cantidad, precio_al_momento) VALUES
-- Ordenes 1-10
(1, 1, 2, 1200.00), -- 2400.00
(1, 5, 1, 300.00),  -- 300.00. Total: 2700.00
(2, 2, 1, 850.00),  -- Total: 850.00
(3, 3, 2, 600.00),  -- Total: 1200.00
(4, 4, 1, 1500.00), -- 1500.00
(4, 7, 3, 250.00),  -- 750.00. Total: 2250.00
(5, 5, 1, 300.00),  -- Total: 300.00
(6, 6, 1, 4500.00), -- Total: 4500.00
(7, 7, 2, 250.00),  -- Total: 500.00
(8, 8, 1, 999.00),  -- Total: 999.00
(9, 9, 1, 1750.00), -- 1750.00
(9, 2, 2, 850.00),  -- 1700.00. Total: 3450.00
(10, 10, 3, 200.00), -- Total: 600.00

-- Ordenes 11-20
(11, 1, 1, 1200.00), -- Total: 1200.00
(12, 2, 2, 850.00),  -- 1700.00
(12, 3, 1, 600.00),  -- 600.00. Total: 2300.00
(13, 3, 1, 600.00),  -- Total: 600.00
(14, 4, 2, 1500.00), -- Total: 3000.00
(15, 5, 1, 300.00),  -- 300.00
(15, 8, 1, 999.00),  -- 999.00. Total: 1299.00
(16, 6, 1, 4500.00), -- Total: 4500.00
(17, 7, 2, 250.00),  -- Total: 500.00
(18, 8, 1, 999.00),  -- 999.00
(18, 3, 1, 600.00),  -- 600.00. Total: 1599.00 (Ajuste para que coincida con 1599)
(19, 9, 1, 1750.00), -- Total: 1750.00
(20, 10, 1, 200.00), -- Total: 200.00

-- Ordenes 21-30
(21, 1, 1, 1200.00), -- Total: 1200.00
(22, 2, 3, 850.00),  -- Total: 2550.00
(23, 3, 1, 600.00),  -- Total: 600.00
(24, 4, 1, 1500.00), -- 1500.00
(24, 5, 1, 300.00),  -- 300.00. Total: 1800.00
(25, 5, 2, 300.00),  -- Total: 600.00
(26, 6, 1, 4500.00), -- Total: 4500.00
(27, 7, 1, 250.00),  -- 250.00
(27, 8, 2, 999.00),  -- 1998.00. Total: 2248.00
(28, 8, 1, 999.00),  -- Total: 999.00
(29, 9, 2, 1750.00), -- Total: 3500.00
(30, 10, 1, 200.00), -- Total: 200.00

-- Ordenes 31-40
(31, 1, 3, 1200.00), -- 3600.00
(31, 5, 1, 300.00),  -- 300.00. Total: 3900.00
(32, 2, 1, 850.00),  -- Total: 850.00
(33, 3, 1, 600.00),  -- Total: 600.00
(34, 4, 3, 1500.00), -- Total: 4500.00
(35, 5, 2, 300.00),  -- Total: 600.00
(36, 6, 1, 4500.00), -- Total: 4500.00
(37, 7, 1, 250.00),  -- Total: 250.00
(38, 4, 1, 1500.00), -- 1500.00
(38, 8, 1, 999.00),  -- 999.00
(38, 7, 1, 250.00),  -- 250.00. Total: 2749.00 (Ajuste para que coincida con 2749)
(39, 9, 1, 1750.00), -- Total: 1750.00
(40, 10, 2, 200.00), -- Total: 400.00

-- Ordenes 41-50
(41, 1, 1, 1200.00), -- Total: 1200.00
(42, 2, 1, 850.00),  -- 850.00
(42, 6, 1, 4500.00), -- 4500.00. Total: 5350.00
(43, 3, 2, 600.00),  -- Total: 1200.00
(44, 4, 1, 1500.00), -- Total: 1500.00
(45, 5, 1, 300.00),  -- Total: 300.00
(46, 6, 2, 4500.00), -- 9000.00
(46, 7, 1, 250.00),  -- 250.00. Total: 9250.00
(47, 7, 1, 250.00),  -- Total: 250.00
(48, 8, 1, 999.00),  -- Total: 999.00
(49, 9, 1, 1750.00), -- Total: 1750.00
(50, 10, 1, 200.00), -- Total: 200.00

-- Ordenes 51-60
(51, 1, 1, 1200.00), -- 1200.00
(51, 8, 1, 999.00),  -- 999.00. Total: 2199.00
(52, 2, 3, 850.00),  -- Total: 2550.00
(53, 3, 1, 600.00),  -- Total: 600.00
(54, 4, 1, 1500.00), -- Total: 1500.00
(55, 5, 1, 300.00),  -- 300.00
(55, 9, 1, 1750.00), -- 1750.00. Total: 2050.00
(56, 6, 1, 4500.00), -- Total: 4500.00
(57, 7, 2, 250.00),  -- Total: 500.00
(58, 8, 1, 999.00),  -- 999.00
(58, 10, 1, 200.00), -- 200.00. Total: 1199.00
(59, 9, 2, 1750.00), -- Total: 3500.00
(60, 10, 1, 200.00), -- Total: 200.00

-- Ordenes 61-70
(61, 1, 1, 1200.00), -- Total: 1200.00
(62, 2, 1, 850.00),  -- Total: 850.00
(63, 3, 3, 600.00),  -- Total: 1800.00
(64, 4, 2, 1500.00), -- Total: 3000.00
(65, 5, 1, 300.00),  -- Total: 300.00
(66, 6, 2, 4500.00), -- Total: 9000.00
(67, 7, 1, 250.00),  -- 250.00
(67, 8, 1, 999.00),  -- 999.00. Total: 1249.00
(68, 8, 2, 999.00),  -- Total: 1998.00
(69, 9, 1, 1750.00), -- 1750.00
(69, 4, 1, 1500.00), -- 1500.00. Total: 3250.00
(70, 10, 3, 200.00), -- Total: 600.00

-- Ordenes 71-80
(71, 1, 2, 1200.00), -- Total: 2400.00
(72, 2, 1, 850.00),  -- 850.00
(72, 3, 1, 600.00),  -- 600.00. Total: 1450.00
(73, 3, 1, 600.00),  -- Total: 600.00
(74, 4, 1, 1500.00), -- Total: 1500.00
(75, 5, 2, 300.00),  -- Total: 600.00
(76, 6, 1, 4500.00), -- Total: 4500.00
(77, 7, 2, 250.00),  -- Total: 500.00
(78, 8, 1, 999.00),  -- 999.00
(78, 9, 1, 1750.00), -- 1750.00. Total: 2749.00
(79, 9, 1, 1750.00), -- Total: 1750.00
(80, 10, 2, 200.00), -- Total: 400.00

-- Ordenes 81-90
(81, 1, 1, 1200.00), -- Total: 1200.00
(82, 2, 2, 850.00),  -- Total: 1700.00
(83, 3, 1, 600.00),  -- Total: 600.00
(84, 4, 2, 1500.00), -- Total: 3000.00
(85, 5, 1, 300.00),  -- 300.00
(85, 7, 1, 250.00),  -- 250.00. Total: 550.00
(86, 6, 1, 4500.00), -- Total: 4500.00
(87, 7, 1, 250.00),  -- Total: 250.00
(88, 8, 1, 999.00),  -- 999.00
(88, 10, 1, 200.00), -- 200.00. Total: 1199.00
(89, 9, 2, 1750.00), -- Total: 3500.00
(90, 10, 1, 200.00), -- Total: 200.00

-- Ordenes 91-100
(91, 1, 1, 1200.00), -- 1200.00
(91, 5, 1, 300.00),  -- 300.00. Total: 1500.00
(92, 2, 1, 850.00),  -- Total: 850.00
(93, 3, 2, 600.00),  -- Total: 1200.00
(94, 4, 1, 1500.00), -- Total: 1500.00
(95, 5, 1, 300.00),  -- 300.00
(95, 8, 1, 999.00),  -- 999.00. Total: 1299.00
(96, 6, 1, 4500.00), -- Total: 4500.00
(97, 7, 1, 250.00),  -- Total: 250.00
(98, 8, 1, 999.00),  -- Total: 999.00
(99, 9, 1, 1750.00), -- Total: 1750.00
(100, 10, 1, 200.00); -- Total: 200.00