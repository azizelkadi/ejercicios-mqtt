import paho.mqtt.publish as publish
from time import sleep
from sys import argv

BROKER = "simba.fdi.ucm.es"
TOPIC = "clients/pruebas"

# Función main
def main(mensaje):
    while True:
        # Enviamos el mensaje
        publish.single(TOPIC, mensaje, hostname=BROKER)
        print("Mensaje enviado")
        # Esperamos 3s para enviar de nuevo el mensaje
        sleep(3)

if __name__ == "__main__":
    
    mensaje = input("Ingresa el mensaje que desea enviar en bucle:")

    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 3:
        BROKER = argv[1]
        TOPIC = argv[2]
    else:
        pass

    main(mensaje)