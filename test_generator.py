from random_movement import PersonMovementGenerator
from google.cloud import pubsub_v1
import json
import random

# Configuración de Pub/Sub
PROJECT_ID = "dataproject2-492516"  # Reemplaza con el ID de tu proyecto
TOPIC_ID = "topic-ingesta-entrenamientos"

def main():
    # 1. Instanciar el generador para Valencia
    print("Descargando red de calles de Valencia...")
    generator = PersonMovementGenerator(place_name="Valencia, Valencian Community, Spain")

    # 2. Generar un movimiento aleatorio
    movimiento = generator.generate_timed_movement(
        num_waypoints=5,
        speed_mps=2.5 
    )

    # 3. Estructurar el payload final
    payload_ingesta = {
        "jugador_id": f"jugador_{random.randint(1000, 9999)}",
        "disciplina": "running",
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