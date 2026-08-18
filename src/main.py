"""
VelocityFlow AI - Main Entry Point
Flight Simulator AI Phase 2 Backend
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="VelocityFlow AI API",
    description="Backend para el simulador de vuelo y gestión de tráfico aéreo - Fase 2",
    version="2.0.0"
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": "VelocityFlow AI Flight Simulator",
        "phase": "Phase 2"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    # Tu menú de bienvenida original en consola
    print("========================================")
    print("   INICIANDO SIMULADOR IA - FASE 2      ")
    print("========================================")
    print(" Sistema de control y API activo...")
    
    # Arranque del servidor web
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)