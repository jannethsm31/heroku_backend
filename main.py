import fastapi
import sqlite3
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

conn = sqlite3.connect("sql/contactos.db")

app = fastapi.FastAPI()

origins = [
    
    #"https://herokufrontend-9f0e84a2ceb0.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


class Contacto(BaseModel):
    email : str
    nombre : str
    telefono : str


@app.get("/")
def inicio():
    return {'Developer by':'yo'}


@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    c = conn.cursor()
    c.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
              (contacto.email, contacto.nombre, contacto.telefono))
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    c = conn.cursor()
    c.execute('SELECT * FROM contactos;')
    response = []
    for row in c:
        contacto = {"email":row[0],"nombre":row[1], "telefono":row[2]}
        response.append(contacto)
    return response


@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    c = conn.cursor()
    c.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    contacto = None
    for row in c:
        contacto = {"email":row[0],"nombre":row[1],"telefono":row[2]}
    return contacto


@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    """Actualiza un contacto."""
    c = conn.cursor()
    c.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
              (contacto.nombre, contacto.telefono, email))
    conn.commit()
    return contacto

@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    c = conn.cursor()
    c.execute('DELETE FROM contactos WHERE email = ?', (email,))
    conn.commit()
    return {"mensaje":"Contacto eliminado"}
