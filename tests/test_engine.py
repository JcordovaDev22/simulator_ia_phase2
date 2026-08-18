import sys
import os

# Añade la ruta 'src' al path de Python de forma dinámica
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core.engine import SimulatorEngine

def test_simulator_initialization():
    engine = SimulatorEngine(simulation_id="TEST-SIM-01")
    assert engine.simulation_id == "TEST-SIM-01"
    assert engine.is_running is False

def test_simulator_execution_cycles():
    engine = SimulatorEngine(simulation_id="TEST-SIM-02")
    engine.start_simulation(cycles=1)
    assert engine.is_running is False