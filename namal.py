import csv
import serial.tools.list_ports
from datetime import datetime
import serial
import time

def select_port(silence=True):
    """ this function returns the arduino  com-port """
    # Get a list of all available serial ports
    available_ports = list(serial.tools.list_ports.comports())

    # If no serial ports are found, print an error message and exit the program
    if len(available_ports) == 0:
        print("No available serial ports found.")
        exit()
    if not silence:
        # Print the available serial ports to the console
        print("Available serial ports:")
        for port in available_ports:
            print(port.device)

    # Choose the Arduino serial port
    arduino_port = None
    for port in available_ports:
        if "Arduino" in port.description:
            arduino_port = port.device
            break

    # If an Arduino serial port is not found, print an error message and exit the program
    if arduino_port is None:
        print("Arduino not found on any serial port.")
        exit()

    # Print the chosen Arduino serial port to the console
    print("Arduino found on serial port:", arduino_port)

    return arduino_port





ser = serial.Serial(str(select_port()),115200)  # open serial port
time.sleep(2)

if not ser.isOpen():
    ser.open()
else:
    print('port is open')




while True:
    command =input("Enter the command: ")
    s_time = datetime.now()     # get start time

    all_data_for_a_test =[]      # remember all the data in one drawing
    if command == 's':
        for i in range(500): # take 500 readings
            ser.write(b's')  # this is to tell arduino to send data to python
            line = ser.readline().decode() # arduino returns a line and it's as bytes thus converting to a string

            line=line.split(',')   # line has comma separated values thus splitting by them and taking a list of data
            time = datetime.now() - s_time  # get current time and by the difference taking the time difference
            line.insert(0,time.microseconds)   # insert time into the first position of the list of data

            """ in the below 5 lines the data in the list called line is converted to floats"""
            data_converted_to_numerics = []
            for i in line:
                try:
                    data_converted_to_numerics.append(float(i))
                except:
                    pass

            print(data_converted_to_numerics)
            all_data_for_a_test.append(data_converted_to_numerics) # list of data is added to the all_data_for_a_test

        with open("data.csv", 'a') as csvfile:
            """ here the data is written to the data.csv file"""
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(all_data_for_a_test)

        with open(str(datetime.now().timestamp()),'w')  as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['time','ax','ay','az','gx','gy','gz'])
            # writing the fields
            csvwriter.writerows(all_data_for_a_test)

        print("_____",len(all_data_for_a_test)) # to check how many data point are there not necessary


    elif command == 'f':  # end the program if the command m is issued
        break

ser.close() # close the comport




"""
import os


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Check if the file exists in the same directory as the script
if not os.path.exists(os.path.join(script_dir, "data.csv")):
    with open('data.csv', "w") as f:
        f.write("Hello, world!")

"""
