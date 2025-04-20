from csv import reader
from datetime import datetime
import csv
import io
from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import List, Optional, Union
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import db_catpet
from client import db_client
import catpet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Schemas de las tablas (Pydantic Models)
class ClienteSchema(BaseModel):
    clientID: int
    fullName: str
    correo: str
    telefono: Optional[str]
    premium: bool
    user: str
    pwd: str

class MascotaSchema(BaseModel):
    petID: int
    name: str
    
class ClienteMascotaSchema(BaseModel):
    clientID: int
    petID: int

class ProductoSchema(BaseModel):
    productID: int
    nombre: str
    descripcion: str
    precio: float

class VeterinariaSchema(BaseModel):
    vetID: int
    nombre: str
    direccion: str
    telefono: str

class VeterinarioSchema(BaseModel):
    vetID: int
    nombre: str
    licencia: str
    clinicaID: Optional[int] = None  # Clínica ID es opcional
    telefono: Optional[str] = None  

class HistorialSchema(BaseModel):
    historyID: int
    petID: int
    descripcion: str
    fecha: str

class ForoSchema(BaseModel):
    foroID: int
    tema: str
    contenido: str
    fecha_publicacion: str

class ComentarioSchema(BaseModel):
    comentarioID: int
    foroID: int
    comentario: str
    fecha: str

class PedidoSchema(BaseModel):
    pedidoID: int
    clientID: int

class PedidoDetalleSchema(BaseModel):
    pedidoID: int
    referencia: int
    cantidad: int
    
# Clases especializadas
class LoginSchema(BaseModel):
    correo: str
    pwd: str

# Metodos GET de la API
@app.get("/")
def root():
    return {"message": "API CatPet"}

@app.get("/clientes", response_model=List[ClienteSchema])
def obtener_clientes():
    clientes = db_catpet.get_clientes()

    if isinstance(clientes, dict):  # Si hubo un error en la BD
        return clientes

    # Convertir las tuplas en objetos ClienteSchema
    clientes_dict = [
        ClienteSchema(
            clientID=cliente[0],
            fullName=cliente[1],
            correo=cliente[2],
            telefono=cliente[3] if cliente[3] is not None else "",  # Manejar valores NULL
            premium=bool(cliente[4]),  # Convertir de int a bool
            user=cliente[5],
            pwd=cliente[6]
        ) for cliente in clientes
    ]

    return clientes_dict

@app.get("/mascotas", response_model=List[MascotaSchema])
def obtener_mascotas():
    mascotas = db_catpet.get_mascotas()
    mascotas_dict = []
    
    for m in mascotas: # Verifica que la tupla tenga al menos 4 elementos
        mascotas_dict.append(
            MascotaSchema(
                petID=m[0],       # ID de la mascota
                name=m[1]
            )
        )
    
    return mascotas_dict

@app.get("/clienteMascotas", response_model=List[ClienteMascotaSchema])
def obtener_clienteMascotas():
    clienteMascotas = db_catpet.get_clienteMascotas()
    
    # Verificar si clienteMascotas es None o está vacío y devolver una lista vacía si es necesario
    if not clienteMascotas:
        return []
    
    clienteMascotas_dict = []
    
    for cm in clienteMascotas:  # Verifica que la tupla tenga al menos 2 elementos
        clienteMascotas_dict.append(
            ClienteMascotaSchema(
                clientID=cm[0],  # ID del cliente
                petID=cm[1]      # ID de la mascota
            )
        )
    
    return clienteMascotas_dict

@app.get("/productos", response_model=List[ProductoSchema])
def obtener_productos():
    productos = db_catpet.get_productos()  # Obtén los productos de la base de datos
    if isinstance(productos, list):  # Verifica que los productos sean una lista válida
        return [
            {
                "productID": producto[0],
                "nombre": producto[1],
                "descripcion": producto[2] if producto[2] is not None else "",  # Manejo de valores nulos
                "precio": float(producto[3]) if producto[3] is not None else 0.00  # Convierte Decimal a float
            }
            for producto in productos
        ]  # Convierte las tuplas en diccionarios
    return productos

@app.get("/veterinarias", response_model=List[VeterinariaSchema])
def obtener_veterinarias():
    veterinarias_db = db_catpet.get_veterinarias()  # Obtener datos de la BD

    veterinarias = [
        VeterinariaSchema(
            vetID=vet[0],  # Primer elemento de la tupla es el ID
            nombre=vet[1],  # Segundo elemento es el nombre
            direccion=vet[2],  # Tercer elemento es la dirección
            telefono=vet[3],  # Cuarto elemento es el teléfono
            email=vet[4]      # Quinto elemento es el email
        )
        for vet in veterinarias_db
    ]
    return veterinarias

