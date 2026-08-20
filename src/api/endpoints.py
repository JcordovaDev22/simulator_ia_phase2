from fastapi import FastAPI
from pydantic import BaseModel
from src.core.physics_engine import calcular_separacion # Asumiendo esta estructura

app = FastAPI()

class SimulacionRequest(BaseModel):
    velocidad: float
    tipo_aeronave: str
    condicion_viento: float

@app.post("/calcular-separacion")
async def obtener_separacion(data: SimulacionRequest):
    # Lógica de cálculo de separación náutica
    resultado = calcular_separacion(data.velocidad, data.tipo_aeronave, data.condicion_viento)
    return {"separacion_nm": resultado, "estado": "NORMAL" if resultado > 5 else "ALERTA"}