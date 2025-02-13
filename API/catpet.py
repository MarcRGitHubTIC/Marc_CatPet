# Función para convertir los datos de Cliente a diccionario
def cliente_schema(cliente) -> dict:
    return {
        "ClientID": cliente[0],
        "FullName": cliente[1],
        "Correo": cliente[2],
        "Telefono": cliente[3],
        "Premium": cliente[4],
        "User": cliente[5],
        "Pwd": cliente[6]
    }

# Función para convertir la lista de clientes a diccionario
def clientes_schema(clientes) -> dict:
    return [cliente_schema(cliente) for cliente in clientes]

# Función para convertir los datos de Mascota a diccionario
def mascota_schema(mascota) -> dict:
    return {
        "PetID": mascota[0],
        "Name": mascota[1]
    }

# Función para convertir la lista de mascotas a diccionario
def mascotas_schema(mascotas) -> dict:
    return [mascota_schema(mascota) for mascota in mascotas]

# Función para convertir los datos de Producto a diccionario
def producto_schema(producto) -> dict:
    return {
        "ProductID": producto[0],
        "Nombre": producto[1],
        "Descripcion": producto[2],
        "Precio": producto[3]
    }

# Función para convertir la lista de productos a diccionario
def productos_schema(productos) -> dict:
    return [producto_schema(producto) for producto in productos]

# Función para convertir los datos de Veterinaria a diccionario
def veterinaria_schema(veterinaria) -> dict:
    return {
        "VetID": veterinaria[0],
        "Nombre": veterinaria[1],
        "Direccion": veterinaria[2],
        "Telefono": veterinaria[3]
    }

# Función para convertir la lista de veterinarias a diccionario
def veterinarias_schema(veterinarias) -> dict:
    return [veterinaria_schema(veterinaria) for veterinaria in veterinarias]

# Función para convertir los datos de Veterinario a diccionario
def veterinario_schema(veterinario) -> dict:
    return {
        "VetID": veterinario[0],
        "Nombre": veterinario[1],
        "Licencia": veterinario[2],
        "Telefono": veterinario[3]
    }

# Función para convertir la lista de veterinarios a diccionario
def veterinarios_schema(veterinarios) -> dict:
    return [veterinario_schema(veterinario) for veterinario in veterinarios]

# Función para convertir los datos de Historial a diccionario
def historial_schema(historial) -> dict:
    return {
        "HistoryID": historial[0],
        "PetID": historial[1],
        "Descripcion": historial[2],
        "Fecha": historial[3]
    }

# Función para convertir la lista de historiales a diccionario
def historiales_schema(historiales) -> dict:
    return [historial_schema(historial) for historial in historiales]

# Función para convertir los datos de Foro a diccionario
def foro_schema(foro) -> dict:
    return {
        "ForoID": foro[0],
        "Tema": foro[1],
        "Contenido": foro[2],
        "FechaPublicacion": foro[3]
    }

# Función para convertir la lista de foros a diccionario
def foros_schema(foros) -> dict:
    return [foro_schema(foro) for foro in foros]

# Función para convertir los datos de Comentario a diccionario
def comentario_schema(comentario) -> dict:
    return {
        "ComentarioID": comentario[0],
        "ForoID": comentario[1],
        "Comentario": comentario[2],
        "Fecha": comentario[3]
    }

# Función para convertir la lista de comentarios a diccionario
def comentarios_schema(comentarios) -> dict:
    return [comentario_schema(comentario) for comentario in comentarios]

# Función para convertir los datos de Pedido a diccionario
def pedido_schema(pedido) -> dict:
    return {
        "PedidoID": pedido[0],
        "ClientID": pedido[1]
    }

# Función para convertir la lista de pedidos a diccionario
def pedidos_schema(pedidos) -> dict:
    return [pedido_schema(pedido) for pedido in pedidos]

# Función para convertir los datos de PedidoDetalle a diccionario
def pedido_detalle_schema(pedido_detalle) -> dict:
    return {
        "DetalleID": pedido_detalle[0],
        "PedidoID": pedido_detalle[1],
        "ProductoID": pedido_detalle[2],
        "Cantidad": pedido_detalle[3],
        "Precio": pedido_detalle[4]
    }

# Función para convertir la lista de detalles de pedido a diccionario
def pedido_detalles_schema(pedido_detalles) -> dict:
    return [pedido_detalle_schema(pedido_detalle) for pedido_detalle in pedido_detalles]
