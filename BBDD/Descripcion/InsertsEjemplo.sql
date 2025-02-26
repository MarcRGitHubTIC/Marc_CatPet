-- Insertar clientes
INSERT INTO Cliente (fullName, correo, telefono, premium, user, pwd) VALUES
('Juan Pérez', 'juan.perez@example.com', '123456789', TRUE, 'juanp', 'password123'),
('María López', 'maria.lopez@example.com', '987654321', FALSE, 'marial', 'securepass'),
('Carlos Gómez', 'carlos.gomez@example.com', '456123789', TRUE, 'carlosg', 'mypassword');

-- Insertar mascotas
INSERT INTO Mascota (name) VALUES
('Firulais'),
('Michi'),
('Pelusa');

-- Relación Cliente-Mascota
INSERT INTO ClienteMascota (clientID, petID) VALUES
(1, 1), -- Juan Pérez tiene a Firulais
(2, 2), -- María López tiene a Michi
(3, 3); -- Carlos Gómez tiene a Pelusa

-- Insertar historial de mascotas
INSERT INTO Historial (fechaRegis, motivo, descripcion, mascotaID) VALUES
('2024-01-15', 'Vacunación', 'Vacuna antirrábica aplicada', 1),
('2024-02-10', 'Consulta general', 'Chequeo de rutina', 2),
('2024-03-05', 'Enfermedad', 'Diagnóstico de infección estomacal', 3);

-- Insertar productos
INSERT INTO Productos (nombre, descripcion, precio) VALUES
('Alimento para perros', 'Bolsa de 10kg de comida premium', 35.99),
('Arena para gatos', 'Arena absorbente de olores', 20.50),
('Juguete para mascotas', 'Pelota de goma resistente', 8.99);

-- Insertar veterinarias
INSERT INTO Veterinaria (calle, nombre, telefono, correo) VALUES
('Av. Siempre Viva 123', 'VetCare', '111222333', 'contacto@vetcare.com'),
('Calle Falsa 456', 'AnimalSalud', '444555666', 'info@animalsalud.com');

-- Insertar veterinarios
INSERT INTO Veterinario (nombre, licencia, clinicaID) VALUES
('Dr. Roberto Sánchez', 'VET-00123', 1),
('Dra. Laura Fernández', 'VET-00456', 2);

-- Insertar hilos de foro
INSERT INTO Foro (tema, pregunta, usuario) VALUES
('Alimentación', '¿Cuál es el mejor alimento para perros grandes?', 'juanp'),
('Salud felina', 'Mi gato no quiere comer, ¿qué puedo hacer?', 'marial');

-- Insertar comentarios en el foro
INSERT INTO Comentario (hiloID, usuario, contenido) VALUES
(1, 'carlosg', 'Yo recomiendo la marca X, es muy buena.'),
(2, 'juanp', 'Tal vez deberías llevarlo al veterinario.');

-- Insertar pedidos
INSERT INTO Pedido (clienteID) VALUES
(1),
(2);

-- Insertar detalles de pedidos
INSERT INTO PedidoDetalle (pedidoID, referencia, cantidad) VALUES
(1, 1, 2), -- Cliente 1 compra 2 bolsas de alimento para perros
(2, 2, 3); -- Cliente 2 compra 3 bolsas de arena para gatos
