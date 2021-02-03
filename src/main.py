from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.grove_temperature_humidity_sensor import 
import seeed_dht

def readTemperatureAndHumidity(): 
    sensor_dht11 = seeed_dht("11", 12)
    counts = 0
    sum = {0, 0}
    while counts < 5:
        humi, temp = sensor_dht11.read()
        if not humi is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor_dht11.dht_type, humi, temp))
            counts += 1
            sum[0] += humi
            sum[1] += temp
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(sensor_dht11.dht_type, temp))
    results = {"humedad":sum[0]/(counts+1), 'temperatura':sum[1]/(counts+1)}
    print(results) 
def main():
    readTemperatureAndHumidity(())
 
 
if __name__ == '__main__':
    main()


