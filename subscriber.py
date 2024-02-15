from msg_displayer import MQTTMessageDisplayer
import paho.mqtt.client as mqtt_client
import sys

class MQTTSubscriber:
    def __init__(self, topic: str):
        self.topic = topic
        self.subscriber = self.create_client()

    def display_message(self, client, userdata, msg):
        print(f"{msg.topic}: {msg.payload.decode()}")

    def on_connect(self, client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Connected to MQTT broker")
            self.subscriber.subscribe(self.topic)
        else:
            print(f"Connection failed with code {rc}")
            sys.exit(1)
    def create_client(self):
        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2)
        client.on_connect = self.on_connect
        client.on_message = self.display_message
        if client.connect("localhost", 1883, 60) != 0:
            print("Couldn't connect to the mqtt broker")
            sys.exit(1)
        return client

    def subscribe(self):
        self.subscriber.subscribe(self.topic)

        try:
            self.subscriber.loop_forever()
        except Exception as e:
            print(e)
            print("Caught an Exception, something went wrong...")
        finally:
            print("Disconnecting from the MQTT broker")
            self.subscriber.disconnect()

if __name__ == "__main__":
    topic = "Sample"
    subscriber = MQTTSubscriber(topic).subscribe()