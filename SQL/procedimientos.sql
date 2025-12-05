
DELIMITER $$

CREATE PROCEDURE ModificarCantidadOrdenesSegura(
    IN p_producto_id INT,
    IN p_cantidad_maxima INT
)
BEGIN
    
    -- variable para indicar si ocurrió un error
    DECLARE transaction_error BOOL DEFAULT FALSE;

    -- Handler para capturar errores
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET transaction_error = TRUE;


    START TRANSACTION;

    -- Actualizar la cantidad en DetallesOrden
    UPDATE DetallesOrden
    SET
        cantidad = p_cantidad_maxima
    WHERE
        producto_id = p_producto_id AND cantidad > p_cantidad_maxima;

    -- Evaluar si hubo errores durante la actualización
    IF transaction_error = TRUE THEN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error en la actualización de órdenes. Transacción revertida (ROLLBACK).';
    ELSE
        COMMIT;
    END IF;

END $$

DELIMITER ;