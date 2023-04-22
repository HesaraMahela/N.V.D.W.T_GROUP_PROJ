#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
char startKey = 's'; // start key

void setup(void) {
  Serial.begin(115200);

  // Try to initialize!
  if (!mpu.begin()) {
    
    while (1) {
      delay(10);
    }
  }
  

  // set accelerometer range to +-8G
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);

  // set gyro range to +- 500 deg/s
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);

  // set filter bandwidth to 21 Hz
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(20);
}

void loop() {
  if (Serial.available() > 0) {
    char key = Serial.read();
    if (key == startKey) {
      /* Get new sensor events with the readings */
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);

      
      Serial.print(a.acceleration.x);
      Serial.print(',');
      
      Serial.print(a.acceleration.y);
      Serial.print(',');
      Serial.print(a.acceleration.z);
      Serial.print(',');
    
      
      Serial.print(g.gyro.x);
      Serial.print(',');
      Serial.print(g.gyro.y);
      Serial.print(',');
      Serial.print(g.gyro.z);
      Serial.print(',');
      
    
      Serial.println("");
    }
  }

}


