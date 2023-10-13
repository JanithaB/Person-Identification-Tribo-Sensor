import serial
import matplotlib.pyplot as plt
from collections import deque
import time
# Configure the serial port
ser = serial.Serial('COM4', 9600)  # Replace 'COMX' with your Arduino's serial port

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



Label=int(input("Enter your value: "))
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
           
       
            x_data.append(len(x_data) + 1)  # Index for x-axis
            y1_data.append(y1_value)  # Append the 'yn' value
            y2_data.append(y2_value)  # Append the 'yn' value
            y3_data.append(y3_value)  # Append the 'yn' value
            y4_data.append(y4_value)  # Append the 'yn' value
            y5_data.append(y5_value)  # Append the 'yn' value
            y6_data.append(y6_value)  # Append the 'yn' value
            
    label_data.append(Label)



            
            #print(y1_value)

    # Convert lists to strings
    y1_data_str = [str(value) for value in y1_data]
    y2_data_str = [str(value) for value in y2_data]
    y3_data_str = [str(value) for value in y3_data]
    y4_data_str = [str(value) for value in y4_data]
    y5_data_str = [str(value) for value in y5_data]
    y6_data_str = [str(value) for value in y6_data]
    
            
    with open('data_set\y1_data.txt', 'a') as y1_file:
        y1_file.write(" ".join(y1_data_str))
        y1_file.write("\n")
    with open('data_set\y2_data.txt', 'a') as y2_file:
        y2_file.write(" ".join(y2_data_str))
        y2_file.write("\n")

    with open('data_set\y3_data.txt', 'a') as y3_file:
        y3_file.write(" ".join(y3_data_str))
        y3_file.write("\n")
    
    with open('data_set\y4_data.txt', 'a') as y4_file:
        y4_file.write(" ".join(y4_data_str))
        y4_file.write("\n")

    with open('data_set\y5_data.txt', 'a') as y5_file:
        y5_file.write(" ".join(y5_data_str))
        y5_file.write("\n")

    with open('data_set\y6_data.txt', 'a') as y6_file:
        y6_file.write(" ".join(y6_data_str))
        y6_file.write("\n")

    plt.subplot(1,3,1)
    plt.plot(x_data, y1_data)
    plt.subplot(1,3,2)
    plt.plot(x_data, y2_data)
    plt.subplot(1,3,3)
    plt.plot(x_data, y3_data)
    plt.show()
    Label=int(input("Enter your value: "))


        
label_data_str =[str(value) for value in label_data]
with open('data_set\label_data.txt', 'a') as label_data_file:
    label_data_file.write(" ".join(label_data_str))
    
    
