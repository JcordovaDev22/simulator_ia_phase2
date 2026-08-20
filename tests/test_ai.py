"""
Unit tests for VelocityFlow AI Aircraft Models and Separation Logic
"""
from core.ai_models import Aircraft
from core.physics_engine import calculate_separation_distance, evaluate_safety_separation

def test_aircraft_initialization():
    """Valida la correcta instanciación de los atributos de la aeronave."""
    ac = Aircraft(
        callsign="FLT-101", 
        latitude=10.0, 
        longitude=-70.0, 
        altitude=30000, 
        speed_knots=450.0
    )
    assert ac.callsign == "FLT-101"
    assert ac.altitude == 30000
    assert ac.speed_knots == 450.0

def test_separation_distance_calculation():
    """Verifica que el cálculo matemático de separación devuelva valores válidos en NM."""
    ac1 = Aircraft(callsign="FLT-101", latitude=10.0, longitude=-70.0, altitude=30000, speed_knots=450.0)
    ac2 = Aircraft(callsign="FLT-102", latitude=10.1, longitude=-70.1, altitude=32000, speed_knots=480.0)
    
    distance = calculate_separation_distance(ac1, ac2)
    assert distance > 0.0
    assert isinstance(distance, float)

def test_safety_separation_compliance():
    """Valida los umbrales mínimos de seguridad en millas náuticas (NM)."""
    assert evaluate_safety_separation(6.5, minimum_required_nm=5.0) is True
    assert evaluate_safety_separation(3.2, minimum_required_nm=5.0) is False