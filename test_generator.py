from random_movement import PersonMovementGenerator
import json
import random
import os

def main():
    print("Inicializando el generador para Valencia...")
    generator = PersonMovementGenerator(place_name="Valencia, Valencian Community, Spain")

    # 1. Generar variables aleatorias para la sesión
    # Seleccionamos un número de waypoints aleatorio (entre 2 y 8)
    # Esto determinará indirectamente la duración total de la ruta
    puntos_ruta = random.randint(2, 8) 
    
    # Seleccionamos una velocidad base aleatoria para este jugador
    # Por ejemplo, entre 1.0 m/s (caminar despacio) y 3.5 m/s (correr rápido)
    velocidad_base_jugador = random.uniform(1.0, 3.5)

    print(f"Simulando jugador con velocidad base: {velocidad_base_jugador:.2f} m/s y {puntos_ruta} waypoints.")

    # 2. Generar el movimiento usando las variables aleatorias
    movimiento = generator.generate_timed_movement(
        num_waypoints=puntos_ruta,
        base_speed_mps=velocidad_base_jugador 
    )

    # 3. Estructurar el payload final para la ingesta
    payload_ingesta = {
        "jugador_id": f"jugador_{random.randint(1000, 9999)}",
        "estadisticas_entrenamiento": movimiento
    }

    # 4. Configurar el nombre y la ruta del archivo de salida
    nombre_archivo = "codigo_pedro_modificado.json"
    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
    
    # 5. Guardar el payload
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(payload_ingesta, archivo, indent=4, ensure_ascii=False)

    print(f"Proceso finalizado. Archivo guardado en: {ruta_archivo}")

if __name__ == "__main__":
    main()