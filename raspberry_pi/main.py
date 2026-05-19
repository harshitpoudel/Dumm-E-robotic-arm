"""
Dumm-E Robotic Arm Controller (Raspberry Pi Side)
-------------------------------------------------
Reads flex sensor values via serial (USB from ESP32 DevKit v1), maps to 5 servos (MG996R) via PCA9685 PWM.
Beginner-friendly, commented, robust.
"""

import time
import serial
import sys
from config import (
    NUM_FINGERS,
    SERVO_CHANNELS,
    MIN_ANGLE,
    MAX_ANGLE,
    SERVO_MIN_PULSE,
    SERVO_MAX_PULSE,
    SERVO_REVERSE,
    FLEX_MIN,
    FLEX_MAX,
    SERIAL_PORT,
    SERIAL_BAUDRATE,
    DEBUG
)

try:
    import board
    import busio
    from adafruit_pca9685 import PCA9685
except ImportError:
    print("ERROR: Adafruit PCA9685 library not found. Install with 'pip install adafruit-circuitpython-pca9685'")
    sys.exit(1)

# Serial communication setup
def open_serial():
    try:
        ser = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
        print(f"Serial port {SERIAL_PORT} opened at {SERIAL_BAUDRATE} baud.")
        return ser
    except serial.SerialException as e:
        print(f"ERROR: Cannot open serial port! Details: {e}")
        sys.exit(1)

# Servo controller setup
def open_pca9685():
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        pwm = PCA9685(i2c)
        pwm.frequency = 50
        print("PCA9685 PWM controller initialized (freq=50Hz).")
        return pwm
    except Exception as e:
        print(f"ERROR: Cannot initialize PCA9685 controller! Check wiring and power. Details: {e}")
        sys.exit(1)

def flex_to_angle(flex_val, flex_min, flex_max, angle_min, angle_max, reverse=False):
    """Map flex sensor value (0-1023) to servo angle (angle_min-angle_max)."""
    flex_val = max(min(flex_val, flex_max), flex_min)
    norm = (flex_val - flex_min) / (flex_max - flex_min) if flex_max > flex_min else 0
    angle = (angle_max - angle_min) * (1 - norm if reverse else norm) + angle_min
    return int(angle)

def set_servo_pwm(pca, channel, angle):
    # Map angle to pulse (approx 500 to 2500 us for MG996R)
    pulse = int((angle - MIN_ANGLE) / (MAX_ANGLE - MIN_ANGLE) * (SERVO_MAX_PULSE - SERVO_MIN_PULSE) + SERVO_MIN_PULSE)
    # Map microseconds pulse to 12-bit value (0–4095) at 50Hz (20,000us period)
    pwm_val = int(pulse * 4096 / 20000)
    pca.channels[channel].duty_cycle = pwm_val

def main():
    print("=== Dumm-E Robotic Arm: Raspberry Pi Controller ===")
    print("Press Ctrl+C to exit.\n")
    ser = open_serial()
    pca = open_pca9685()
    time.sleep(2)
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if ',' not in line:
                continue
            flex_vals = [int(x) for x in line.split(',') if x.strip().isdigit()]
            if len(flex_vals) != NUM_FINGERS:
                if DEBUG:
                    print(f"Received {len(flex_vals)} values instead of {NUM_FINGERS}. Skipping.")
                continue
            for i in range(NUM_FINGERS):
                angle = flex_to_angle(
                    flex_vals[i],
                    FLEX_MIN[i],
                    FLEX_MAX[i],
                    MIN_ANGLE,
                    MAX_ANGLE,
                    SERVO_REVERSE[i]
                )
                if DEBUG:
                    print(f"Finger {i+1} flex:{flex_vals[i]} → angle:{angle}")
                set_servo_pwm(pca, SERVO_CHANNELS[i], angle)
        except KeyboardInterrupt:
            print("\nExiting. Servos disabled.")
            for ch in SERVO_CHANNELS:
                set_servo_pwm(pca, ch, 90)  # Move servos to neutral
            break
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    main()

"""
============== Calibration Notes ==============
- For best accuracy, update FLEX_MIN and FLEX_MAX for your glove's actual 'straight' and 'fully bent' values. Edit config.py.
- To reverse a servo's direction (e.g., servo turns opposite finger), set SERVO_REVERSE[] to True.
- Ensure power OFF when wiring!
- Always use a UBEC (6V, 5A) for the servo supply.
- Servos and Raspberry Pi must have a *common ground*.
"""
