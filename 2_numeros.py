from paho.mqtt.client import Client
from sys import argv
from time import sleep
from numpy import mean

BROKER = 'simba.fdi.ucm.es'
TOPIC = 'numbers'

# Función on_message
def on_message(mqttc, data, msg):
    print("on_message", msg.topic, msg.payload)

    # Consumimos el número
    n = float(msg.payload)
    if n.is_integer():
        data['enteros'] = data['enteros'] + [int(n)]
    else:
        data['reales'] = data['reales'] + [n]
    
    print("on_message", data)

# Función auxiliar 'es_primo'
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

# Función main
def main():
    # Inicializamos diccionario para almacenar datos obtenidos
    data = {'enteros': [], 'reales': []}

    # Inicializamos el cliente MQTT
    mqttc = Client(userdata=data)
    mqttc.on_message = on_message
    mqttc.connect(BROKER)
    mqttc.subscribe(TOPIC)
    mqttc.loop_start()

    # Esperamos 8s para recibir los datos
    sleep(8)

    # Esperamos extra de tiempo si aún no hay datos en algún tipo
    while (len(data['enteros']) * len(data['reales'])) == 0:
        sleep(1)

    # Obtenemos información de los datos
    print('\nRESULTADOS:')
    for tipo, lista in data.items():
        print(f'\n{tipo}: {lista}')
        print(f'Maximo: {max(lista)}')
        print(f'Minimo: {min(lista)}')
        if tipo == 'enteros':
            print(f'Primos: {[n for n in lista if es_primo(n)]}')
        else:
            print(f'Media: {mean(lista)}')

if __name__ == "__main__":
    
    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 3:
        BROKER = argv[1]
        TOPIC = argv[2]
    else:
        pass

    main()
