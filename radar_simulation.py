import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import serial

# Initialize the serial connection
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your actual COM port

# Initialize the radar plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
max_distance = 200  # Set the maximum radar range
ax.set_ylim(0, max_distance)

# Blue scanning line
line, = ax.plot([], [], label="Radar Line", color="blue", lw=2)

# Red dot for detected objects
red_dot, = ax.plot([], [], 'ro', label="Detected Object")  # Single red dot

# Function to update the radar in real time
def update(frame):
    try:
        # Read serial data and parse angle, distance
        data = ser.readline().decode('utf-8').strip()
        print(f"Received data: {data}")  # Debugging
        angle, distance = map(float, data.split(","))

        # Cap distance to max range
        if distance > max_distance:
            distance = max_distance

        # Convert angle to radians
        angle_rad = np.radians(angle)

        # Update the blue scanning line
        line.set_data([angle_rad, angle_rad], [0, max_distance])  # Blue line spans the radar

        # Update the red dot to display detected object
        red_dot.set_data([angle_rad], [distance])

    except Exception as e:
        print(f"Error: {e}")

    return line, red_dot

# Start the animation
ani = FuncAnimation(fig, update, interval=50)  # Updates every 50ms

# Configure the plot
plt.title("Live Radar Simulation with Detected Object")
plt.legend()
plt.show()

# Close the serial connection when done
ser.close()
