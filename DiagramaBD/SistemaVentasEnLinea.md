Project SistemaVentasEnLinea {
  database_type: "MySQL"
}

Table Categorias {
  categoria_id int [pk, increment]
  padre_id int [ref: > Categorias.categoria_id]
  nombre varchar(100) [unique, not null]

  Note: "Categorías con relación recursiva (subcategorías)"
}

Table Clientes {
  cliente_id int [pk, increment]
  nombre varchar(100) [not null]
  apellido varchar(100) [not null]
  domicilio varchar(255) [not null]
  telefono varchar(15) [not null]
  correo_electronico varchar(100) [unique, not null]
}

Table Productos {
  producto_id int [pk, increment]
  nombre varchar(150) [unique, not null]
  descripcion text [not null]
  categoria_id int [not null, ref: > Categorias.categoria_id]
  precio_unitario decimal(10,2) [not null]
  stock int [not null, default: 0]
}

Table Ordenes {
  orden_id int [pk, increment]
  cliente_id int [not null, ref: > Clientes.cliente_id]
  fecha datetime [not null, default: 'CURRENT_TIMESTAMP']
  tipo_pago enum("Debito", "Credito", "Efectivo") [not null]
  estado enum("Pendiente", "Procesando", "Enviado", "Completada", "Cancelada") [not null, default: "Pendiente"]
  monto_total decimal(10,2) [not null]
}

Table DetallesOrden {
  orden_id int [not null, ref: > Ordenes.orden_id]
  producto_id int [not null, ref: > Productos.producto_id]
  cantidad int [not null]
  precio_al_momento decimal(10,2) [not null]

  Indexes {
    (orden_id, producto_id) [pk]
  }
}

