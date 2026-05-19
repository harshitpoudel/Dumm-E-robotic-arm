/*
  Dumm-E ESP32 DevKit v1 Controller
  ---------------------------------
  Reads 5 flex sensors from glove, maps values to servo angles,
  and drives servos through PCA9685 over I2C.
*/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

#define NUM_SENSORS 5
#define NUM_SERVOS 5

// ESP32 DevKit v1 defaults (configurable)
const int I2C_SDA_PIN = 21;
const int I2C_SCL_PIN = 22;
const uint8_t PCA9685_ADDR = 0x40;

// Use ESP32 ADC1 pins for stable reads
const int flexPins[NUM_SENSORS] = {32, 33, 34, 35, 39};
const uint8_t servoChannels[NUM_SERVOS] = {0, 1, 2, 3, 4};
bool servoReverse[NUM_SERVOS] = {false, false, false, false, false};

int flexVals[NUM_SENSORS];

// Calibration values (ESP32 ADC is 0-4095; tune these placeholders for your glove readings)
const int flexMin[NUM_SENSORS] = {1200, 1200, 1200, 1200, 1200};
const int flexMax[NUM_SENSORS] = {3000, 3000, 3000, 3000, 3000};

const int minAngle = 0;
const int maxAngle = 180;
const int servoMinPulseUs = 500;
const int servoMaxPulseUs = 2500;
const int pcaResolution = 4096;  // 12-bit
const int pwmPeriodUs = 20000;   // 50Hz

Adafruit_PWMServoDriver pca9685 = Adafruit_PWMServoDriver(PCA9685_ADDR);

int flexToAngle(int flexVal, int inMin, int inMax, bool reverse = false) {
  flexVal = constrain(flexVal, inMin, inMax);
  int angle = map(flexVal, inMin, inMax, minAngle, maxAngle);
  if (reverse) {
    angle = maxAngle - (angle - minAngle);
  }
  return constrain(angle, minAngle, maxAngle);
}

void setServoAngle(uint8_t channel, int angle) {
  angle = constrain(angle, minAngle, maxAngle);
  int pulseUs = map(angle, minAngle, maxAngle, servoMinPulseUs, servoMaxPulseUs);
  int pwmTicks = static_cast<int>((pulseUs * pcaResolution * 1.0) / pwmPeriodUs + 0.5);
  pca9685.setPWM(channel, 0, pwmTicks);
}

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < NUM_SENSORS; i++) {
    pinMode(flexPins[i], INPUT);
  }

  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);
  pca9685.begin();
  pca9685.setPWMFreq(50);
  delay(10);

  Serial.println("ESP32 + PCA9685 controller ready");
}

void loop() {
  for (int i = 0; i < NUM_SENSORS; i++) {
    int raw = analogRead(flexPins[i]);
    flexVals[i] = raw;
    int angle = flexToAngle(raw, flexMin[i], flexMax[i], servoReverse[i]);
    setServoAngle(servoChannels[i], angle);
  }

  // Optional debug stream for calibration/logging
  for (int i = 0; i < NUM_SENSORS; i++) {
    Serial.print(flexVals[i]);
    if (i < NUM_SENSORS - 1) {
      Serial.print(",");
    }
  }
  Serial.println();

  delay(10);
}

/*
  ==== Flex Sensor Calibration (ESP32) ====
  - Upload this sketch with board set to "ESP32 Dev Module".
  - Open Serial Monitor at 115200 baud.
  - Note readings when fingers are straight -> flexMin[].
  - Note readings when fingers are fully bent -> flexMax[].
  - Update arrays and re-upload.
*/
