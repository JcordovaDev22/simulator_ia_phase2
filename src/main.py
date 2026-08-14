from core.simulator_engine import SimulatorEngine

if __name__ == "__main__":
    print("========================================")
    print("   INICIANDO SIMULADOR IA - FASE 2      ")
    print("========================================")
    
    engine = SimulatorEngine(simulation_id="SIM-2026-08A")
    engine.start_simulation(cycles=3)