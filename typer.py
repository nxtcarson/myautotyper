import pyautogui
import time

def type_text(text):
    # Type with a small delay (0.05 seconds) between characters
    pyautogui.write(text, interval=0.05)

def ask_for_input():
    # Allow user to input the text in the console
    text_to_type = input("Enter the text you want to type: ")

    # Wait for the user to switch to the desired window
    print("You have 5 seconds to switch to the window where you want to type.")
    time.sleep(5)  # Wait for 5 seconds for the user to switch windows

    # Call the function to type the input text
    type_text(text_to_type)

    # Ask again if the user wants to type more text
    repeat = input("Do you want to type more text? (yes/no): ").lower()
    if repeat == "yes":
        ask_for_input()  # Recursion to ask for new input again

# Start the process
ask_for_input()
