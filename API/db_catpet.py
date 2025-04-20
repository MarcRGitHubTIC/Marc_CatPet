from client import db_client

def get_clientes():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Cliente")
        clientes = cur.fetchall()
        return clientes

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_mascotas():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM mascota")
        mascotas = cur.fetchall()
        return mascotas

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_clienteMascotas():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM ClienteMascota")
        clientemascotas = cur.fetchall()
        return clientemascotas

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_productos():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Productos")
        productos = cur.fetchall()
        return productos

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_veterinarias():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Veterinaria")
        veterinarias = cur.fetchall()
        return veterinarias

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_veterinarios():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Veterinario")
        veterinarios = cur.fetchall()
        return veterinarios

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_historiales():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Historial")
        historiales = cur.fetchall()
        return historiales

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_foros():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Foro")
        foros = cur.fetchall()
        return foros

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_comentarios():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Comentario")
        comentarios = cur.fetchall()
        return comentarios

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_pedidos():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM Pedido")
        pedidos = cur.fetchall()
        return pedidos

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def get_pedido_detalles():
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        cur.execute("SELECT * FROM PedidoDetalle")
        pedido_detalles = cur.fetchall()
        return pedido_detalles

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()

def insert_cliente(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = """INSERT INTO Cliente (fullName, correo, telefono, premium, user, pwd) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cur.execute(sql, (data["fullName"], data["correo"], data["telefono"], data["premium"], data["user"], data["pwd"]))
        conn.commit()
        return {"status": 1, "message": "Cliente insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar cliente: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_mascota(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO mascota (name) VALUES (%s)"
        cur.execute(sql, (data["name"],))
        conn.commit()
        return {"status": 1, "message": "Mascota insertada correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar mascota: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_clienteMascota(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO ClienteMascota (clientID, petID) VALUES (%s, %s)"
        cur.execute(sql, (data["clientID"], data["petID"]))
        conn.commit()
        return {"status": 1, "message": "ClienteMascota insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar ClienteMascota: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_producto(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO Productos (nombre, descripcion, precio) VALUES (%s, %s, %s)"
        cur.execute(sql, (data["nombre"], data["descripcion"], data["precio"]))
        conn.commit()
        return {"status": 1, "message": "Producto insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar producto: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_veterinaria(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO Veterinaria (calle, nombre, telefono, correo) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (data["calle"], data["nombre"], data["telefono"], data["correo"]))
        conn.commit()
        return {"status": 1, "message": "Veterinaria insertada correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar veterinaria: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_veterinario(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO Veterinario (nombre, licencia, clinicaID) VALUES (%s, %s, %s)"
        cur.execute(sql, (data["nombre"], data["licencia"], data["clinicaID"]))
        conn.commit()
        return {"status": 1, "message": "Veterinario insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar veterinario: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_historial(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO Historial (fechaRegis, motivo, descripcion, mascotaID) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (data["fechaRegis"], data["motivo"], data["descripcion"], data["mascotaID"]))
        conn.commit()
        return {"status": 1, "message": "Historial insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar historial: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
            
def insert_foro(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO Foro (tema, pregunta, usuario, fechaCreacion) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (data["tema"], data["pregunta"], data["usuario"], data["fechaCreacion"]))
        conn.commit()
        return {"status": 1, "message": "Publicación en el foro insertada correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar en el foro: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_comentario(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO Comentario (hiloID, usuario,  contenido, fechaComentario) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (data["hiloID"],  data["usuario"], data["contenido"], data["fechaComentario"]))
        conn.commit()
        return {"status": 1, "message": "Comentario insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar comentario: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
            
def insert_pedido(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        # Cambia aquí para pasar una tupla con el valor de clienteID
        sql = "INSERT INTO Pedido (clienteID) VALUES (%s)"
        cur.execute(sql, (data["clienteID"],))  # Añadir la coma hace que sea una tupla
        conn.commit()
        return {"status": 1, "message": "Pedido insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar pedido: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def insert_pedido_detalle(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()
        sql = "INSERT INTO PedidoDetalle (pedidoID, referencia, cantidad) VALUES (%s, %s, %s)"
        cur.execute(sql, (data["pedidoID"], data["referencia"], data["cantidad"]))
        conn.commit()
        return {"status": 1, "message": "Detalle de pedido insertado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al insertar detalle de pedido: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
            
def update_cliente(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()
        fields = []
        values = []

        # Construimos dinámicamente los campos que se actualizarán
        if "fullName" in data:
            fields.append("fullName = %s")
            values.append(data["fullName"])
        if "correo" in data:
            fields.append("correo = %s")
            values.append(data["correo"])
        if "telefono" in data:
            fields.append("telefono = %s")
            values.append(data["telefono"])
        if "premium" in data:
            fields.append("premium = %s")
            values.append(data["premium"])
        if "user" in data:
            fields.append("user = %s")
            values.append(data["user"])
        if "pwd" in data:
            fields.append("pwd = %s")
            values.append(data["pwd"])

        # Si no hay campos para actualizar, devolvemos un error
        if not fields:
            return {"status": -1, "message": "No hay campos válidos para actualizar"}

        # Agregamos el clientID al final
        values.append(data["clientID"])

        # Construimos la consulta con los campos dinámicos
        sql = f"UPDATE Cliente SET {', '.join(fields)} WHERE clientID = %s"
        cur.execute(sql, values)
        conn.commit()

        return {"status": 1, "message": "Cliente actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar cliente: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
      
def update_mascota(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Mascota SET "
        updates = []
        params = []

        if "name" in data:
            updates.append("name = %s")
            params.append(data["name"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE petID = %s"
        params.append(data["petID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Mascota actualizada correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar mascota: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
            
def update_clienteMascota(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE ClienteMascota SET "
        updates = []
        params = []

        if "clientID" in data:
            updates.append("clientID = %s")
            params.append(data["clientID"])
        if "petID" in data:
            updates.append("petID = %s")
            params.append(data["petID"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE clientID = %s AND petID = %s"
        params.append(data["clientID"])
        params.append(data["petID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "ClienteMascota actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar ClienteMascota: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_producto(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Productos SET "
        updates = []
        params = []

        if "nombre" in data:
            updates.append("nombre = %s")
            params.append(data["nombre"])
        if "descripcion" in data:
            updates.append("descripcion = %s")
            params.append(data["descripcion"])
        if "precio" in data:
            updates.append("precio = %s")
            params.append(data["precio"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE referencia = %s"
        params.append(data["productID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Producto actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar producto: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_veterinaria(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Veterinaria SET "
        updates = []
        params = []

        if "calle" in data:
            updates.append("calle = %s")
            params.append(data["calle"])
        if "nombre" in data:
            updates.append("nombre = %s")
            params.append(data["nombre"])
        if "telefono" in data:
            updates.append("telefono = %s")
            params.append(data["telefono"])
        if "correo" in data:
            updates.append("correo = %s")
            params.append(data["correo"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE clinicaID = %s"
        params.append(data["clinicaID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Veterinaria actualizada correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar veterinaria: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
            
def update_veterinario(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Veterinario SET "
        updates = []
        params = []

        if "nombre" in data:
            updates.append("nombre = %s")
            params.append(data["nombre"])
        if "licencia" in data:
            updates.append("licencia = %s")
            params.append(data["licencia"])
        if "clinicaID" in data:
            updates.append("clinicaID = %s")
            params.append(data["clinicaID"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE vetID = %s"
        params.append(data["vetID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Veterinario actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar veterinario: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_historial(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Historial SET "
        updates = []
        params = []

        if "fechaRegis" in data:
            updates.append("fechaRegis = %s")
            params.append(data["fechaRegis"])
        if "motivo" in data:
            updates.append("motivo = %s")
            params.append(data["motivo"])
        if "descripcion" in data:
            updates.append("descripcion = %s")
            params.append(data["descripcion"])
        if "mascotaID" in data:
            updates.append("mascotaID = %s")
            params.append(data["mascotaID"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE historyID = %s"
        params.append(data["historyID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Historial actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar historial: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_foro(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Foro SET "
        updates = []
        params = []

        if "tema" in data:
            updates.append("tema = %s")
            params.append(data["tema"])
        if "pregunta" in data:
            updates.append("pregunta = %s")
            params.append(data["pregunta"])
        if "usuario" in data:
            updates.append("usuario = %s")
            params.append(data["usuario"])
        if "fechaCreacion" in data:
            updates.append("fechaCreacion = %s")
            params.append(data["fechaCreacion"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE hiloID = %s"
        params.append(data["hiloID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Publicación en el foro actualizada correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar el foro: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_comentario(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Comentario SET "
        updates = []
        params = []

        if "hiloID" in data:
            updates.append("hiloID = %s")
            params.append(data["hiloID"])
        if "usuario" in data:
            updates.append("usuario = %s")
            params.append(data["usuario"])
        if "contenido" in data:
            updates.append("contenido = %s")
            params.append(data["contenido"])
        if "fechaComentario" in data:
            updates.append("fechaComentario = %s")
            params.append(data["fechaComentario"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE comentarioID = %s"
        params.append(data["comentarioID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Comentario actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar el comentario: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_pedido(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE Pedido SET "
        updates = []
        params = []

        if "clienteID" in data:
            updates.append("clienteID = %s")
            params.append(data["clienteID"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE pedidoID = %s"
        params.append(data["pedidoID"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Pedido actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar pedido: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def update_pedido_detalle(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn

    try:
        cur = conn.cursor()

        sql = "UPDATE PedidoDetalle SET "
        updates = []
        params = []

        if "pedidoID" in data:
            updates.append("pedidoID = %s")
            params.append(data["pedidoID"])
        if "referencia" in data:
            updates.append("referencia = %s")
            params.append(data["referencia"])
        if "cantidad" in data:
            updates.append("cantidad = %s")
            params.append(data["cantidad"])

        if not updates:
            return {"status": -1, "message": "No hay campos para actualizar"}

        sql += ", ".join(updates) + " WHERE pedidoID = %s AND referencia = %s"
        params.append(data["pedidoID"])
        params.append(data["referencia"])

        cur.execute(sql, tuple(params))
        conn.commit()

        return {"status": 1, "message": "Detalle de pedido actualizado correctamente"}

    except Exception as e:
        return {"status": -1, "message": f"Error al actualizar el detalle de pedido: {e}"}

    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
            
def delete_cliente(data):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        
        # Extraer correctamente el ID
        clientID = data.get("clienteID")  
        if clientID is None:
            return {"status": -1, "message": "clientID es requerido"}

        sql = "DELETE FROM Cliente WHERE clientID = %s"
        cur.execute(sql, (clientID,))
        conn.commit()
        return {"status": 1, "message": "Cliente eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar cliente: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def delete_mascota(petID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM mascota WHERE petID = %s"
        cur.execute(sql, (petID,))
        conn.commit()
        return {"status": 1, "message": "Mascota eliminada correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar mascota: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def delete_clienteMascota(clientMascotaID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM ClienteMascota WHERE clientMascotaID = %s"
        cur.execute(sql, (clientMascotaID,))
        conn.commit()
        return {"status": 1, "message": "ClienteMascota eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar ClienteMascota: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def delete_producto(productoID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Productos WHERE productoID = %s"
        cur.execute(sql, (productoID,))
        conn.commit()
        return {"status": 1, "message": "Producto eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar producto: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
    
def delete_veterinaria(clinicaID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Veterinaria WHERE clinicaID = %s"
        cur.execute(sql, (clinicaID,))
        conn.commit()
        return {"status": 1, "message": "Veterinaria eliminada correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar veterinaria: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def delete_veterinario(vetID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Veterinario WHERE vetID = %s"
        cur.execute(sql, (vetID,))
        conn.commit()
        return {"status": 1, "message": "Veterinario eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar veterinario: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def delete_historial(historialID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Historial WHERE historialID = %s"
        cur.execute(sql, (historialID,))
        conn.commit()
        return {"status": 1, "message": "Historial eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar historial: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

def delete_foro(hiloID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Foro WHERE hiloID = %s"
        cur.execute(sql, (hiloID,))
        conn.commit()
        return {"status": 1, "message": "Publicación en el foro eliminada correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar en el foro: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
    
def delete_comentario(comentarioID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Comentario WHERE comentarioID = %s"
        cur.execute(sql, (comentarioID,))
        conn.commit()
        return {"status": 1, "message": "Comentario eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar comentario: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
    
def delete_pedido(pedidoID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM Pedido WHERE pedidoID = %s"
        cur.execute(sql, (pedidoID,))
        conn.commit()
        return {"status": 1, "message": "Pedido eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar pedido: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()
    
def delete_pedido_detalle(detalleID):
    conn = db_client()
    if isinstance(conn, dict):
        return conn
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM PedidoDetalle WHERE detalleID = %s"
        cur.execute(sql, (detalleID,))
        conn.commit()
        return {"status": 1, "message": "Detalle de pedido eliminado correctamente"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error al eliminar detalle de pedido: {e}"}
    
    finally:
        if conn and hasattr(conn, "close"):
            conn.close()

# Endpoint especificos

# Login para usuario
def get_login(user):
    conn = db_client()
    if isinstance(conn, dict):
        return conn  

    try:
        cur = conn.cursor()  
        sql = "SELECT * FROM Cliente WHERE user = %s"
        cur.execute(sql, (user,))
        cliente = cur.fetchone()
        return cliente

    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()
            
def register_user(data):
    conn = db_client
    if isinstance(conn, dict):
        return conn
    try: 
        cur = conn.cursor()
        sql = "INSERT INTO Cliente (fullName, correo, telefono, premium, user, pwd) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (data["fullName"], data["correo"], data["telefono"], data["premium"], data["user"], data["pwd"]))
        conn.commit()
        
    except Exception as e:
        return {"status": -1, "message": f"Error en la consulta: {e}"}  

    finally:
        if conn and hasattr(conn, "close"):  
            conn.close()