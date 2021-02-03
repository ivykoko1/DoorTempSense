from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import seeed_dht
import time

def checkProximity():
    usonic = GroveUltrasonicRanger(5)
    print(usonic.get_distance())
    time.sleep(1)

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
    print('>>DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor_dht11.dht_type, results[0], results[1]))
def main():
   while True:
         readTemperatureAndHumidity()
         checkProximity()

if __name__ == '__main__':
    main()

















