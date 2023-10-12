# Specify the path to your text file
file_path = 'y3_data.txt'

# Initialize a list to store the element counts for each line
element_counts = []

# Open the file in read mode
with open(file_path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into elements using spaces as the separator
        elements = line.strip().split()
        
        # Count the number of elements in the line and append it to the list
        element_count = len(elements)
        element_counts.append(element_count)

# Print the element counts for each line
for i, count in enumerate(element_counts, start=1):
    print(f'Line {i}: {count} elements')
