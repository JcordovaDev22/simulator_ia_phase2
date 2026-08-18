"""
VelocityFlow AI - Engine Core
Gestión del ciclo de simulación y cálculos de separación de aeronaves.
"""
from core.models import Aircraft

class SimulatorEngine:
    def __init__(self, simulation_id: str):
        self.simulation_id = simulation_id
        self.is_running = False

    def start_simulation(self, cycles: int = 1):
        """Simula la ejecución de ciclos de control de tráfico aéreo."""
        self.is_running = True
        # Lógica de simulación de ciclos
        self.is_running = False

def calculate_separation_distance(ac1: Aircraft, ac2: Aircraft) -> float:
    """
    Calcula la distancia de separación entre dos aeronaves 
    y retorna el valor estimado en millas náuticas (NM).
    """
    lat_diff = abs(ac1.latitude - ac2.latitude)
    lon_diff = abs(ac1.longitude - ac2.longitude)
    
    distance_nm = ((lat_diff ** 2 + lon_diff ** 2) ** 0.5) * 60.0
    return round(distance_nm, 2)

def evaluate_safety_separation(distance_nm: float, minimum_required_nm: float = 5.0) -> bool:
    """
    Evalúa si la separación actual cumple con el estándar mínimo de seguridad.
    """
    return distance_nm >= minimum_required_nm