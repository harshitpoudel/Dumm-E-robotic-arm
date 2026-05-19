"""
Configuration for Dumm-E Robotic Arm

Edit these values for YOUR setup and calibration!
"""

NUM_FINGERS = 5

# Servo channel mapping (PCA9685 channels 0-15); e.g., 0-thumb ... 4-pinky
SERVO_CHANNELS = [0, 1, 2, 3, 4]

# Min/max angles for servos (degrees)
MIN_ANGLE = 0    # Fully open
MAX_ANGLE = 180  # Fully closed

# PWM pulse length (us): MG996R is safe from 500-2500us
SERVO_MIN_PULSE = 500
SERVO_MAX_PULSE = 2500

# Servo reversal (False=normal, True=reversed; use if servo moves opposite direction)
SERVO_REVERSE = [False, False, False, False, False]

# Flex sensor calibration (update per your glove/ESP32 calibration)
FLEX_MIN = [0, 0, 0, 0, 0]      # Sensor value when finger is straight
FLEX_MAX = [1023, 1023, 1023, 1023, 1023]  # Sensor value when fully bent

# Serial communication
SERIAL_PORT = "/dev/ttyACM0"    # Use 'ls /dev/ttyACM*' or 'ls /dev/ttyUSB*' to find your ESP32
SERIAL_BAUDRATE = 115200

# Debug output for troubleshooting (set True for verbose)
DEBUG = False

"""
================== GPIO Reference ==================
- All servo PWM outputs connected to PCA9685 channels 0-4
- PCA9685 module is controlled over I2C (default ESP32 pins: SDA GPIO21 / SCL GPIO22)
- No servo PWM directly from GPIO pins—always use PWM driver!
- For more, see hardware/WIRING.md.
"""
