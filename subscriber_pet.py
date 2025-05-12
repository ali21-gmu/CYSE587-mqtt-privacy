import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
import hashlib
import secrets
import time
import json

# function for hashing strings - creates anonymized, fixed length topics/IDs
def hash_func(val):
    return hashlib.sha256(val.encode()).hexdigest()[:10]

# function for looking up the original location with
# token-based mapping - returns original location
def detokenize(token):
    with open('token_mapping.json', 'r') as f:
        mapping = json.load(f)
    return mapping.get(token)

# callback function called when message has been received on subscribed topic
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully with result code: ", rc)
        client.subscribe(topic)
    else:
        print("Connection failed with result code: ", rc)

# MQTT broker address (localhost since communicating on same computer)
def on_message(client, userdata, message):
    # get current time for measuring latency
    current = time.perf_counter()
    try:
        # decrypts message with Fernet secret key
        decrypt = secret.decrypt(message.payload)
        # loads data with JSON payload
        data = json.loads(decrypt.decode())
        # prints information to print for verification and comparing metrics
        print(f"Message received on topic {message.topic}")
        print(f"Decrypted message: {data}")
        print(f"Detokenized Victim Location: {detokenize(data['position'])}")
        print(f"Latency: {current - data['timestamp']}\n")
    # error message for decryption failure
    except Exception as e:
        print("Decryption Failed: ", e)

broker = "localhost"
port = 1883
# topic names as hashed for anonymization
topic = hash_func("victim") +"/"+ hash_func("distress")

# reads shared key to use secret key for decryption
with open("secret.key", "rb") as f:
    key = f.read()
secret = Fernet(key)

# initialize MQTT client and connect to broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

# continues to loop
client.loop_forever()