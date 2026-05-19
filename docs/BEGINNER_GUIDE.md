# Beginner’s Guide: Dumm-E Robotic Arm

Welcome! This guide walks you step-by-step through setting up your own bionic, glove-controlled robotic arm.

---

## Table of Contents

1. [Safety Warnings](#safety-warnings)
2. [Required Parts](#required-parts)
3. [Assembly Overview](#assembly-overview)
4. [Glove Preparation](#glove-preparation)
5. [ESP32 Flex Sensor Calibration](#esp32-flex-sensor-calibration)
6. [ESP32 Setup](#esp32-setup)
7. [Firmware Upload](#firmware-upload)
8. [Servo & Power Safety](#servo--power-safety)
9. [Initial Power-on Checklist](#initial-power-on-checklist)
10. [Testing & Debugging](#testing--debugging)
11. [Upgrades & Extensions](#upgrades--extensions)

---

## Safety Warnings

- **Never power the servos from your ESP32 board 5V/USB rail!**  
  Use a separate UBEC/BEC at 6V and a fuse.
- **Always check for common ground** between ESP32, PCA9685, and servos.
- **Remove jewelry and tie hair/clothes** before testing.
- **Servos can pinch or crush fingers**—keep hands clear!
- **Hotglue and soldering irons are HOT—Use with care.**

---

## Required Parts

See [`hardware/PARTS_LIST.md`](../hardware/PARTS_LIST.md).

---

## Assembly Overview

1. **3D print** the required arm/hand parts.
2. **Wire** flex sensors to ESP32 as voltage dividers.
3. **Mount** servos and string tendons.
4. **Connect** servos to PCA9685 and power.
5. **Wire** ESP32 I2C to PCA9685 (see [`hardware/WIRING.md`](../hardware/WIRING.md)).
6. **Connect** ESP32 USB for programming and serial debug.

---

## Glove Preparation

- Attach 1 × flex sensor to each glove finger using hotglue or velcro.
- Route wires neatly to avoid snags.
- Solder flex sensors to DuPont wires for secure connections.

---

## ESP32 Flex Sensor Calibration

1. Upload [`glove_sensor_reader.ino`](../code/glove_sensor_reader/glove_sensor_reader.ino) to your ESP32 DevKit v1.
2. Open Serial Monitor at 115200 baud.
3. Note the analog values for each finger when straight (**flexMin**) and fully bent (**flexMax**).
4. Update the arrays in the code for precise mapping.
5. Re-upload to your ESP32.

---

## ESP32 Setup

- Install Arduino IDE board package: **esp32 by Espressif Systems**.
- Select board: **ESP32 Dev Module** (ESP32 DevKit v1 compatible).
- Connect each sensor output (middle wire) to ESP32 ADC pins (default: GPIO32, 33, 34, 35, 39).
- Use 10kΩ resistors to ground to form voltage dividers.

---

## Firmware Upload

1. Install required Arduino libraries:
   - `Adafruit PWM Servo Driver Library`
2. Ensure I2C pins in firmware match your wiring (default SDA=GPIO21, SCL=GPIO22).
3. Compile and upload the sketch to ESP32 DevKit v1.
4. Optional (PlatformIO): use `platform = espressif32`, `board = esp32dev`.

---

## Servo & Power Safety

- Use a fuse and UBEC on your LiPo power!
- Connect servo external power “V+” and ground to PCA9685 and all servos.
- Never power servos from ESP32 board 5V/USB pin.

---

## Initial Power-on Checklist

✓ All joints move smoothly by hand  
✓ Glove sensor readings present in Serial Monitor  
✓ All grounds connected in common  
✓ Servo power off for first software test  
✓ ESP32 firmware uploaded correctly

---

## Testing & Debugging

1. Open Serial Monitor (115200 baud) and confirm live flex values.
2. Move your gloved fingers—corresponding servos should move via PCA9685 channels.
3. If servos move in wrong direction, set `servoReverse[]` in the ESP32 sketch.
4. If movement is limited, recalibrate `flexMin[]` and `flexMax[]`.

---

## Upgrades & Extensions

- Add **wireless glove** (Bluetooth/ESP-NOW).
- Integrate **MPU-6050 IMU** for gesture detection.
- Add web dashboard (Flask server on Pi).
- Add more degrees of freedom or thumb opposition.

---

*Enjoy building your Dumm-E robotic arm! Share your improvements as a pull request!*
