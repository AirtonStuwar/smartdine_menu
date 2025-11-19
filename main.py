from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Plato(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool

menu: List[Plato] = []

@app.get("/")
def home():
    return {"msg": "SmartDine Menu API funcionando correctamente"}

@app.get("/menu", response_model=List[Plato])
def obtener_menu():
    return menu

@app.post("/menu", response_model=Plato)
def agregar_plato(plato: Plato):
    menu.append(plato)
    return plato
