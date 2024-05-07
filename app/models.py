from pydantic import BaseModel, HttpUrl
from datetime import date
from typing import Optional


class Personaje(BaseModel):
    nombre: str
    pelicula_serie: str  # Podríamos referenciar esto más adelante con un modelo propio o un ID
    imagen: Optional[HttpUrl] = None  # URL de la imagen, opcional
    descripcion: Optional[str] = None

class PeliculaSerie(BaseModel):
    nombre: str
    clasificacion: str
    fecha_lanzamiento: date
    revision: Optional[str] = None
    temporada: Optional[int] = None  # Solo relevante para series
