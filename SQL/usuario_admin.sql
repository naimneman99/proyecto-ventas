
USE SistemaVentasEnLinea;

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'adminSistemaVentas';

GRANT ALL PRIVILEGES ON SistemaVentasEnLinea.* TO 'admin'@'localhost';

FLUSH PRIVILEGES;
