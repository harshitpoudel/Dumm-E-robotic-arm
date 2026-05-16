# Beginner’s Guide: Dumm-E Robotic Arm

Welcome! This guide walks you step-by-step through setting up your own bionic, glove-controlled robotic arm.

---

## Table of Contents

1. [Safety Warnings](#safety-warnings)
2. [Required Parts](#required-parts)
3. [Assembly Overview](#assembly-overview)
4. [Glove Preparation](#glove-preparation)
5. [Arduino Flex Sensor Calibration](#arduino-flex-sensor-calibration)
6. [Arduino Setup](#arduino-setup)
7. [Raspberry Pi Preparation](#raspberry-pi-preparation)
8. [Servo & Power Safety](#servo--power-safety)
9. [Initial Power-on Checklist](#initial-power-on-checklist)
10. [Testing & Debugging](#testing--debugging)
11. [Upgrades & Extensions](#upgrades--extensions)

---

## Safety Warnings

- **Never power the servos from your Pi’s 5V rail!**  
  Use a separate UBEC/BEC at 6V and a fuse.
- **Always check for common ground** between Pi, Arduino, and servos.
- **Remove jewelry and tie hair/clothes** before testing.
- **Servos can pinch or crush fingers**—keep hands clear!
- **Hotglue and soldering irons are HOT—Use with care.**

---

## Required Parts

See [`hardware/PARTS_LIST.md`](../hardware/PARTS_LIST.md).

---

## Assembly Overview

1. **3D print** the required arm/hand parts.
2. **Wire** flex sensors to Arduino as voltage dividers.
3. **Mount** servos and string tendons.
4. **Connect** servos to PCA9685 and power.
5. **Wire** Raspberry Pi I2C to PCA9685 (see [`hardware/WIRING.md`](../hardware/WIRING.md)).
6. **Connect** Arduino to Pi over USB.

---

## Glove Preparation

- Attach 1 × flex sensor to each glove finger using hotglue or velcro.
- Route wires neatly to avoid snags.
- Solder flex sensors to DuPont wires for secure connections.

---

## Arduino Flex Sensor Calibration

1. Upload [`glove_sensor_reader.ino`](../code/glove_sensor_reader/glove_sensor_reader.ino) to your Arduino.
2. Open Arduino Serial Monitor at 115200 baud.
3. Note the analog values for each finger when straight (**flexMin**) and fully bent (**flexMax**).
4. Update the arrays in the code for precise mapping.
5. Re-upload to your Arduino.

---

## Arduino Setup

- Use any Arduino model with ≥5 analog inputs.
- Connect each sensor’s output (middle wire) to each analog pin A0–A4.
- Use 10kΩ resistors to ground to form voltage dividers.

---

## Raspberry Pi Preparation

1. Install Raspbian OS, update with `sudo apt update && sudo apt upgrade`.
2. Enable I2C with `sudo raspi-config` (Interfacing → I2C → Enable).
3. `cd raspberry_pi/`
4. Install dependencies with `pip install -r requirements.txt`

---

## Servo & Power Safety

- Use a fuse and UBEC on your LiPo power!
- Connect servo external power “V+” and ground to PCA9685 and all servos.
- Never power servos from Pi’s 5V pin.

---

## Initial Power-on Checklist

✓ All joints move smoothly by hand  
✓ Glove sensor readings present in Serial Monitor  
✓ All grounds connected in common  
✓ Servo power off for first software test  
✓ All code uploaded correctly

---

## Testing & Debugging

1. Run `main.py` on Raspberry Pi:  
   `python3 main.py`
2. Move your gloved fingers—corresponding servos should move the robot.
3. If servos move wrong direction, set `SERVO_REVERSE[]` in `config.py`.
4. If movement is limited, recalibrate flex sensors and servos.

---

## Upgrades & Extensions

- Add **wireless glove** (Bluetooth/ESP-NOW).
- Integrate **MPU-6050 IMU** for gesture detection.
- Add web dashboard (Flask server on Pi).
- Add more degrees of freedom or thumb opposition.

---

*Enjoy building your Dumm-E robotic arm! Share your improvements as a pull request!*
