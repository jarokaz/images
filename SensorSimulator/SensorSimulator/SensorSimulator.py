from azure.servicebus import ServiceBusService
import random

def getReading(sensorId,temperature,inverter_speed):                  
    body = "{\"SensorId\" : \"" + sensorId + "\", \"Temperature\" : " + str(temperature) + ", \"InverterSpeed\" : " + str(inverter_speed) + "}"        
    return body


service_namespace='mtcsvcamat'
key_name = 'All' # SharedAccessKeyName from Azure portal
key_value = 'EUudNBNEAfkwPV1jmyh+PpeuAd3sp624MulfJGau0C0=' # SharedAccessKey from Azure portal
sbs = ServiceBusService(service_namespace,
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)

random.seed()
temperaturebase=20.0
inverter_speedbase = 200.0
count=0
sensor='Pump1'

while True:
    count=count+1
    if (count < 20):
       temperature = temperaturebase 
       inverter_speed = inverter_speedbase     
    else:
        temperature = temperature + round(3*random.random(),2)
        inverter_speed = inverter_speed + round(3*random.random(),2)     

    body = getReading(sensor, temperature, inverter_speed)
    print(body)
    sbs.send_event('amatdemo', body)
    #if hubStatus <> 201:
        #print("Error on " + str(datetime.datetime.now()) + " :"+str(hubStatus))


