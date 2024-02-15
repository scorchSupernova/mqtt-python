import sys
import paho.mqtt.client as mqtt_client


class MQTTPublish:
    def __init__(self, topic: str):
        self.topic = topic
        self.publisher = self.create_client()

    def create_client(self):
        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2)
        if client.connect("localhost", 1883, 60) != 0:
            print("Couldn't connect to the mqtt broker")
            sys.exit(1)
        return client

    def publish_message(self, message):
        self.publisher.publish(self.topic, message, 0)
        print("OK")
        self.publisher.disconnect()


if __name__ == "__main__":
    topic = "Sample"
    publisher = MQTTPublish(topic).publish_message("HELLO There")
