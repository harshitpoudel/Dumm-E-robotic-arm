# Parts List: Dumm-E Robotic Arm

For a robust and reliable Dumm-E, here’s the complete Bill of Materials.

| Part                           | Quantity | Notes/Links                                               |
|---------------------------------|---------:|-----------------------------------------------------------|
| **Raspberry Pi 4 Model B**      |      1   | 4GB+ recommended                                          |
| **ESP32 DevKit v1**             |      1   | Main glove + servo controller over I2C/PCA9685           |
| **MG996R Servo Motor**          |      5   | Metal gear, high torque; one per finger                   |
| **PCA9685 PWM Driver (I2C)**    |      1   | 16-channel servo driver                                   |
| **ADS1115 ADC Module (I2C)**    |      1   | Needed if using analog sensors with Pi directly*          |
| **MPU-6050 IMU (GY-521)**       |      1   | Optional: enable motion enhancements                      |
| **Flex Sensor 2.2"**            |      5   | For glove (one per finger)                                |
| **7.4V 2S LiPo Battery**        |      1   | 2200mAh+ recommended                                      |
| **6V 5A UBEC BEC Regulator**    |      1   | Steps LiPo to safe voltage for servos                     |
| **5V 5A Step-Down Regulator**   |      1   | For stable Pi power if not using USB-C supply             |
| **10kΩ Resistors**              |     10   | For flex sensor voltage dividers                          |
| **PLA Filament**                |  1 spool | 3D print structure                                        |
| **PETG Filament**               | ½ spool  | For strong, flexible parts                                |
| **Braided Fishing Line**        |    2 m   | Finger tendon lines                                       |
| **Silicone Elastic Cord**       |   50 cm  | Return springs for fingers                                |
| **M3×10 Screws**                |    Set   | Mechanical assembly                                       |
| **M2.5 Brass Standoffs**        |    Set   | For mounting PCBs                                         |
| **Dupont Jumper Wires**         |    Set   | For breadboard/prototyping                                |
| **Blade Fuse + Holder**         |      1   | LiPo safety                                               |
| **Work Glove**                  |      1   | Choose stretchy & durable                                 |
| **Velcro Straps**               |      2   | Glove-to-arm/hand fitment                                 |
| **Hotglue or Superglue**        |    Tube  | Mechanical assembly                                       |

*If using all flex sensors through ESP32 ADC pins, ADS1115 is optional.

**Tip:** Buy extra jumpers, screws, and fishing line for mistakes and spares.

---

*No part should be powered beyond its rated voltage!*
