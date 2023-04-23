# Ejercicios MQTT

Autor: Abdelaziz el Kadi Lachehab

Asignatura: PRPA

Instrucciones generales: Para probar cada ejercicio se deberá ejecutar el fichero (o ficheros) correspondientes. Cada fichero tiene como prefijo el número del ejercicio al que corresponde. Para ejecutarlos debemos dirigirnos al directorio donde tengamos el fichero, y ejecutar el archivo de Python junto con el Broker y el Topic. Por ejemplo: `python 3_temperaturas simba.fdi.ucm.es temperature/#`. Si no se indican esos valores, el programa tomará los valores por defecto. Se **recomienda** ejecutar sin indicar esos argumentos, por ejemplo: `python 3_temperaturas`.

### Ejercicio 1: Prueba Broker
Ejecutar `1_prueba_productor.py` para producir valores de prueba (string `"Mensaje enviado"` en bucle) y luego ejecutar `1_prueba_broker.py` para comprobar que se reciben y publican bien los mensajes. Se debe mostrar pon pantalla el mensaje.

### Ejercicio 2: Números
Ejecutar `2_numeros.py`. Este escuchará el Topic (por defecto `numbers`), recibiendo números reales y enteros. Tras 8 segundos, se clasificarán los números en enteros (indicando cuáles son primos) y reales (indicando la media).

### Ejercicio 3: Temperaturas
Ejecutar `2_temperaturas.py`. Este escuchará el Topic (por defecto `temperature/#`, escuchando los sensores t1 y t2), recibiendo temperaturas de ambos sensores, calculará la temperatura media, máxima y mínima para cada sensor y en total.

### Ejercicio 4: Temperatura y Humedad
Ejecutar `2_temp_y_humedad.py`. Escuchará los Topics (por defecto `temperature/t1` y `humidity`) siguiendo la lógica pedida. Por defecto los límites son `K_0 = 20` y `K_1 = 80`.

### Ejercicio 5: Temporizador
Ejecutar el cliente `5_cliente.py` y el publicador `5_publicador.py`. El publicador enviará tres mensajes de prueba (almacenador en la variable `prueba`) indicando el tiempo de espera, un Topic y un texto. El cliente lo recibirá y escribirá en ese Topic el mensaje tras el tiempo de espera indicado.

### Ejercicio 6: Encadenar clientes
Ejecutar `6_encadenar.py`. Escuchará los Topics (por defecto `numbers` y `humidity`), y seguirá los siguientes pasos:

1. Se suscribe al Topic 'numbers'.
2. Si el número recibido es primo (y entero), se suscribe al Topic 'humidity'.
4. Si la humedad recibida es mayor a 80, se desuscribe del Topic 'humidity' y vuelve al paso 1.
5. Si llega un número no entero en el Topic 'numbers' mientras se está suscrito al tópico 'humidity', se desuscribe del tópico 'humidity' y vuelve al paso 1.
