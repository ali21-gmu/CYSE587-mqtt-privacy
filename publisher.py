import paho.mqtt.client as mqtt
import time
import json

# MQTT broker address (localhost since communicating on same computer)
broker = "localhost"
# default MQTT port
port = 1883
# topic to publish to
topic = "victim/distress"

# generates payload with victim ID, severity, position, and timestamp of sent message
def create_payload():
    payload = {
        "id": "victim1",
        "severity": "high",
        "position": (-23.22488,-45.232),
        "timestamp": time.perf_counter()
    }
    return payload

# set up client and connect to the broker (with address and port)
client = mqtt.Client()
client.connect(broker, port)

while True:
    # transforms JSON payload into UTF-8 encoded version for MQTT transmission
    payload = json.dumps(create_payload()).encode()
    # publish payload to topic every 10 seconds (sleep(10))
    client.publish(topic, payload)
    # print to terminal for verification
    print(f"Published to {topic}: {payload}")
    print(f"Payload size: {len(payload)} bytes")
    time.sleep(10)