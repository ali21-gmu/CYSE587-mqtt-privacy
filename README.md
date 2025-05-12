# CYSE587 MQTT Privacy Project
The repository contains:
- Source code (Python) for the publishers and subscribers
- MQTT configuration and broker setup
- README with the tools used, a how-to explaining how to install each library or supported tool.
- SCENARIO.md that explains how to create the scenario and interpret the result.
- LICENSE file (you can select any given, it is open source)
- A slide with the information about the video presentation.

---

## Scenario Overview
This project simulates a MQTT disaster response system, using a publisher, subscriber, and broker. The system is enhanced with privacy-enhancing technologies such as pseudonymization, tokenization, and encrypted payloads with Fernet Symmetric Encryption to address LINDDUN-identified privacy threats.

---

## Individual Files
- publisher.py: Simulates publisher in base MQTT system
- subscriber.py: Simulates subscriber in base MQTT system
- publisher_pet.py: Simulates publisher in MQTT system enhancing with privacy-enhancing technologies
- subscriber_pet.py: Simulates subscriber in MQTT system enhancing with privacy-enhancing technologies
- secret.key: Contains Fernet symmetric encryption key used by publisher_pet.py and subscriber_pet.py
- token_mapping.json: Contains token mapping of victim location data

---

## Tools & Libraries
- **Language**: Python 3.12.3+
- **Broker**: [Mosquitto MQTT](https://mosquitto.org/)
- **Libraries**:
  - `paho-mqtt`: Python MQTT client
  - `cryptography`: MQTT Encryption (Fernet symmetric encryption)
  - `hashlib`: Includes different hash algorithms, such as SHA256
 
---

## Installation
### Install Mosquitto Broker
- Go to downloads at Mosquitto webpage [Mosquitto MQTT Downloads](https://mosquitto.org/download/)
- Download and install the mosquitto-2.0.21a-install-windows-x64.exe installer under Windows

### Library Installation
```bash
pip install paho-mqtt
```
```bash
pip install cryptography
```

### MQTT Configuration and Broker Setup
Start broker with default settings by running:
```bash
mosquitto.exe -v
```

Optional Usage: you can start Mosquitto broker with a custom configuration file (`custom.conf`)
```bash
mosquitto.exe -c custom.conf
```

---

## Video
- [MQTT Privacy Project Video](https://gmuedu-my.sharepoint.com/:v:/g/personal/ali21_gmu_edu/EdGtSflQz-ZIo2iicVeDShYB_-yKPjcTMeZ1Uo0u1QoWyQ?e=5jJf9e&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)
