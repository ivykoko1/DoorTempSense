from grove.gpio import GPIO
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import seeed_dht

def readTemperatureAndHumidity(): 
    sensor_temp = seeed_dht.DHT("11", 12)
    counts = 0
    sum = {0, 0}
    while counts < 5:
        humi, temp = sensor_temp.read()
        if not humi is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor_temp.dht_type, humi, temp))
            counts += 1
            sum[0] += humi
            sum[1] += temp
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(sensor_temp.dht_type, temp))
    results = {sum[0]/(counts+1), sum[1]/counts}
    print(results) 
def main():
    readTemperatureAndHumidity() 
 
if __name__ == '__main__':
    main()


