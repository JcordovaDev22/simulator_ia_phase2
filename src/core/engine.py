import logging
import random
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SimulatorEngine:
    def __init__(self, simulation_id: str):
        self.simulation_id = simulation_id
        self.is_running = False

    def start_simulation(self, cycles: int = 3):
        """Ejecuta los ciclos de simulación y detecta posibles anomalías."""
        logging.info(f"Iniciando simulación ID: {self.simulation_id}")
        self.is_running = True

        for cycle in range(1, cycles + 1):
            logging.info(f"Ejecutando ciclo {cycle}/{cycles}...")
            time.sleep(1)
            
            # Simulando lectura de métricas de rendimiento y estado del vuelo
            metric_load = random.randint(50, 100)
            logging.info(f"Métrica de carga del sistema: {metric_load}%")
            
            if metric_load > 85:
                self.handle_anomaly(cycle, metric_load)

        self.is_running = False
        logging.info("Simulación finalizada exitosamente.")

    def handle_anomaly(self, cycle: int, load: float):
        """Gestiona el registro de la anomalía detectada."""
        logging.warning(f"¡ANOMALÍA DETECTADA en ciclo {cycle}! Carga crítica: {load}%")
        # Aquí integraremos la llamada al conector de Jira para automatizar el ticket