from paho.mqtt.client import Client
from time import sleep
from sys import argv
from numpy import mean

BROKER = 'simba.fdi.ucm.es'
TOPIC = 'temperature/#'

# Función on_message
def on_message(mqttc, data, msg):
    # Temperatura registrada
    temperatura = float(msg.payload)
    print('on_message', msg.topic, temperatura)
    
    # Añadimos datos del sensor correspondiente
    sensor = msg.topic[-2:]
    data[sensor] = data.get(sensor, []) + [temperatura]
    print('on_message', data)

# Función para calcular los resultados
def calc_informacion(data):
    informacion = {}
    
    for sensor, temperaturas in data.items():
        # Obtenemos las estadisticas
        maximo = max(temperaturas)
        minimo = min(temperaturas)
        media = mean(temperaturas)
        # Guardamos la información
        informacion[sensor] = {'max': maximo, 'min': minimo, 'media': media}
    
    # Calculamos las estadísticas totales
    data_total = [item for sensor_lista in data.values() for item in sensor_lista]
    maximo_total = max(data_total)
    minimo_total = min(data_total)
    media_total = mean(data_total)
    informacion['total'] = {'max': maximo_total, 'min': minimo_total, 'media': media_total}

    return informacion

# Función main
def main():
    # Inicializamos diccionario para almacenar datos obtenidos
    data = {}

    # Inicializamos el cliente MQTT
    mqttc = Client(userdata=data)
    mqttc.on_message = on_message
    mqttc.connect(BROKER)
    mqttc.subscribe(TOPIC)
    mqttc.loop_start()

    # Esperamos 8s para recibir los datos
    sleep(8)

    # Obtenemos y mostramos las estadísticas pedidas
    informacion = calc_informacion(data)
    print('\nRESULTADOS:')
    for sensor, info in informacion.items():
        print(f'\n{sensor}:')
        for metrica, valor in info.items():
            print(f'{metrica}: {valor}')

if __name__ == "__main__":
    
    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 3:
        BROKER = argv[1]
        TOPIC = argv[2]
    else:
        pass

    main()
