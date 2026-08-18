"""
VelocityFlow AI - Setup Configuration
"""
from setuptools import setup, find_packages

setup(
    name="simulator_ia_phase_2",
    version="2.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.112.0",
        "uvicorn==0.30.6",
        "pydantic==2.8.2",
        "pytest==8.3.2"
    ],
    description="Backend para el simulador de vuelo y gestión de tráfico aéreo - Fase 2",
    author="José Córdova",
    python_requires=">=3.10",
)