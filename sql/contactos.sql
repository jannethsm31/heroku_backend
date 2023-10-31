CREATE TABLE contactos (
    email TEXT PRIMARY KEY,
    nombre TEXT,
    telefono TEXT
);

INSERT INTO contactos  (email, nombre, telefono) VALUES ('juan@example,com', 'Juan Perez', '555-123-4567');

INSERT INTO contactos (email, nombre, telefono) VALUES ('maria@example.com', 'Maria Garcia', '555-678-9012');