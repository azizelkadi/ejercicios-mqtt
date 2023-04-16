from paho.mqtt.client import Client
from sys import argv

BROKER = 'simba.fdi.ucm.es'
TOPIC = 'clients/pruebas'

# Función on_message
def on_message(mqttc, userdata, msg):
    print("on_message", userdata, msg.topic, msg.payload)
    if msg.topic != TOPIC:
        mqttc.publish(TOPIC, msg.payload)

# Función main
def main():
    # Inicializamos el cliente MQTT
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
