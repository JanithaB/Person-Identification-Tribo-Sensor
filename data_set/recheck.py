file_names = ['y1_data.txt', 'y2_data.txt', 'y3_data.txt','y4_data.txt', 'y5_data.txt', 'y6_data.txt']

# Iterate through the file names
for file_name in file_names:
    with open(file_name, 'r') as file:
        content = file.read()
    
    newline_count = content.count('\n')
    
    print(f"Number of newlines in {file_name}: {newline_count}")

# Open the file in read mode
with open('label_data.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Count the number of spaces in the content
space_count = content.count(' ')
one_count = content.count('1')
two_count = content.count('2')

print(f"Number of spaces in the file: {space_count}")
print(f"Number of ones in the file: {one_count}")
print(f"Number of twos in the file: {two_count}")
