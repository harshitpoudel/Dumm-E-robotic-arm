# Dumm-E Robotic Arm

**Dumm-E** is a DIY, open-source bionic robotic arm controlled by a glove outfitted with flex sensors.  
You move your hand—the robotic arm mimics your fingers using servo motors, a Raspberry Pi 4, and an Arduino.

## Project Architecture

```
[Flex Sensors on Glove]
        │
        ▼ (Analog)
   [Arduino Nano/Uno]
        │
        ▼ (USB Serial)
   [Raspberry Pi 4]
        │
        ▼ (PWM)
   [Servo Motors (MG996R)]
```

- The glove’s flex sensors measure your finger bends.
- An Arduino reads the sensors and sends values via USB serial.
- A Raspberry Pi 4 receives sensor values, maps them to servo angles, and controls 5 servo motors using a PWM driver.

---

## Folder Structure

```
Dumm-E-robotic-arm/
├── README.md
├── code/
│   └── glove_sensor_reader/
│       └── glove_sensor_reader.ino
├── raspberry_pi/
│   ├── main.py
│   ├── config.py
│   └── requirements.txt
├── hardware/
│   ├── WIRING.md
│   └── PARTS_LIST.md
└── docs/
    ├── BEGINNER_GUIDE.md
    └── TROUBLESHOOTING.md
```

---

## Features

- **5 flex sensors** (one per finger)
- **Arduino**: reads sensors, calibrates, sends to RPi over serial
- **Raspberry Pi 4**: reads sensor values, drives 5 MG996R servos via PCA9685 PWM
- **Beginner-friendly**: Comprehensive guides, wiring help, troubleshooting, and safety
- **Flexible**: Calibration and reversal for left/right-handed gloves and servo orientation
- **Upgradable**: Modular design to add IMU, WiFi, or gesture recognition

---

## Quickstart

1. **Read [`docs/BEGINNER_GUIDE.md`](docs/BEGINNER_GUIDE.md) thoroughly!**
2. **Check all safety notes.**
3. Assemble hardware and wire as in [`hardware/WIRING.md`](hardware/WIRING.md)
4. Flash Arduino with [`code/glove_sensor_reader/glove_sensor_reader.ino`](code/glove_sensor_reader/glove_sensor_reader.ino)
5. Set up Raspberry Pi 4 as in  [`raspberry_pi/requirements.txt`](raspberry_pi/requirements.txt) and run [`main.py`](raspberry_pi/main.py)

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Contributing

Issues and PRs are welcome! See [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) for common problems and how to help.

**build affordable bionic arm**
