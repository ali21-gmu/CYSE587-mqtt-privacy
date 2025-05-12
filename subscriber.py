import paho.mqtt.client as mqtt
import time
import json

# callback function for broker response to connection request
def on_connect(client, userdata, flags, rc):
    # print message on success and on failure
    if rc == 0:
        print("Connected successfully with result code: ", rc)
        client.subscribe(topic)
    else:
        print("Connection failed with result code: ", rc)

# callback function called when message has been received on subscribed topic
def on_message(client, userdata, message):
    current = time.perf_counter()
    # loads data with JSON payload
    data = json.loads(message.payload.decode())
    # prints information to print for verification and comparing metrics
    print(f"Message received on topic {message.topic}")
    print(f"Message: {data}")
    print(f"Latency: {current - data["timestamp"]}")

# MQTT broker address (localhost since communicating on same computer)
broker = "localhost"
# default MQTT port
port = 1883
# topic to publish to
topic = "victim/distress"

# set up client and connect to the broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

# continues to loop
client.loop_forever()