# Wiring Guide: Dumm-E Robotic Arm

**⚠️ Safety First!**  
Always turn OFF power supplies before wiring. Use a UBEC to bring LiPo voltage to safe 6V for MG996R servos.

---

## Connection Overview

| Module                     | Connects To      | Signal Details                       |
|----------------------------|------------------|--------------------------------------|
| Flex Sensors (Glove)       | Arduino Analog   | A0–A4, via 10kΩ resistors            |
| Arduino (Nano/Uno)         | RPi 4 (USB)      | USB Serial connection                |
| Raspberry Pi 4 GPIO        | PCA9685 Module   | I2C: SDA (GPIO2), SCL (GPIO3)        |
| PCA9685 PWM Board          | Servos           | Channels 0–4; +6V, GND per servo     |
| Power (LiPo via UBEC)      | PCA9685, Servos  | 6V 5A output, common ground w/ RPi   |
| MPU-6050 IMU (Optional)    | RPi 4 I2C        | Shared SDA, SCL (address selectable) |

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
  GND ————————+———————> PCA9685 GND, Servo Brown wires, RPi GND
             |
         RPi GND
```

---

### **PCA9685/RPi I2C Wiring:**

| PCA9685 pin | RPi GPIO (BCM) | Pi Pin # |
|-------------|----------------|----------|
| SCL         | GPIO3 (SCL)    | 5        |
| SDA         | GPIO2 (SDA)    | 3        |
| VCC         | 3.3V           | 1        |
| GND         | GND            | 6        |

*PCA9685 "V+" must be powered by 6V (UBEC), not Pi 5V pin!*

---

## **Arduino/Flex Sensor:**

- Each flex sensor forms a voltage divider with a 10kΩ resistor.
- Connect middle “sensor wire” to analog input (A0–A4).
- Both sensor ends: ground & +5V from Arduino.

---

### **Flex Sensor Example Schematic:**

```
+5V ----+
        |
   [Flex Sensor]
        |
     Analog In (A0)
        |
   [10kΩ resistor]
        |
      GND
```

[Flexes] → [Arduino analog pins] — USB — [RPi] — I2C — [PWM Driver] → [Servos]

---

## **Helpful Tips**

- **Always** have a fuse on your LiPo lines!
- All modules get a *common ground* (connect all GNDs together!).
- Double check voltage: servos burn at >7V, Pi dies above 5.5V.
- Keep signal wires short; use new Dupont cables and solder for reliability.
- Only power on Pi and servos once double-checked.

---

## **Further Reading**

- [Adafruit PCA9685 Servo Driver Guide](https://learn.adafruit.com/16-channel-pwm-servo-driver)
- [Arduino Analog Input Tutorial](https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInput)
