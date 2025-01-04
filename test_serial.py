import serial

try:
    ser = serial.Serial('COM3', 9600)  # Replace 'COM4' with your actual COM port
    print("Connection successful!")
    ser.close()
except Exception as e:
    print(f"Error: {e}")
