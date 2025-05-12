# SCENARIO.md

## 🛠️ Scenario Setup Instructions

### How to Run the Scenario
#### A. Start Mosquitto Broker
In one terminal, run:
```bash
mosquitto.exe -v
```
Success if the output returns "mosquitto version 2.0.21 running"

#### B. Start the Subscriber
In the second terminal, run:
```bash
python subscriber.py
```

or

```bash
python subscriber_pet.py
```

### C. Start the Publisher
In the third terminal, run:
```bash
python publisher.py
```
or
```bash
python publisher_pet.py
```
if subscriber_pet.py was ran before

---

## Interpreting the Results
### subscriber.py
You should see:
- Topic the message is received on
- MQTT message payload
- Latency

### publisher.py
You should see:
- Topic published to and MQTT payload
- Payload size (in bytes)

### subscriber_pet.py
You should see:
- Hashed topic the message is received on
- Decrypted MQTT message payload
- Detokenized Victim Location
- Latency

### publisher_pet.py
You should see:
- Hashed topic published to and MQTT payload
- Payload encrypted with Fernet
- Payload size (in bytes)

---

### Example Output
#### subscriber.py
```bash
Connected successfully with result code:  0
Message received on topic victim/distress
Message: {'id': 'victim1', 'severity': 'high', 'position': [-23.22488, -45.232], 'timestamp': 169903.0767261}
Latency: 0.0031106999958865345
```
#### publisher.py
```bash
Published to victim/distress: b'{"id": "victim1", "severity": "high", "position": [-23.22488, -45.232], "timestamp": 169903.0767261}'
Payload size: 100 bytes
```
#### subscriber_pet.py
```bash
Message received on topic 1bdd5b5b92/16e601ed6c
Decrypted message: {'id': 'ca12f31b8c', 'severity': 'high', 'position': '014e572462068381ee6a7b291e2b9aab', 'timestamp': 163255.7220207}
Detokenized Victim Location: [-23.22488, -45.232]
Latency: 0.0007345000049099326
```
#### publisher_pet.py
```bash
Published to 1bdd5b5b92/16e601ed6c: b'{"id": "ca12f31b8c", "severity": "high", "position": "e6311f547951b6df69c40ba00725310a", "timestamp": 163215.708769}'
Encrypted Payload: b'gAAAAABoIVSLm1QEzXTzdvf-6X8hg-RIwricaa3mpDfJRArMMRWTZ9eZcqJPDO2dvwDbwy5S814wz3wE_V1nC9YlOMJ81aNeX00nIqbXQ2dnLAVA7-sE4NrzjqqZ9gcwo9cx7znIqNUYviSB8k9OeoBRbaGFRebGAkNbs7nnaE27kiyryU1729ewA7jOZC3uh3XuzpCzL25HROiC-EGtYo8FfG3RU_HYSAocjuGUGCeeZhVqzMI_9fE='
Payload size: 248 bytes
```
