# /server/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar variables de entorno (para la configuración de la DB, etc.)
load_dotenv()

# --- Configuración Básica de Flask y CORS ---
app = Flask(__name__)

# Configura CORS: CLAVE para permitir que Next.js (puerto 3000) acceda a Flask (puerto 5000)
# En un entorno de producción, cambiarías esta lista por el dominio real.
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# --- Rutas de Prueba y Funcionales ---

@app.route('/')
def home():
    """Ruta de prueba para verificar que el servidor esté funcionando."""
    return jsonify({"status": "running", "service": "Plateia API"})

@app.route('/api/seats', methods=['GET'])
def get_seats_status():
    """Ruta del Sprint 1: Devuelve el estado inicial de la sala."""
    # En este punto, devolverías datos simulados antes de conectar la DB.
    # Después, esta función llamará al servicio de la base de datos.
    
    simulated_data = {
        "sala_id": 1,
        "asientos": [
            {"id": "A1", "estado": "ocupado", "precio": 10},
            {"id": "A2", "estado": "disponible", "precio": 10}
            # ... más datos
        ]
    }
    return jsonify(simulated_data)

@app.route('/api/reserve', methods=['POST'])
def toggle_seat_reservation():
    """Ruta del Sprint 2: Lógica de selección/deselección de asiento."""
    data = request.get_json()
    seat_id = data.get('seatId')
    user_id = "USER_MOCK_123"  # Sustituir con la lógica real de sesión/token

    # 1. Ejecutar la lógica de negocio y la validación aquí.
    # 2. Actualizar la DB (tabla de reservas temporales).
    
    return jsonify({
        "status": "success", 
        "seatId": seat_id,
        "newState": "seleccionado"
    })

# --- Ejecución del Servidor ---
if __name__ == '__main__':
    # Obtener el puerto desde el .env o usar 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port) # debug=True es bueno para desarrollo