@app.get("/veterinarios", response_model=List[VeterinarioSchema])
def obtener_veterinarios():
    veterinarios_db = db_catpet.get_veterinarios()  # Obtener datos de la BD

    veterinarios = [
        VeterinarioSchema(
            vetID=vet[0],  # ID del veterinario
            nombre=vet[1],  # Nombre del veterinario
            licencia=vet[2],  # Número de licencia
            clinicaID=vet[3]  # ID de la clínica (puede ser NULL)
        )
        for vet in veterinarios_db
    ]
    return veterinarios

@app.get("/historiales", response_model=List[HistorialSchema])
def obtener_historiales():
    # Obtener los historiales de la base de datos (probablemente una lista de tuplas)
    historiales = db_catpet.get_historiales()

    # Convertir las tuplas a diccionarios con el formato correcto para el esquema
    return [
        {
            "historyID": historial[0],  # Suponiendo que el ID de historial está en la posición 0
            "petID": historial[4],      # Suponiendo que el ID de la mascota está en la posición 4
            "descripcion": historial[3],  # Descripción en la posición 3
            "fecha": str(historial[1])   # Asegúrate de convertir la fecha a cadena
        }
        for historial in historiales
    ]

@app.get("/foros", response_model=List[ForoSchema])
def obtener_foros():
    # Obtener los foros desde la base de datos
    foros = db_catpet.get_foros()

    # Convertir las tuplas a diccionarios que coincidan con ForoSchema
    foros_convertidos = [
        ForoSchema(
            foroID=foro[0],
            tema=foro[1],
            contenido=foro[2],
            fecha_publicacion=foro[3]
        )
        for foro in foros
    ]

    return foros_convertidos

@app.get("/comentarios", response_model=List[ComentarioSchema])
def obtener_comentarios():
    # Recuperar los comentarios de la base de datos
    comentarios_db = db_catpet.get_comentarios()
    
    # Convertir los resultados de la base de datos en una lista de objetos ComentarioSchema
    comentarios = []
    for comentario in comentarios_db:
        # Asumimos que la estructura de la tupla es algo como (comentarioID, foroID, comentario, fecha)
        comentario_obj = ComentarioSchema(
            comentarioID=comentario[0],  # comentarioID
            foroID=comentario[1],        # foroID
            comentario=comentario[2],    # contenido del comentario
            fecha=comentario[3]          # fecha
        )
        comentarios.append(comentario_obj)
    
    return comentarios

@app.get("/pedidos", response_model=List[PedidoSchema])
def obtener_pedidos():
    pedidos = db_catpet.get_pedidos()  # Obtener los pedidos desde la base de datos
    pedidos_dict = []
    
    for p in pedidos:  # Verifica que la tupla tenga al menos 2 elementos
        pedidos_dict.append(
            PedidoSchema(
                pedidoID=p[0],    # ID del pedido
                clientID=p[1]     # ID del cliente
            )
        )
    
    return pedidos_dict

@app.get("/pedido_detalles", response_model=List[PedidoDetalleSchema])
def obtener_pedido_detalles():
    # Obtenemos los datos de la base de datos
    detalles = db_catpet.get_pedido_detalles()
    
    # Convertimos las tuplas a instancias de PedidoDetalleSchema
    return [
        PedidoDetalleSchema(pedidoID=detalle[0], referencia=detalle[1], cantidad=detalle[2])
        for detalle in detalles
    ]

# Metodos POST de la API
@app.post("/insert/clientes/")
async def create_cliente(data: dict):
    return db_catpet.insert_cliente(data)

@app.post("/insert/mascotas/")
async def create_mascota(data: dict):
    return db_catpet.insert_mascota(data)

@app.post("/insert/clienteMascotas/")
async def create_clienteMascota(data: dict):
    return db_catpet.insert_cliente(data)

@app.post("/insert/productos/")
async def create_producto(data: dict):
    return db_catpet.insert_producto(data)

@app.post("/insert/veterinarias/")
async def create_veterinaria(data: dict):
    return db_catpet.insert_veterinaria(data)

@app.post("/insert/veterinarios/")
async def create_veterinario(data: dict):
    return db_catpet.insert_veterinario(data)

@app.post("/insert/historiales/")
async def create_historial(data: dict):
    return db_catpet.insert_historial(data)

