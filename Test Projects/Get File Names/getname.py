import os

# Specify the directory path
directory_path = '/home/yomesh/Documents'

# Create a list to store file names and paths
file_list = []

# Iterate through the files in the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)

# Specify the output text file
output_file = '/home/yomesh/Documents/File_list.txt'

# Write the file names and paths to the text file with UTF-8 encoding
with open(output_file, 'w', encoding='utf-8') as file:
    for file_path in file_list:
        file.write(file_path + '\n')

print(f'File names and paths have been written to {output_file}')
