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
