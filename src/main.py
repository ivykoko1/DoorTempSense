from grove.gpio import 
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.button import Button
import seeed_dht
import time

def main():
    btnEntrada = Button(12)
    global aforoMaximo
    aforoMaximo = 20
    global aforo 
    aforo = 0
    def on_press(t):
        print('Button is pressed')
        while True:
            print('Aforo {0}, aforo máximo', aforo, (aforoMaximo - aforo))
            if(aforo < aforoMaximo):
                if(checkProximity() < 50.0):
                    if(readTemperatureAndHumidity() < 37):
                        #LEDS VERDES
                        aforo = aforo + 1
                    else:
                        #LEDS ROJOS
                        print('CAUTION: PUEDE TENER SARS COV 2, NO ENTRAR')
                        #BUZZER SUENA
    btnEntrada.on_press = on_press

   
def checkProximity():
    usonic = GroveUltrasonicRanger(5)
    print(usonic.get_distance())
    return usonic.get_distance
def readTemperatureAndHumidity(): 
    sensor_dht11 = seeed_dht.DHT("11", 22)
    counts = 0
    sum = [0, 0]
    while counts < 5:
        humi, temp = sensor_dht11.read()
        if not humi is None:
            counts += 1
            sum[0] += humi
            sum[1] += temp
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(sensor_dht11.dht_type, temp))
    results = [sum[0]/(counts), sum[1]/(counts)]
    print('>>Humedad {1:.1f}%, temperature {2:.1f}*'.format(sensor_dht11.dht_type, results[0], results[1]))
    return results[1]
if __name__ == '__main__':
    main()

















