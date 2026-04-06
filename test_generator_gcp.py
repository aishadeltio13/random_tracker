from random_movement import PersonMovementGenerator
from google.cloud import pubsub_v1
import json
import random

# Configuración de Pub/Sub
PROJECT_ID = "dataproject2-492516"  # Reemplaza con tu ID de proyecto real
TOPIC_ID = "topic-ingesta-entrenamientos"

def main():
    print("Inicializando el generador para Valencia...")
    generator = PersonMovementGenerator(place_name="Valencia, Valencian Community, Spain")

    # 1. Generar variables aleatorias para la sesión
    puntos_ruta = random.randint(2, 8) 
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

    # 4. Inicializar el cliente publicador de Pub/Sub
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

    # 5. Formatear y publicar el mensaje
    # Pub/Sub requiere que el payload sea un string de bytes
    data_str = json.dumps(payload_ingesta)
    data_bytes = data_str.encode("utf-8")

    print(f"Publicando mensaje en el topic: {TOPIC_ID}...")
    future = publisher.publish(topic_path, data=data_bytes)
    
    # future.result() bloquea la ejecución hasta que se confirme la publicación
    message_id = future.result()
    print(f"Mensaje publicado exitosamente. ID del mensaje en Pub/Sub: {message_id}")

if __name__ == "__main__":
    main()