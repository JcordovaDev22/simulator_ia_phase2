"""
VelocityFlow AI - Aircraft Models
Definición de esquemas de datos con Pydantic.
"""
from pydantic import BaseModel, Field

class Aircraft(BaseModel):
    callsign: str = Field(..., description="Identificador de la aeronave")
    latitude: float = Field(..., description="Latitud actual")
    longitude: float = Field(..., description="Longitud actual")
    altitude: int = Field(..., description="Altitud en pies")
    speed_knots: float = Field(..., description="Velocidad en nudos")