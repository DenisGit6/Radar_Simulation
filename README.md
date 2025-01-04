🔧 Technical Overview:

Hardware:

Arduino Uno connected to an HC-SR04 ultrasonic sensor to measure distances.
Serial communication over COM port to stream live data (angle and distance) to a Python script.
Software:

Python Libraries Used:
matplotlib: For real-time radar visualization, including a dynamic scanning line and plotted detected objects.
pyserial: For capturing live data from the Arduino via serial communication.
numpy: For angle and distance calculations to convert data into polar coordinates.
🎥 Here’s a short demo video showcasing the radar in action: (Attach the trimmed video)

💡 How It Works:

The Arduino sends angle-distance pairs over the serial port. For example: 280,37.71.
Python receives this data using pyserial, parses it, and caps the distance to a set maximum range.
The matplotlib polar plot dynamically updates:
A blue scanning line simulates radar movement.
Red dots appear on the radar, marking detected objects' positions based on live data.
✨ Key Challenges:

Ensuring real-time synchronization between the hardware and the radar visualization.
Debugging wiring and sensor setup for accurate readings.
Optimizing the radar plot to represent detected objects clearly and reset the scanning line for clean visualization.
🛠️ What I Gained:

A deeper understanding of serial communication and hardware-software integration.
Real-time data handling and visualization using Python.
Experience in blending technical problem-solving with creativity for an interactive application.
