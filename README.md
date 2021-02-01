# Trabajo final IoT Ivan Sanchez

 Este es el trabajo final para la asignatura Desarrollo de Aplicaciones para Internet de las Cosas, debido a motivos personales su funcionalidad se ha tenido que reducir ya que el tiempo ha sido escaso  y ha habido falta de recursos.

 Aun así, estas funcionalidades serán listadas e implementadas en  el futuro, ya que el proyecto es un módulo opcional (aunque independiente) a un proyecto en desarrollo.

## Sistema reducción de riesgo de contagios aplicado al control de aforos

### Descripción del problema:
La pandemia de COVID-19 es una pandemia causada por por coronavirus cuyo afente principal es el virus SARS-CoV-2 la cual sigue estando activa a día de hoy (enero de 2021).

Uno de sus principales síntomas, y  en el que se va a centrar el proyecto es la fiebre, por lo tanto mediante un conglomerado de sensores, actuadores e HMIs (Human Machine Interface)

### Orientación del proyecto

Hay que tener en cuenta, que a día de hoy sigue sin existir un test 100% fiable del virus, y que muchos establecimientos públicos w están viendo obligados a reducir su aforo.

Viendo los síntomas, el único que parece objetivo y fácil de medir de manera no intrusiva es la temperatura corporal, verificar si el usuario tiene una temperatura elevada o no.

### Cómo funciona

Cuando una persona se aproxime a la puerta, será detectado  por el sensor infrarrojos  el cual ~~activará varios láseres y receptores IR~~  indicará con leds azules que la  persona  posicione su dedo en el sensor. Cuando la lectura se estabilice,  se considerará si tiene fiebre o no,  si la  tiene los  led  se  volverán rojos y el  buzzer sonará. Si no,cambiarán su color a verde. Antes de continuar el cliente/individuo  deberá pulsar el botón  que lleva  cuenta del aforo. A la salida deberá pulsarlo de nuevo,  actualizando el contador.

### Estructura a nivel físico (instalación física)

El sistema consistiría de:

* ~~1 o múltiples (si queremos adaptarlo a  diferentes alturas: niños, adultos...) sensores de temperatura via infrarrojo~~
* ~~1 o múltiples Microcontroladores ESP8266 Wi-Fi para transmitir la información a una API central, alojada en nuestra Raspberru (cada uno puede leer varios sensores via I2C), reduciendo cableado y dificultad de instalación.~~
* ~~API REST Con interfaz web  para ver los datos recibidos por los ESP8266 en tiempo real~~
* Sensor  de  ultrasonidos
* Pulsador de entrada y de salida
* Sensor de humedad para comprobar que el habitáculo no  se está humedeciendo demasiado debido a la sobrecarga de visitantes.
* Buzzer para avisar
* Una Raspberry Pi que se encargará de controlar todos los sensores, y mostrar en el puerto  1337 de su IP  el aforo actual y máximo.

### Estructura a bajo nivel (software)

### Componentes necesarios

* [~~Sensor de infrarojos MLX90614ESF~~](https://www.mouser.es/datasheet/2/734/MLX90614-Datasheet-Melexis-953298.pdf) *No estará en el proyecto final, pero era la idea principal*
* ~~Diodo emisor laser infrarrojo~~
* Sensor de temperatura [DS18B20](https://www.mouser.es/datasheet/2/256/DS18B20-370043.pdf)
* Sensor de distancia por ultrasonidos *Detecta cuando alguien  hapasado la puerta y activa el láser*
* Raspberry Pi 3/4 (**En el futuro será sustituido por un microcontrolador de mucha menos potencia computacional, coste mucho menor y consumo casi nulo**)
* LEDs RGB (*Tira o diodos de 3 conexiones, el circuito variará dependiendo de la elección*)
* Buzzer o altavoz de alerta
* Pulsador
* Sensor de humedad DHT11 o DHT22 (son iguales, cambia la resolución de cada uno)

## Librerías de  terceros

* [W1ThermSensor](https://pypi.org/project/w1thermsensor/)
* [Adafruit_Python_DHT](https://github.com/adafruit/Adafruit_Python_DHT)