import win32api

# To switch to English (US) layout
win32api.LoadKeyboardLayout('00000409', 1)

# To switch to Arabic layout
win32api.LoadKeyboardLayout('00000401', 1)

# For Dvorak layout
win32api.LoadKeyboardLayout("00010409", 1)  # or "00020409"