@app.post("/insert/foro/")
async def create_foro(data: dict):
    return db_catpet.insert_foro(data)

@app.post("/insert/comentario/")
async def create_comentario(data: dict):
    return db_catpet.insert_comentario(data)

@app.post("/insert/pedidos/")
async def create_pedido(data: dict):
    return db_catpet.insert_pedido(data)

@app.post("/insert/pedido_detalles/")
async def create_pedido_detalle(data: dict):
    return db_catpet.insert_pedido_detalle(data)    

# Metodos UPDATE de la API
@app.put("/update/clientes/")
async def update_cliente(data: dict):
    return db_catpet.update_cliente(data)

@app.put("/update/mascotas/")
async def update_mascota(data: dict):
    return db_catpet.update_mascota(data)

@app.put("/update/clienteMascotas/")
async def update_clienteMascota(data: dict):
    return db_catpet.update_clienteMascota(data)

@app.put("/update/productos/")
async def update_producto(data: dict):
    return db_catpet.update_producto(data)

@app.put("/update/veterinarias/")
async def update_veterinaria(data: dict):
    return db_catpet.update_veterinaria(data)

@app.put("/update/veterinarios/")
async def update_veterinario(data: dict):
    return db_catpet.update_veterinario(data)

@app.put("/update/historiales/")
async def update_historial(data: dict):
    return db_catpet.update_historial(data)

@app.put("/update/foro/")
async def update_foro(data: dict):
    return db_catpet.update_foro(data)

@app.put("/update/comentario/")
async def update_comentario(data: dict):
    return db_catpet.update_comentario(data)

@app.put("/update/pedidos/")
async def update_pedido(data: dict):
    return db_catpet.update_pedido(data)

@app.put("/update/pedido_detalles/")
async def update_pedido_detalle(data: dict):
    return db_catpet.update_pedido_detalle(data)

# Metodos DELETE de la API
@app.delete("/delete/clientes/")
async def delete_cliente(data: dict):
    return db_catpet.delete_cliente(data)

@app.delete("/delete/mascotas/")
async def delete_mascota(data: dict):
    return db_catpet.delete_mascota(data)

@app.delete("/delete/clienteMascotas/")
async def delete_clienteMascota(data: dict):
    return db_catpet.delete_clienteMascota(data)

@app.delete("/delete/productos/")
async def delete_producto(data: dict):
    return db_catpet.delete_producto(data)

@app.delete("/delete/veterinarias/")
async def delete_veterinaria(data: dict):
    return db_catpet.delete_veterinaria(data)

@app.delete("/delete/veterinarios/")
async def delete_veterinario(data: dict):
    return db_catpet.delete_veterinario(data)

@app.delete("/delete/historiales/")
async def delete_historial(data: dict):
    return db_catpet.delete_historial(data)

@app.delete("/delete/foro/")
async def delete_foro(data: dict):
    return db_catpet.delete_foro(data)

@app.delete("/delete/comentario/")
async def delete_comentario(data: dict):
    return db_catpet.delete_comentario(data)

@app.delete("/delete/pedidos/")
async def delete_pedido(data: dict):
    return db_catpet.delete_pedido(data)

@app.delete("/delete/pedido_detalles/")
async def delete_pedido_detalle(data: dict):
    return db_catpet.delete_pedido_detalle(data)

    
# Metodos especificos

# Para obtener login con el usuario
@app.get("/clientes/{clientID}", response_model=ClienteSchema)
async def obtener_cliente(clientID: int):
    cliente = db_catpet.get_cliente(clientID)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_catpet.get_login(
        clientID=cliente[0],
        fullName=cliente[1],
        correo=cliente[2],
        telefono=cliente[3] if cliente[3] is not None else "",  # Manejar valores NULL
        premium=bool(cliente[4]),  # Convertir de int a bool
        user=cliente[5],
        pwd=cliente[6]
    )
    
@app.post("/registro")
async def registrar_usuario(data: dict):
    # Por defecto todos los nuevos clientes no son premium
    data["premium"] = False
    return db_catpet.insert_cliente(data)

@app.post("/login")
async def login_usuario(data: LoginSchema):
    return db_catpet.login_cliente_por_correo(data.correo, data.pwd)

# Metodo para registrarse

@app.post("/registro")
async def registrar_usuario(data: dict):
    # Por defecto todos los nuevos clientes no son premium
    data["premium"] = False
    # Insertamos los datos en la base de datos
    return db_catpet.insert_cliente(data)