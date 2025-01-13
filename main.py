import os

# generate an array of all file names under the main directory (with complete path)
def get_files_in_directory(dir_path):
    file_paths = []  
    for root, _, files in os.walk(dir_path):  
        for file in files:
            file_paths.append(os.path.join(root, file))  # Add the full path of each file to the list
    return file_paths

dir_path = '/Users/jadakisner/Documents/files'  # path to my test directory
all_files = get_files_in_directory(dir_path) 
#print(all_files) 

#  for a given file, parse the contents into an array of lines and break each line into individual words
def read_lines(file_path):
    if os.path.exists(file_path):
        with open(file_path) as file:
            lines = file.readlines()  
        return [line.strip().split() for line in lines]
        

file_path = '/Users/jadakisner/Documents/files/test1.txt' 
lines = read_lines(file_path)

for line_num, words in enumerate(lines, start=1):
    print(f"Line {line_num}: {words}") #adding line numbers for tracking

# NEXT STEPS : to match the command line parameters to the words 
#              in the lines for each file.