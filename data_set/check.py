# Specify the path to your text file
file_path = 'y1_data.txt'

# Initialize a line count variable
line_count = 0

# Open the file in read mode
with open(file_path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Increment the line count for each line
        line_count += 1

# Print the total number of lines
print(f'Total number of lines in the file: {line_count}')
