#Here's a simple Python program using the subprocess module to open Google Chrome tabs
#-and the time module for handling delays. 
#The program assumes that the text file is named "input.txt." 


#Make sure to replace "input.txt" with the actual path to your input file. 
#This program uses the subprocess module to open Google Chrome tabs, 
#and it prints information about the progress in the terminal.

import subprocess
import time
import os

#------------When using windows-------------
def open_google_tab(query):
    url = f"https://www.google.com/search?q={query}"
    subprocess.run(["start", url], shell=True)

#------------When using Linux-------------
# def open_google_tab(query):
#     url = f"https://www.google.com/search?q={query}"
#     subprocess.run(["google-chrome", "--new-tab", url])
#-----------------------------------------
def read_lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# def read_lines_from_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#     return [line.strip() for line in lines]

def main():
    file_path = "D:\\G\\Git\\Python-projects\\Test Projects\\Automated-Google-Search\\input.txt"  # Change this to your input file path
    lines = read_lines_from_file(file_path)
    total_lines = len(lines)
    current_line_index = 0

    automatic_mode = True  # Change to False for user mode
    repeat_previous_search = False

    while current_line_index < total_lines:
        if repeat_previous_search:
            current_line_index -= 1
            repeat_previous_search = False

        current_line = lines[current_line_index]
        search_query = current_line.split("\\")[-1]

        open_google_tab(search_query)
        print(f"Searching for: {search_query}")

        time.sleep(7)

        print(f"Total lines: {total_lines}, Lines left: {total_lines - current_line_index - 1}")
        
        if automatic_mode:
            current_line_index += 1
        else:
            user_input = input("Press '\\' for the next search, ']' to repeat the previous search, 'p' to pause, 'c' to continue, and 'tab' to stop: ")

            if user_input == '\\':
                current_line_index += 1
            elif user_input == ']':
                repeat_previous_search = True
            elif user_input == 'p':
                time.sleep(7)  # Pause for 7 seconds
            elif user_input == 'c':
                continue
            elif user_input == 'tab':
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
