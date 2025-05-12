# SCENARIO.md

## 🛠️ Scenario Setup Instructions

### 1. Prerequisites

Install required Python packages:
```bash
pip install paho-mqtt cryptography python-dotenv
```

Install and run the Mosquitto MQTT broker locally:
```bash
mosquitto
```

## How to Run the Scenario

### A. Start the Subscriber (C2 System)

```bash
python subscriber.py
```

You should see:
- Decrypted messages
- Latency in seconds
- Message size in bytes

### B. Start the Publisher (Victim/Drones)

```bash
python publisher.py
```

You should see:
- Hashed topic used for publishing
- Encrypted payload size

---

## 🔍 Interpreting the Results

### ✅ What to Observe

| Metric | Meaning |
|--------|---------|
| **Hashed Topics** | Topic names are obfuscated (e.g., `topics/0c1f...`) |
| **Encrypted Payload** | Data is unreadable to broker/attacker |
| **Latency** | Time taken from message sent to received |
| **Payload Size** | Encrypted messages are longer than plaintext |
| **Decrypted Message** | UID and location are hashed (pseudonymized) |

### 🔐 Example Output (Subscriber)
```json
Decrypted message:
{
  "uid_hash": "0c1fdaab7f13",
  "zone_hash": "5a72b9a3482d",
  "severity": "high",
  "timestamp": 1714552280.027
}
Latency: 0.045 seconds
Encrypted message size: 184 bytes
```