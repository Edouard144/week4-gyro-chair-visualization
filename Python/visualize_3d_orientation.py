import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ser = serial.Serial('COM3', 9600)
time.sleep(2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

while True:
    line = ser.readline().decode().strip()
    try:
        pitch, roll, yaw = map(float, line.split(','))
    except:
        continue

    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_title(f"Pitch: {pitch:.1f}°, Roll: {roll:.1f}°")

    # Create a plane (like a board)
    X = np.array([[-1, 1], [-1, 1]])
    Y = np.array([[-1, -1], [1, 1]])
    Z = np.zeros((2, 2))

    # Apply pitch and roll
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(np.radians(pitch)), -np.sin(np.radians(pitch))],
                   [0, np.sin(np.radians(pitch)), np.cos(np.radians(pitch))]])
    Ry = np.array([[np.cos(np.radians(roll)), 0, np.sin(np.radians(roll))],
                   [0, 1, 0],
                   [-np.sin(np.radians(roll)), 0, np.cos(np.radians(roll))]])

    R = Ry @ Rx

    for i in range(2):
        for j in range(2):
            v = np.array([X[i, j], Y[i, j], Z[i, j]])
            v_rot = R @ v
            X[i, j], Y[i, j], Z[i, j] = v_rot

    ax.plot_surface(X, Y, Z, color='skyblue', alpha=0.8)
    plt.pause(0.01)
