# Wiring Guide: Dumm-E Robotic Arm

**⚠️ Safety First!**  
Always turn OFF power supplies before wiring. Use a UBEC to bring LiPo voltage to safe 6V for MG996R servos.

---

## Connection Overview

| Module                     | Connects To      | Signal Details                       |
|----------------------------|------------------|--------------------------------------|
| Flex Sensors (Glove)       | ESP32 ADC pins   | GPIO32, 33, 34, 35, 39 via 10kΩ dividers |
| ESP32 DevKit v1            | PCA9685 Module   | I2C: SDA (GPIO21), SCL (GPIO22)      |
| PCA9685 PWM Board          | Servos           | Channels 0–4; +6V, GND per servo     |
| Power (LiPo via UBEC)      | PCA9685, Servos  | 6V 5A output, common ground w/ ESP32 |
| MPU-6050 IMU (Optional)    | ESP32 I2C        | Shared SDA, SCL (address selectable) |

---

## **Servo Power Diagram**

```
LiPo (+7.4V)
   |
[Blade Fuse]
   |
[UBEC] ——> +6V → PCA9685 V+ (power rail)
   |                 \
   |                  +––> MG996R Servos (red wires)
  GND ————————+———————> PCA9685 GND, Servo Brown wires, ESP32 GND
             |
         ESP32 GND
```

---

### **PCA9685 / ESP32 DevKit v1 I2C Wiring (Default):**

| PCA9685 pin | ESP32 pin | Notes |
|-------------|-----------|-------|
| SCL         | GPIO22    | Default SCL, configurable in code |
| SDA         | GPIO21    | Default SDA, configurable in code |
| VCC         | 3V3       | Logic supply |
| GND         | GND       | Must share common ground |

*PCA9685 "V+" must be powered by external 5V–6V servo supply (UBEC), not from ESP32 3V3 pin.*

**Logic-level note:** Most PCA9685 boards accept 3.3V I2C logic directly. If your specific board requires 5V-only I2C thresholds, add an I2C level shifter.

---

## **ESP32/Flex Sensor:**

- Each flex sensor forms a voltage divider with a 10kΩ resistor.
- Connect middle “sensor wire” to ESP32 ADC1 inputs (GPIO32/33/34/35/39).
- Feed divider from 3.3V and GND on ESP32.

---

### **Flex Sensor Example Schematic:**

```
3.3V ----+
        |
   [Flex Sensor]
        |
    Analog In (ESP32 ADC pin)
        |
   [10kΩ resistor]
        |
      GND
```

[Flexes] → [ESP32 ADC pins] — I2C — [PCA9685 PWM Driver] → [Servos]

---

## **Helpful Tips**

- **Always** have a fuse on your LiPo lines!
- All modules get a *common ground* (connect all GNDs together!).
- Double check voltage: servos burn at >7V, ESP32 dies above 3.3V logic and 5V USB limits.
- Keep signal wires short; use new Dupont cables and solder for reliability.
- Only power on ESP32 and servos once double-checked.

---

## **Further Reading**

- [Adafruit PCA9685 Servo Driver Guide](https://learn.adafruit.com/16-channel-pwm-servo-driver)
- [ESP32 ADC Guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/adc.html)
