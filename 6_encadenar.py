from paho.mqtt.client import Client
from sys import argv

BROKER = 'simba.fdi.ucm.es'
TOPIC_NUM = 'numbers'
TOPIC_HUM = 'humidity'

# Función es_primo
def es_primo(n):
    if (not n.is_integer()) or (n < 2):
        return False
    n_int = int(n)
    for i in range(2, int(n_int**0.5) + 1):
        if n_int % i == 0:
            return False
    return True

# Función on_message
def on_message(mqttc, data, msg):
    print(f'on_message: {msg.topic}: {msg.payload}')

    if data['flag'] == 0:
        numero = float(msg.payload)
        if es_primo(numero):
            print(f'{numero} es primo, suscripción a {TOPIC_HUM}')
            mqttc.subscribe(TOPIC_HUM)
            data['flag'] = 1

    elif data['flag'] == 1:
        if msg.topic == TOPIC_HUM:
            humedad = int(msg.payload)
            if humedad > 80:
                print(f'{humedad} supera el umbral, suscripción cancelada')
                mqttc.unsubscribe(TOPIC_HUM)
                data['flag'] = 0

        elif msg.topic == TOPIC_NUM:
            numero = float(msg.payload)
            if not numero.is_integer():
                print(f'{numero} no es un entero, suscripción cancelada')
                mqttc.unsubscribe(TOPIC_HUM)
                data['flag'] = 0

# Función main
def main():
    # Inicializamos diccionario
    data = {'flag': 0}
    
    # Inicializamos el cliente MQTT
    mqttc = Client(userdata=data)
    mqttc.on_message = on_message
    mqttc.enable_logger()
    mqttc.connect(BROKER)
    mqttc.subscribe(TOPIC_NUM)
    mqttc.loop_forever()

if __name__ == "__main__":
    
    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 4:
        BROKER = argv[1]
        TOPIC_NUM = argv[2]
        TOPIC_HUM = argv[3]
    else:
        pass

    main()
