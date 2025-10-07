import serial
import time
import matplotlib.pyplot as plt

# Connect to Arduino
ser = serial.Serial('COM3', 9600)
time.sleep(2)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', lw=2)
ax.set_xlim(0, 100)
ax.set_ylim(-90, 90)
ax.set_xlabel('Time')
ax.set_ylabel('Pitch (°)')
ax.set_title('2D Pitch Visualization')

pitch_data = []
time_data = []

i = 0
while True:
    line_str = ser.readline().decode().strip()
    try:
        pitch, roll, yaw = map(float, line_str.split(','))
    except:
        continue

    pitch_data.append(pitch)
    time_data.append(i)
    i += 1

    if len(time_data) > 100:
        time_data.pop(0)
        pitch_data.pop(0)

    line.set_data(time_data, pitch_data)
    ax.relim()
    ax.autoscale_view()
    plt.pause(0.01)
