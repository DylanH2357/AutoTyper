import json
import time as t
import keyboard as k
import sys
import ctypes
from ctypes import wintypes
import time

k.block_key("a")

'''user32 = ctypes.WinDLL('user32', use_last_error=True)

# Constants
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
VK_A = 0x41  # Virtual Key Code for 'A'

# Define the LowLevelKeyboardProc callback function
def low_level_keyboard_handler(nCode, wParam, lParam):
    if nCode >= 0:
        if wParam == WM_KEYDOWN:
            vk_code = lParam[0]
            if vk_code == VK_A:
                print("Key 'a' pressed")
        elif wParam == WM_KEYUP:
            vk_code = lParam[0]
            if vk_code == VK_A:
                print("Key 'a' released")
    # Call the next hook in the hook chain
    return user32.CallNextHookEx(None, nCode, wParam, lParam)

# Set up the hook
LowLevelKeyboardProc = ctypes.CFUNCTYPE(wintypes.LPARAM, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)
keyboard_hook = LowLevelKeyboardProc(low_level_keyboard_handler)

# Install the hook
keyboard_hook_id = user32.SetWindowsHookExW(WH_KEYBOARD_LL, keyboard_hook, None, 0)

# Message loop
try:
    msg = wintypes.MSG()
    while True:
        if user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))
        time.sleep(0.1)  # Sleep to prevent high CPU usage
finally:
    # Unhook and exit
    user32.UnhookWindowsHookEx(keyboard_hook_id)
'''