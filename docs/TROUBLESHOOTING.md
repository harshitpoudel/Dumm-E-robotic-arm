# Troubleshooting: Dumm-E Robotic Arm

Having trouble with your Dumm-E? Here’s how to diagnose and fix common problems.

---

## Table of Contents

- [Serial Communication Issues](#serial-communication-issues)
- [Servo Issues](#servo-issues)
- [Flex Sensor Issues](#flex-sensor-issues)
- [Wiring Faults](#wiring-faults)
- [General Errors](#general-errors)
- [Power/Safety Issues](#powersafety-issues)
- [Recommended Future Upgrades](#recommended-future-upgrades)

---

## Serial Communication Issues

- **ESP32 not found?**
  - Run `ls /dev/ttyUSB*` or `ls /dev/ttyACM*`.
  - Check your cable and port.
  - Try lowering baudrate if you have errors.

- **Strange characters or garbled data?**
  - Make sure firmware and Serial Monitor use the same baudrate (default \= 115200).
  - USB hub may cause issues. Try plugging ESP32 directly into your computer.

---

## Servo Issues

- **Servos twitch or don’t move?**
  - Confirm external 6V supply to PCA9685 “V+” (not ESP32 board 5V!).
  - Check common ground—missing GND will prevent PWM from working.
  - Check for reversed servo connector (brown = GND, red = V+, yellow/orange = PWM).
  - Use `servoChannels[]` and `servoReverse[]` in the ESP32 sketch for mapping/fixing rotation.

- **Servos buzz but don’t move?**
  - Power supply is too weak—use at least 5A UBEC.
  - Some MG996R servos have high stall current; add a small capacitor across power lines for stability.

---

## Flex Sensor Issues

- **Sensors not responding or values stuck?**
  - Check flex sensor wiring (refer to schematic in [`hardware/WIRING.md`](../hardware/WIRING.md)).
  - Inspect solder joints, use multimeter for continuity.
  - Double-check 10kΩ resistors to ground.

- **Calibration off / movement imprecise?**
  - Carefully calibrate `flexMin[]` and `flexMax[]` in ESP32 code for YOUR glove.
  - Use Serial Monitor to log sensor readings for each flex/bend position.

---

## Wiring Faults

- **No movement or odd servos?**
  - Recheck all V+ and GND wires.
  - Inspect for shorts or loose wires.
  - Ensure ESP32, PCA9685, and servo supply share common ground.

---

## General Errors

- **Python script errors on import?**
  - Run `pip install -r requirements.txt` inside `raspberry_pi/` directory.

- **PCA9685 not detected?**
  - Run `i2cdetect -y 1` to check device appears (usually as `0x40`).

---

## Power/Safety Issues

- **Pi suddenly shuts down?**
  - Never power Pi from servo V+ rail or BEC.
  - Use quality USB-C power if using Pi 4.

- **Servos/UBEC feel VERY hot?**
  - Check for jammed gears or high resistance in tendons.

---

## Recommended Future Upgrades

- Support for wireless glove (Bluetooth).
- Add current sensor for servo power monitoring.
- Add OLED status display or beep for errors.
- Add force/resistance sensors on fingertips.
- Build a custom PCB for compact wiring.

---

Still stuck?  
- Ask for help in Issues or Discussions on this repo!
- Share photos of your wiring for quick diagnosis.

*Keep calm and debug on!*
