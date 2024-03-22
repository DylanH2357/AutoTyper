import json
import time as t
import keyboard as k
import sys
import os
import pynput as p
from ahk import AHK

ahk = AHK()
textDir = f"{os.path.dirname(__file__)}\\Texts"
configDir = f"{os.path.dirname(__file__)}\\Configs"
suppressedKeys = ["a", "b", "d", "e", "f", 
                  "g", "h", "i", "j", "k",
                  "l", "m", "n", "o", "p",
                  "q", "r", "s", "t", "u",
                  "v", "w", "x", "y", "z",
                  ";", ",", ".", "/"]

def suppress_keyboard():
    """
    Suppresses keyboard inputs by rebinding most key presses to left shift. 
    This makes it easier to register an individual keypress of any key to perform an action.
    """
    
    print("Suppressing keyboard")
        
    # for i in suppressedKeys:
    #     k.remap_key(i, "shift")
    
    appliedConfig = open(f"{configDir}\\AppliedWindowsConfig.ahk", "w+")
    with open(f"{configDir}\\WindowsConfig.ahk", "r") as config:
        print("Applying config")
        for i in config:
            i = i.replace("keybinding", "LShift")
            appliedConfig.write(i)
        
    ahk.run_script(f"{configDir}\\AppliedWindowsConfig.ahk", blocking=True)
    
def regain_keyboard():
    """
    Reapplies standard keyboard bindings
    """
    
    print("Regaining keyboard")
    k.press_and_release("esc")
    # ahk.run_script(f"{configDir}\\DefaultWindowsConfig.ahk")

def main_program():
    """
    Performs main program functions and logic

    Returns:
        null
    """
    
    print("The program will begin when the control key is pressed twice within a second...")
    ctrl_pressed_time = 0
    ctrl_pressed_count = 0
    right_shift_pressed_time = 0
    right_shift_pressed_count = 0
    alt_pressed_time = 0
    alt_pressed_count = 0

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
        "text1": open(f"{textDir}\\ExampleText.txt", "r").read(),
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
            if event.name == "esc":
                current_time = t.time()
                # Check if it's within 1 second since the last esc press
                if current_time - right_shift_pressed_time <= 1:
                    right_shift_pressed_count += 1
                else:
                    right_shift_pressed_count = 1
                right_shift_pressed_time = current_time
                # If esc pressed twice within a second
                if right_shift_pressed_count == 2:
                    print("Exiting Program")
                    regain_keyboard()
                    sys.exit()
                    
            # for switching between texts: (alt)
            if event.name == "alt":
                current_time = t.time()
                # Check if it's within 1 second since the last return press
                if current_time - alt_pressed_time <= 1:
                    alt_pressed_count += 1
                else:
                    alt_pressed_count = 1
                alt_pressed_time = current_time
                # If return pressed twice within a second
                if alt_pressed_count == 2:
                    print("Switching Texts")
                    i = 0  # go to the beginning of the text
                    j = (j + 1) % len(texts)
                    currentText = texts[(list(texts.keys())[j])]

            if paused == False and event.name not in ["ctrl", "alt", "esc", "up", "down", "right"]:
                k.write(currentText[i], delay=0, restore_state_after=True, exact=None)
                print(f"Character {i}")
                i += 1

    print("Text completed")
    regain_keyboard()
    sys.exit()
    
try:
    main_program()
except:
    regain_keyboard()
    sys.exit()