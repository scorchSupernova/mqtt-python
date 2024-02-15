from publish import MQTTPublish
from subscriber import MQTTSubscriber


if __name__ == "__main__":
    topic = "Sample"
    publisher = MQTTPublish(topic).publish_message("HELLO There")
    subscriber = MQTTSubscriber(topic).subscribe()