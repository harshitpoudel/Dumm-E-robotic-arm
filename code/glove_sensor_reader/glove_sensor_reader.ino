/*
  Dumm-E Glove Sensor Reader (for Arduino Nano/Uno)
  -------------------------------------------------
  Reads 5 flex sensors, outputs comma-separated values to serial.
  Fully commented for beginners.
*/

#define NUM_SENSORS 5

const int flexPins[NUM_SENSORS] = {A0, A1, A2, A3, A4}; // Flex sensors wired to analog pins
int flexVals[NUM_SENSORS];

// Calibration values: Update after calibrating your glove!
const int flexMin[NUM_SENSORS] = {300, 310, 315, 320, 325};  // Replace with your straight-finger readings
const int flexMax[NUM_SENSORS] = {700, 720, 715, 725, 730};  // Replace with your full-bend readings

void setup() {
  Serial.begin(115200); // Use fast baud rate for smooth control
  for (int i = 0; i < NUM_SENSORS; i++) {
    pinMode(flexPins[i], INPUT);
  }
  Serial.println("Ready");
}

void loop() {
  for (int i = 0; i < NUM_SENSORS; i++) {
    int val = analogRead(flexPins[i]);
    // Map value to 0–1023 range (custom calibrate if necessary)
    val = constrain(val, flexMin[i], flexMax[i]);
    int mapped = map(val, flexMin[i], flexMax[i], 0, 1023); // 0:straight, 1023:bent
    flexVals[i] = mapped;
  }

  // Output comma-separated sensor values (e.g., 100,350,600,1023,230)
  for (int i = 0; i < NUM_SENSORS; i++) {
    Serial.print(flexVals[i]);
    if (i < NUM_SENSORS - 1) Serial.print(",");
  }
  Serial.println();
  delay(10); // ~100Hz update rate
}

/*
  ==== Flex Sensor Calibration Instructions ====
  - Upload this sketch.
  - Open Serial Monitor. Note values when fingers are straight — use as flexMin[] above.
  - Bend each finger fully, note readings — use as flexMax[].
  - Update the arrays, re-upload code for accurate motion mapping.
*/