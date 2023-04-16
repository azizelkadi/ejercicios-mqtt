from paho.mqtt.client import Client
from sys import argv

BROKER = 'simba.fdi.ucm.es'
TOPIC_TEMP = 'temperature/t1'  # Por defecto tomamos el sensor t1
TOPIC_HUM = 'humidity'

# Función on_message
def on_message(mqttc, limites, msg):
    print(f'on_message: {msg.topic}: {msg.payload}')

    if limites['flag'] == 0:
        temperatura = int(msg.payload)
        if temperatura > limites['limite_temp']:
            print(f'Umbral superado con valor {temperatura}, suscripción a {TOPIC_HUM}')
            mqttc.subscribe(TOPIC_HUM)
            limites['flag'] = 1

    elif limites['flag'] == 1:
        if msg.topic == TOPIC_HUM:
            humedad = int(msg.payload)
            if humedad > limites['limite_hum']:
                print(f'Umbral superado en {msg.topic} con valor {humedad}, suscripción cancelada')
                mqttc.unsubscribe(TOPIC_HUM)
                limites['flag'] = 0

        elif msg.topic == TOPIC_TEMP:
            temperatura = int(msg.payload)
            if temperatura < limites['limite_temp']:
                print(f'Umbral superado en {msg.topic} con valor {temperatura}, suscripción cancelada')
                mqttc.unsubscribe(TOPIC_HUM)
                limites['flag'] = 0

# Función main
def main():
    # Inicializamos diccionario para almacenar datos obtenidos
    limites = {'limite_temp': 20,
               'limite_hum': 80,
               'flag': 0}
    
    # Inicializamos el cliente MQTT
    mqttc = Client(userdata=limites)
    mqttc.on_message = on_message
    mqttc.enable_logger()
    mqttc.connect(BROKER)
    mqttc.subscribe(TOPIC_TEMP)
    mqttc.loop_forever()

if __name__ == "__main__":
    
    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 4:
        BROKER = argv[1]
        TOPIC_TEMP = argv[2]
        TOPIC_HUM = argv[3]
    else:
        pass

    main()
