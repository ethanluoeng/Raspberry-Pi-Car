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

<pre>
  graph TD
      A[Laptop Controller] --&gt;|MQTT Commands| B[HiveMQ Broker]
      B --&gt; C[Raspberry Pi]
      C --&gt; D[MQTT Client]
      C --&gt; E[Motor Control Logic]
      C --&gt; F[GPIO + PWM Outputs]
      F --&gt; G[Motor Driver]
      G --&gt; H[DC Motors x4]
</pre>
## 📈 Future Improvements

- Camera-based vision using OpenCV or MediaPipe
- Obstacle avoidance with ultrasonic sensors for autonomous navigation modes
- Web-based control dashboard
