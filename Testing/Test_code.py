from tensorflow.keras.models import load_model
import serial
import matplotlib.pyplot as plt
from collections import deque
import time
import numpy as np

model = load_model("CNN_PRETRAINED_MODEL.h5")

# Configure the serial port
ser = serial.Serial('COM5', 9600)  # Replace 'COMX' with your Arduino's serial port

# Initialize data storage
max_data_points = 1000  # Adjust as needed
x_data = []
y1_data = []
y2_data = []
y3_data = []
y4_data = []
y5_data = []
y6_data = []
label_data=[]
y_data =[]



Label=int(input("Enter 1 to continue: "))
while(Label>0):
    x_data = []
    y1_data = []
    y2_data = []
    y3_data = []
    y4_data = []
    y5_data = []
    y6_data = []
    
    y_data =[]

    for i in range(200):
        serial_line = ser.readline().decode('utf-8').strip()  # Read a line from serial
        serial_line = serial_line.split()
        
        print(serial_line)
        print(i)
        
        if serial_line:
            y1_value = float(serial_line[0])  # Extract the 'yn' value
            y2_value = float(serial_line[1])
            y3_value = float(serial_line[2])
            y4_value = float(serial_line[3])  # Extract the 'yn' value
            y5_value = float(serial_line[4])
            y6_value = float(serial_line[5])
           
       
            y1_data.append(y1_value)  # Append the 'yn' value
            y2_data.append(y2_value)  # Append the 'yn' value
            y3_data.append(y3_value)  # Append the 'yn' value
            y4_data.append(y4_value)  # Append the 'yn' value
            y5_data.append(y5_value)  # Append the 'yn' value
            y6_data.append(y6_value)  # Append the 'yn' value

            y1_data_all = np.array(y1_data)
            y2_data_all = np.array(y2_data)
            y3_data_all = np.array(y3_data)
            y4_data_all = np.array(y4_data)
            y5_data_all = np.array(y5_data)
            y6_data_all = np.array(y6_data)
            
    
    combined_y_data = np.column_stack((y1_data, y2_data, y3_data, y4_data, y5_data, y6_data))

    input_sample = combined_y_data.reshape(1, 200, 6)

    # Make a prediction for the input sample
    predicted_label = model.predict(input_sample)

    # Convert the one-hot encoded predicted label back to binary label (0 or 1)
    predicted_label_binary = np.argmax(predicted_label, axis=1)

    #print(f"Predicted Label: {predicted_label_binary[0]}")

    if (predicted_label_binary == 0):
        print("Narendra")

    elif(predicted_label_binary == 1):
        print("Janitha")

    else:
        print("Other")
        
    Label=int(input("Enter your value: "))

