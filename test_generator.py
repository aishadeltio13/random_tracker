from random_movement import PersonMovementGenerator
import json
import random

def main():
    # 1. Instanciar el generador para Valencia
    print("Descargando red de calles de Valencia (esto puede tardar unos segundos en la primera ejecución)...")
    generator = PersonMovementGenerator(place_name="Valencia, Valencian Community, Spain")

    # 2. Generar un movimiento aleatorio (simulando una carrera)
    # 2.5 m/s equivale a unos 9 km/h
    movimiento = generator.generate_timed_movement(
        num_waypoints=5,
        speed_mps=2.5 
    )

    # 3. Estructurar el payload final para Pub/Sub
    payload_ingesta = {
        "jugador_id": f"jugador_{random.randint(1000, 9999)}",
        "disciplina": "running",
        "estadisticas_entrenamiento": movimiento
    }

    # 4. Mostrar el resultado por consola
    print("\n--- Payload generado listo para Pub/Sub ---")
    print(json.dumps(payload_ingesta, indent=2))

if __name__ == "__main__":
    main()