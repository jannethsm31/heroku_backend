import fastapi
import sqlite
from pydantic import BaseModel
from fastapi.middleware import CORSMiddleware

conn = sqlite3.connect("sql/contactos.db")

app = fastapi.FastAPI()

origins = [
    "heroku http"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentiales = True,
    allow_methods = ["*"],
    allow_header = ["*"]
)

class Contacto(BaseModel):
    email : str
    nombre : str 
    telefono : str

@app.get("/")
def inicio():
    return {'Developer by': 'Yo'}

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Nuevo contacto"""
    c = conn.cursor()
    c.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
            (contacto.email, contacto.nombre, contacto.telefono))

    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos();
"""Todos los contactos"""
    c = conn.cursor()
    c.execute('SELECT * FROM contactos;')
    respone =[]
    for row in c:
        contacto = {"email":row[0], "nombre":row[1], "telefono":row[2]}
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contactos(email: str):
    """Contactos por email"""
    c = conn.cursor()
    c.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    contacto = None
    for row in c:
        contacto = {"email":row[0], "nombre":row[1], "telefono":row[2]}
    return contacto

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    """Actualiza contacto"""
    c = conn.cursor()
    c.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
        (contacto.nombre, contacto.telefono, email))
    conn.commit()
    return contacto

@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Eliminar contacto"""
    c = conn.cursor()
    c.execute('DELETE FROM contactos WHERE email = ?', (email,))
    conn.commit()
    return {"mensaje":"Contacto eliminado"}
