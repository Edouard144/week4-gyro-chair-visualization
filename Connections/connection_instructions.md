# Connection Instructions

## Components
- Arduino UNO
- MPU6050 Gyroscope/Accelerometer module
- Breadboard + jumper wires
- USB cable (for Arduino connection)

## Steps
1. Connect the MPU6050 as follows:
   - VCC → 5V on Arduino
   - GND → GND
   - SDA → A4
   - SCL → A5

2. Upload the Arduino sketch: `mpu6050_chair.ino`.

3. Open the Python script (e.g. `visualize_2d_pitch.py`) and make sure the serial port (e.g. `COM3`) matches your system.

4. Run the Python file and tilt the sensor — your visualization updates live.

## Tip
If the sensor doesn’t respond:
- Check wire connections.
- Try switching SDA/SCL pins if using a different board (like Arduino Mega).
- Ensure `MPU6050` library is installed in Arduino IDE.
