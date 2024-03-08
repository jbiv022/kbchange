import win32api

# Load the Dvorak keyboard layout
win32api.LoadKeyboardLayout("00010409", 1)  # or "00020409"

print("Keyboard layout changed to Dvorak.")
