from paho.mqtt.client import Client
import paho.mqtt.publish as publish
from multiprocessing import Process
from time import sleep
from sys import argv

BROKER = 'simba.fdi.ucm.es'
TOPIC = 'clients/temporizador'

# Función para extraer la información y publicar
def consumir(mensaje):
    # Extraemos la información
    topic, espera, text = mensaje[2:-1].split(",")
    # Esperamos el tiempo de espera indicado
    sleep(int(espera))
    # Publicamos el mensaje enviado en el topic indicado
    publish.single(topic, payload = text, hostname = BROKER)
    print("Se ha consumido: ", mensaje)

# Función on_message
def on_message(mqttc, userdata, msg):
    print("on_message", msg.topic, msg.payload)
    consumidor = Process(target = consumir, args = (str(msg.payload),))
    consumidor.start()

# Función main
def main():
    mqttc = Client()
    mqttc.on_message = on_message
    mqttc.connect(BROKER)
    mqttc.subscribe(TOPIC)
    mqttc.loop_forever()

if __name__ == "__main__":
    
    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 3:
        BROKER = argv[1]
        TOPIC = argv[2]
    else:
        pass

    main()