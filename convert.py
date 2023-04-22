import numpy as np

# Open the file for reading
with open('data.csv', 'r') as f:
    # Read the lines and remove the newlines
    lines = [line.strip('\"') for line in f.readlines()]
print(lines)


"""
# Parse each line as a list of floats and add it to a list
data = []
for line in lines:
    values = [float(x.strip()) for x in line.strip('[]').split(',')]
    data.append(values)

# Convert the list of lists to a NumPy array
data_np = np.array(data)

"""


import re

file_data = "[0.0, -1.37, -9.81, -0.91, 0.01, 0.0, 0.01] [973628.0, -1.4, -9.79, -0.89, 0.01, 0.0, 0.02] "

numbers_regex = r'[-+]?\d*\.\d+|[-+]?\d+'  # regex pattern for floating-point and integer numbers


numbers_list = re.findall(numbers_regex, file_data)  # extracting numbers using regex

print(numbers_list)
from datetime import datetime
import csv

all_data_for_a_test=[[0.0, -1.37, -9.81, -0.91, 0.01, 0.0, 0.01],[973628.0, -1.4, -9.79, -0.89, 0.01, 0.0, 0.02],[954977.0, -1.37, -9.82, -0.9, 0.01, -0.0, 0.0]]
name = str(datetime.now().timestamp()) +'.csv'

with open(name, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, escapechar=' ', quoting=csv.QUOTE_NONE)
    csvwriter.writerow(['time', 'ax', 'ay', 'az', 'gx', 'gy', 'gz'])
    # writing the fields
    csvwriter.writerows(all_data_for_a_test)