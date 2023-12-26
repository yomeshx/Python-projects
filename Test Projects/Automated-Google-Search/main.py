import webbrowser
import subprocess
import time

def mode():
    while True:
        usermode = input("\n---------------------------------------\nChoose The Mode A (Auto) / M (Manual) \n------------------> | : ").lower()
        if usermode == "a":
            return True
        elif usermode == "m":
            return False
        else:
            print("Please enter the correct mode selection !")
            continue

def ask_sleep(): #sleep interval after each iteration
    ask_sleep = int(input("\nEnter Sleep Interval : "))
    return ask_sleep

def open_google_tab(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def read_lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    file_path = "input.txt"  # Change this to your input file path
    lines = read_lines_from_file(file_path)
    total_lines = len(lines)
    current_line_index = 0
    
    sleep_time = ask_sleep()
    automatic_mode = mode()  # Mode Automatic (every x second after new tab) or Manual (By use inputs)

    repeat_previous_search = False

    while current_line_index < total_lines:
        if repeat_previous_search:
            current_line_index -= 1
            repeat_previous_search = False

        current_line = lines[current_line_index]
        search_query = current_line.split("\\")[-1]

        open_google_tab(search_query)
        print(f"Searching for: {search_query}")

        time.sleep(sleep_time)

        print(f"Total lines: {total_lines}, Lines left: {total_lines - current_line_index - 1}")

        if automatic_mode:
            current_line_index += 1
        else:
            user_input = input("\n             ---------Press---------\n\n------| Next search ('\\') \n------| previous search (']')\n------| pause ('p')\n------| continue (c)\n------| Stop (Tab)\n\n---------------------->:")

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
