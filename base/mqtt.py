import paho.mqtt.client as mqtt
import json
import threading
from .models import User, TemperatureData,RespirationData,PulseData,HumidityData,SPO2Data,NIBPData
 
class thread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
 
        # helper function to execute the threads
    def run(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            client.subscribe("topic/TemperatureData")
            client.subscribe("topic/RespirationData")
            client.subscribe("topic/PulseData")
            client.subscribe("topic/HumidityData")
            client.subscribe("topic/SPO2Data")
            client.subscribe("topic/NIBPData")


        def on_message(client, userdata, msg):
            data = json.loads(msg.payload).split(" ")
            if msg.topic == 'topic/TemperatureData':
                user = User.objects.get(id=data[0])
                TemperatureData.objects.create(
                    patient = user,
                    value = data[2],
                )
                print("Temperature saved succesfully!")
            elif msg.topic == 'topic/RespirationData':
                user = User.objects.get(id=data[0])
                RespirationData.objects.create(
                    patient = user,
                    value = data[2],
                )
                print("Respiration saved succesfully!")
            elif msg.topic == 'topic/PulseData':
                user = User.objects.get(id=data[0])
                PulseData.objects.create(
                    patient = user,
                    value = data[2],
                )
                print("Pulse saved succesfully!")
            elif msg.topic == 'topic/HumidityData':
                user = User.objects.get(id=data[0])
                HumidityData.objects.create(
                    patient = user,
                    value = data[2],
                )
                print("Humidity saved succesfully!")
            elif msg.topic == 'topic/SPO2Data':
                user = User.objects.get(id=data[0])
                SPO2Data.objects.create(
                    patient = user,
                    value = data[2],
                )
                print("SPO2 saved succesfully!")
            elif msg.topic == 'topic/NIBPData':
                user = User.objects.get(id=data[0])
                NIBPData.objects.create(
                    patient = user,
                    value = data[2],
                )
                print("NIBP saved succesfully!")
            print(json.loads(msg.payload)) #converting the string back to a JSON object


        def on_disconnect(client, userdata, rc):
            client.loop_stop(force=False)
            if rc != 0:
                print("Unexpected disconnection.")
            else:
                print("Disconnected")

        client = mqtt.Client()

        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_message = on_message

        client.connect("test.mosquitto.org", 1883, 60)

        client.loop_start()
 
thread1 = thread("Communication")
