from paho.mqtt.client import Client
from sys import argv

BROKER = 'simba.fdi.ucm.es'
TOPIC = 'clients/temporizador'

def on_message(mqttc, userdata, msg):
    print(f'on_message topic: {msg.topic}, payload: {msg.payload}')
    
def main():
    mqttc = Client()
    mqttc.on_message = on_message
    mqttc.connect(BROKER)
    final_topics = ["clients/topic1", "clients/topic2"]
    for subt in final_topics:
        mqttc.subscribe(subt)
    mqttc.loop_start()

    pruebas = [(final_topics[0], "1", "Primera prueba"), 
               (final_topics[0], "3", "Segunda prueba"), 
               (final_topics[1], "5", "Tercera prueba"),]
    
    for p in pruebas:
        mqttc.publish(TOPIC, ','.join(p))

if __name__ == "__main__":
    
    if len(argv) == 2:
        BROKER = argv[1]
    elif len(argv) == 3:
        BROKER = argv[1]
        TOPIC = argv[2]
    else:
        pass

    main()
