-- CAT-PET Database

CREATE TABLE Cliente (
    clientID INT PRIMARY KEY AUTO_INCREMENT, 
    fullName VARCHAR(255) NOT NULL, 
    correo VARCHAR(255) UNIQUE NOT NULL, 
    telefono VARCHAR(15), 
    premium BOOLEAN DEFAULT FALSE, 
    user VARCHAR(50) UNIQUE NOT NULL, 
    pwd VARCHAR(255) NOT NULL
);

CREATE TABLE Mascota (
    petID INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL
);

CREATE TABLE ClienteMascota (
    clientID INT REFERENCES Cliente(clientID) ON DELETE CASCADE, 
    petID INT REFERENCES Mascota(petID) ON DELETE CASCADE, 
    PRIMARY KEY (clientID, petID)
);

CREATE TABLE Historial (
    historyID INT PRIMARY KEY AUTO_INCREMENT, 
    fechaRegis DATE NOT NULL, 
    motivo TEXT NOT NULL, 
    descripcion TEXT, 
    mascotaID INT REFERENCES Mascota(petID) ON DELETE CASCADE
);

CREATE TABLE Productos (
    referencia INT PRIMARY KEY AUTO_INCREMENT, 
    nombre VARCHAR(255) NOT NULL, 
    descripcion TEXT, 
    precio DECIMAL(10,2) CHECK (precio > 0)
);

CREATE TABLE Veterinaria (
    clinicaID INT PRIMARY KEY AUTO_INCREMENT, 
    calle VARCHAR(255) NOT NULL, 
    nombre VARCHAR(100) NOT NULL, 
    telefono VARCHAR(20), 
    correo VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE Veterinario (
    vetID INT PRIMARY KEY AUTO_INCREMENT, 
    nombre VARCHAR(100) NOT NULL, 
    licencia VARCHAR(50) UNIQUE NOT NULL, 
    clinicaID INT REFERENCES Veterinaria(clinicaID) ON DELETE SET NULL
);

CREATE TABLE Foro (
    hiloID INT PRIMARY KEY AUTO_INCREMENT, 
    tema VARCHAR(255) NOT NULL, 
    pregunta TEXT NOT NULL, 
    usuario VARCHAR(50) REFERENCES Cliente(user) ON DELETE CASCADE, 
    fechaCreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Comentario (
    comentarioID INT PRIMARY KEY AUTO_INCREMENT, 
    hiloID INT REFERENCES Foro(hiloID) ON DELETE CASCADE, 
    usuario VARCHAR(50) REFERENCES Cliente(user) ON DELETE CASCADE, 
    contenido TEXT NOT NULL, 
    fechaComentario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Pedido (
    pedidoID INT PRIMARY KEY AUTO_INCREMENT, 
    clienteID INT REFERENCES Cliente(clientID) ON DELETE CASCADE
);

CREATE TABLE PedidoDetalle (
    pedidoID INT REFERENCES Pedido(pedidoID) ON DELETE CASCADE, 
    referencia INT REFERENCES Productos(referencia) ON DELETE CASCADE, 
    cantidad INT CHECK (cantidad > 0),
    PRIMARY KEY (pedidoID, referencia)
);
