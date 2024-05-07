# Importa FastAPI
from fastapi import FastAPI

# Importar modelos
from .models import Personaje, PeliculaSerie

# Crea una instancia de la aplicación
app = FastAPI()

# Lista para almacenar personajes
personajes = []

@app.post("/personajes/", tags=["personajes"])
async def crear_personaje(personaje: Personaje):
    personajes.append(personaje)
    return {"message": "Personaje añadido con éxito", "personaje": personaje}

@app.get("/personajes/", tags=["personajes"])
async def listar_personajes():
    return {"personajes": personajes}

# Lista para almacenar películas/series
peliculas_series = []

@app.post("/peliculas-series/", tags=["peliculas/series"])
async def crear_pelicula_serie(pelicula_serie: PeliculaSerie):
    peliculas_series.append(pelicula_serie)
    return {"message": "Pelicula/Serie añadida con éxito", "pelicula_serie": pelicula_serie}

@app.get("/peliculas-series/", tags=["peliculas/series"])
async def listar_peliculas_series():
    return {"peliculas_series": peliculas_series}

@app.put("/peliculas-series/{item_index}", tags=["peliculas/series"])
async def actualizar_pelicula_serie(item_index: int, pelicula_serie: PeliculaSerie):
    if item_index < 0 or item_index >= len(peliculas_series):
        return {"error": "Índice fuera de rango"}
    peliculas_series[item_index] = pelicula_serie
    return {"message": "Pelicula/Serie actualizada con éxito", "pelicula_serie": pelicula_serie}

@app.delete("/peliculas-series/{item_index}", tags=["peliculas/series"])
async def eliminar_pelicula_serie(item_index: int):
    if item_index < 0 or item_index >= len(peliculas_series):
        return {"error": "Índice fuera de rango"}
    peliculas_series.pop(item_index)
    return {"message": "Pelicula/Serie eliminada con éxito"}