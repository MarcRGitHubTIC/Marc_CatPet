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