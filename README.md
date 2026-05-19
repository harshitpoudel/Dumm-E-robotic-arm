# Dumm-E Robotic Arm

**Dumm-E** is a DIY, open-source bionic robotic arm controlled by a glove outfitted with flex sensors.  
You move your hand—the robotic arm mimics your fingers using servo motors and an **ESP32 DevKit v1** with a PCA9685 servo driver.

## Project Architecture

```
[Flex Sensors on Glove]
        │
        ▼ (Analog)
   [ESP32 DevKit v1]
        │
        ▼ (I2C via PCA9685)
   [Servo Motors (MG996R)]
```

- The glove’s flex sensors measure your finger bends.
- ESP32 reads the flex sensors and maps them to servo angles.
- ESP32 drives 5 servo motors through the PCA9685 PWM driver over I2C.

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
- **ESP32 DevKit v1**: reads sensors, calibrates, and controls servos
- **PCA9685 servo driver (I2C)**: drives 5 MG996R servos on channels 0–4
- **Beginner-friendly**: Comprehensive guides, wiring help, troubleshooting, and safety
- **Flexible**: Calibration and reversal for left/right-handed gloves and servo orientation
- **Upgradable**: Modular design to add IMU, WiFi, or gesture recognition

---

## Quickstart

1. **Read [`docs/BEGINNER_GUIDE.md`](docs/BEGINNER_GUIDE.md) thoroughly!**
2. **Check all safety notes.**
3. Assemble hardware and wire as in [`hardware/WIRING.md`](hardware/WIRING.md)
4. Install ESP32 board support in Arduino IDE (`esp32 by Espressif Systems`) or use PlatformIO (`platform = espressif32`).
5. Flash ESP32 DevKit v1 with [`code/glove_sensor_reader/glove_sensor_reader.ino`](code/glove_sensor_reader/glove_sensor_reader.ino)
6. Wire ESP32 ↔ PCA9685 and flex sensors as documented in [`hardware/WIRING.md`](hardware/WIRING.md)

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Contributing

Issues and PRs are welcome! See [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) for common problems and how to help.

**build affordable bionic arm**
