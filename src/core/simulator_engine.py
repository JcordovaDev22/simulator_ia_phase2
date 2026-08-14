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
            
            # Simulando lectura de métricas de rendimiento
            metric_value = random.uniform(50.0, 105.0)
            logging.info(f"Métrica registrada: {metric_value:.2f}%")
            
            # Detección de anomalías simuladas (> 95%)
            if metric_value > 95.0:
                logging.warning(f"¡Anomalía detectada en el ciclo {cycle}! Valor crítico: {metric_value:.2f}%")
                self.handle_anomaly(metric_value)

        self.is_running = False
        logging.info("Simulación finalizada exitosamente.")

    def handle_anomaly(self, value: float):
        """Prepara el reporte del error para su futura integración con Jira."""
        error_report = {
            "error_code": "ERR_THRESHOLD_EXCEEDED",
            "description": f"El valor métrico superó el límite permitido: {value:.2f}%",
            "severity": "HIGH"
        }
        logging.info(f"Generando reporte de incidencia automatizado: {error_report}")