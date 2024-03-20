import json
import time as t
import keyboard as k
import sys
import os

'''

sudo python3 path_to_your_file/KeyboardRemapping.py

'''

textDir = os.path.dirname()

def suppress_keyboard():
    """
    Suppresses keyboard inputs by rebinding most key presses to left shift. 
    This makes it easier to register an individual keypress of any key to perform an action.
    """
    
    keyCode = "left_shift"  # KeyCode #1
    # Define the path to the Karabiner JSON file
    karabinerFilePath = "path_to_your_file/.config/karabiner/karabiner.json"
    macConfigPath = f"{os.path.dirname()}macConfig.json"

    with open(karabinerFilePath, "r") as file:
        data = json.load(file)

    newRules = json.load(macConfigPath)
    
    # Replaces all "keycode" values in the config file with the keycode here for easy changes
    for i in newRules["manipulators"]["to"]:
        i["key_code"] = i["key_code"].replace("keyCode", keyCode)

    # Update the "rules" portion with the new rule
    data["profiles"][0]["complex_modifications"]["rules"].append(newRules)
    
    # Write the modified JSON back to the file
    with open(karabinerFilePath, "w") as file:
        json.dump(data, file, indent=4)


def regain_keyboard():
    """
    Reapplies the standard Karabiner keybinding profile to return the keyboard to normal
    """
    
    karabinerFilePath = "path_to_your_file/.config/karabiner/karabiner.json"
    
    with open(karabinerFilePath, "r") as file:
        data = json.load(file)
    
    # Set the "rules" portion to an empty list
    data["profiles"][0]["complex_modifications"]["rules"] = []
    
    # Write the modified JSON back to the file
    with open(karabinerFilePath, "w") as file:
        json.dump(data, file, indent=4)


def main_program():
    """
    Performs main program functions

    Returns:
        null
    """
    
    print("The program will begin when the control key is pressed twice within a second...")
    ctrl_pressed_time = 0
    ctrl_pressed_count = 0
    right_shift_pressed_time = 0
    right_shift_pressed_count = 0
    command_pressed_time = 0
    command_pressed_count = 0

    while ctrl_pressed_count < 2:
        event = k.read_event()
        if event.event_type == "down":  # check for key press
            if event.name == "ctrl":
                current_time = t.time()
                # Check if it's within 1 second since the last ctrl press
                if current_time - ctrl_pressed_time <= 1:
                    ctrl_pressed_count += 1
                else:
                    ctrl_pressed_count = 1
                ctrl_pressed_time = current_time
    
    print("Starting program")

    suppress_keyboard()

    texts = {
        "text1": open(f"{textDir}ExampleText.txt", "r"),
        "text2": "This is text #2, and that's pretty cool",
        "text3": "This is text #3, and that's pretty cool",
        "text4": "This is text #4, and that's pretty cool",
        "text5": "This is text #5, and that's pretty cool",
        "text6": "This is text #6, and that's pretty cool",
        "text7": "This is text #7, and that's pretty cool",
        "text8": "This is text #8, and that's pretty cool",
        "text9": "This is text #9, and that's pretty cool",
        "text10": "This is text #10, and that's pretty cool",
        "text11": "This is text #11, and that's pretty cool",
        "text12": "This is text #12, and that's pretty cool",
        "text13": "This is text #13, and that's pretty cool",
        "text14": "This is text #14, and that's pretty cool",
        "text15": "This is text #15, and that's pretty cool",
        "text16": "This is text #16, and that's pretty cool",
        "text17": "This is text #17, and that's pretty cool",
        "text18": "This is text #18, and that's pretty cool",
        "text19": "This is text #19, and that's pretty cool",
        "text20": "This is text #20, and that's pretty cool"
    }

    paused = False
    i = 0  # initial value of i (place value in text)
    j = 0  # initial value of j (the specific text you are in)
    currentText = texts[(list(texts.keys())[j])]
    
    while i < len(currentText):
        event = k.read_event()
        if event.event_type == "down":  # check for key press      
            # for pausing the program
            if event.name == "ctrl":
                current_time = t.time()
                # Check if it's within 1 second since the last ctrl press
                if current_time - ctrl_pressed_time <= 1:
                    ctrl_pressed_count += 1
                else:
                    ctrl_pressed_count = 1
                ctrl_pressed_time = current_time
                # If ctrl pressed twice within a second
                if ctrl_pressed_count == 2 and not paused:  # if not paused
                    print("Pausing Program")
                    regain_keyboard()
                    paused = True  # now paused
                else:  # if paused
                    print("Resuming Program")
                    suppress_keyboard()
                    paused = False  # now unpaused

            # for exiting the program
            if event.name == "right shift":
                current_time = t.time()
                # Check if it's within 1 second since the last right shift press
                if current_time - right_shift_pressed_time <= 1:
                    right_shift_pressed_count += 1
                else:
                    right_shift_pressed_count = 1
                right_shift_pressed_time = current_time
                # If right shift pressed twice within a second
                if right_shift_pressed_count == 2:
                    print("Exiting Program")
                    regain_keyboard()
                    sys.exit()
                    
            # for switching between texts: (command)
            if event.name == "command":
                current_time = t.time()
                # Check if it's within 1 second since the last return press
                if current_time - command_pressed_time <= 1:
                    command_pressed_count += 1
                else:
                    command_pressed_count = 1
                command_pressed_time = current_time
                # If return pressed twice within a second
                if command_pressed_count == 2:
                    print("Switching Texts")
                    i = 0  # go to the beginning of the text
                    j = (j + 1) % len(texts)
                    currentText = texts[(list(texts.keys())[j])]

            if paused == False and event.name not in ["ctrl", "command", "right shift", "up", "down", "right"]:
                k.write(currentText[i], delay=0, restore_state_after=True, exact=None)
                print(i)
                i += 1

    regain_keyboard()

try:
    main_program()
except:
    regain_keyboard()

'''

sudo python3 path_to_your_file/MacKeyboardRemapper.py

'''