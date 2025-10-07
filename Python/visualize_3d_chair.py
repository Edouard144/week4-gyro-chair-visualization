import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Connect to Arduino (change COM3 to your port)
ser = serial.Serial('COM3', 9600)
time.sleep(2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_chair(ax, R):
    seat = np.array([[1, 1, 0], [-1, 1, 0], [-1, -1, 0], [1, -1, 0]])
    back = np.array([[1, 1, 0], [-1, 1, 0], [-1, 1, 2], [1, 1, 2]])
    legs = [
        np.array([[1, 1, 0], [1, 1, -2]]),
        np.array([[-1, 1, 0], [-1, 1, -2]]),
        np.array([[1, -1, 0], [1, -1, -2]]),
        np.array([[-1, -1, 0], [-1, -1, -2]])
    ]

    seat = seat @ R.T
    back = back @ R.T
    legs = [leg @ R.T for leg in legs]

    # Draw seat
    for i in range(4):
        j = (i + 1) % 4
        ax.plot([seat[i, 0], seat[j, 0]], [seat[i, 1], seat[j, 1]], [seat[i, 2], seat[j, 2]], color='brown', lw=2)

    # Draw back
    for i in range(4):
        j = (i + 1) % 4
        ax.plot([back[i, 0], back[j, 0]], [back[i, 1], back[j, 1]], [back[i, 2], back[j, 2]], color='sienna', lw=2)

    # Draw legs
    for leg in legs:
        ax.plot(leg[:, 0], leg[:, 1], leg[:, 2], color='black', lw=2)

while True:
    line = ser.readline().decode().strip()
    try:
        pitch, roll, yaw = map(float, line.split(','))
    except:
        continue

    ax.cla()
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_title(f"Pitch: {pitch:.1f}° | Roll: {roll:.1f}° | Yaw: {yaw:.1f}°")

    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(np.radians(pitch)), -np.sin(np.radians(pitch))],
        [0, np.sin(np.radians(pitch)), np.cos(np.radians(pitch))]
    ])
    Ry = np.array([
        [np.cos(np.radians(roll)), 0, np.sin(np.radians(roll))],
        [0, 1, 0],
        [-np.sin(np.radians(roll)), 0, np.cos(np.radians(roll))]
    ])
    Rz = np.array([
        [np.cos(np.radians(yaw)), -np.sin(np.radians(yaw)), 0],
        [np.sin(np.radians(yaw)), np.cos(np.radians(yaw)), 0],
        [0, 0, 1]
    ])

    R = Rz @ Ry @ Rx
    draw_chair(ax, R)
    plt.pause(0.01)
