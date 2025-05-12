# import Fernet for symmetric encryption, hashlib for hashing IDs and topic names, and secrets
# for secure token generation
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
import hashlib
import secrets
import time
import json
import os

# function for hashing strings - creates anonymized, fixed length topics/IDs
def hash_func(val):
    return hashlib.sha256(val.encode()).hexdigest()[:10]

# function for replacing plaintext location with a secure token
# mapping saved to JSON file for subscriber to detokenize
def tokenize(loc):
    token = secrets.token_hex(16)
    with open('token_mapping.json', 'r') as f:
        mapping = json.load(f)
    mapping[token] = loc
    with open('token_mapping.json', 'w') as f:
        json.dump(mapping, f)
    return token

# generates payload with hashed victim ID, severity, tokenized position, and 
# timestamp of sent message
def create_payload():
    payload = {
        "id": hash_func("node1"),
        "severity": "high",
        "position": tokenize((-23.22488,-45.232)),
        "timestamp": time.perf_counter()
    }
    return payload

# checks if there is an existing shared key
if not os.path.exists("secret.key"):
    # if not, generate new key and write to secret.key
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
else:
    # otherwise, use shared key
    with open("secret.key", "rb") as f:
        key = f.read()
# creates Fernet encryption object with key for encrypting messages
secret = Fernet(key)

broker = "localhost"
port = 1883
# topic names as hashed for anonymization
topic = hash_func("victim")+"/"+hash_func("distress")

# initialize MQTT client and connect to broker
client = mqtt.Client()
client.connect(broker, port)

while True:
    # encrypts payload with Fernet encryption, prints to terminal for verification,
    # and publishes every 10 seconds
    payload = json.dumps(create_payload()).encode()
    encrypted_payload = secret.encrypt(payload)
    client.publish(topic, encrypted_payload)
    print(f"Published to {topic}: {payload}")
    print(f"Encrypted Payload: {encrypted_payload}")
    print(f"Payload size: {len(encrypted_payload)} bytes\n")
    time.sleep(10)