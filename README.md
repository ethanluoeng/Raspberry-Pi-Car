# Raspberry Pi Robotic Car 🚗🤖

Featuring four-motor drive, PWM speed control, remote operation over MQTT and a live webcam.

---

## 📌 Features

- Four-motor drive system  
  - Independent speed and direction control  
  - Supports differential steering and tank drive
- PWM-based motor control  
  - Smooth acceleration and deceleration  
  - Adjustable speed resolution
- Remote control via MQTT  
  - Real-time command publishing from a laptop  
  - Low-latency communication using a HiveMQ broker
- Multiple driving modes  
  - Regular car-style steering  
  - Tank drive (independent left/right control)
- Modular Python codebase  
  - Clean separation between motor control, networking, and command handling
- Extensible design  
  - Easy to integrate sensors (camera, ultrasonic, IMU)  

## 🧠 System Architecture

graph TD
    A[Laptop Controller] -->|MQTT Commands| B[HiveMQ Broker]
    B --> C[Raspberry Pi]
    
    subgraph "Raspberry Pi Internals"
    C --> D[MQTT Client]
    C --> E[Motor Control Logic]
    C --> F[GPIO + PWM Outputs]
    end
    
    F --> G[Motor Driver]
    G --> H[DC Motors x4]

## 📈 Future Improvements

- Camera-based vision using OpenCV or MediaPipe
- Obstacle avoidance with ultrasonic sensors for autonomous navigation modes
- Web-based control dashboard
