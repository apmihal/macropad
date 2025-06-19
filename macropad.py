#!/usr/bin/env python
# coding: utf-8

# Load the gamepad and time libraries
import Gamepad
import time
import subprocess
import sys

# Sends all print() statements to stdout for logging
# An alternative would be print('foo', flush=True) for every print() statement I want logged
sys.stdout.reconfigure(line_buffering=True)

# Gamepad settings
gamepadType = Gamepad.EightBitDoMicro
buttonCenter = 'HEART'
buttonTerminal = 'PLUS'
buttonCopy = 'Y'
buttonPaste = 'X'
buttonShowWindows = 'B'
buttonAlbert = 'L1'
buttonListen = 'L2'
buttonReset = 'R2'
buttonLogout = 'R1'
buttonExit = 'MINUS'
buttonDolphin = 'A'
dpadYAxis = 'DPAD -Y'
dpadXAxis = 'DPAD -X'

#Allows toggling of functionality
listen = True

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
gamepad = gamepadType()
print('Gamepad connected')

# Handle joystick updates one at a time
while gamepad.isConnected():
    # Wait for the next event
    eventType, control, value = gamepad.getNextEvent()

    if listen:
        # Determine the type
        if eventType == 'BUTTON':
            # Button changed
            if control == buttonCenter:
                # Switches to center of desktop grid
                if value:
                    subprocess.run(['xdotool', 'key', 'ctrl+F5'])
            elif control == buttonTerminal:
                # Opens a terminal
                if value:
                    subprocess.run(["xdotool", "key", 'ctrl+alt+t'])
            elif control == buttonExit:
                # Closes focused window
                if value:
                    subprocess.run(["xdotool", "key", 'alt+F4'])
            elif control == buttonCopy:
                # Closes focused window
                if value:
                    subprocess.run(["xdotool", "key", 'ctrl+c'])
            elif control == buttonPaste:
                # Closes focused window
                if value:
                    subprocess.run(["xdotool", "key", 'ctrl+v'])
            elif control == buttonShowWindows:
                # Closes focused window
                if value:
                    subprocess.run(["xdotool", "key", 'super+w'])
            elif control == buttonReset:
                # Toggles compositor
                if value:
                    subprocess.run(["xdotool", "key", 'alt+shift+F12'])
            elif control == buttonDolphin:
                # pulls up search bar
                if value:
                    subprocess.run(["xdotool", "key", 'super+e'])
            elif control == buttonLogout:
                # pulls up search bar
                if value:
                    subprocess.run(["xdotool", "key", 'super+l'])
            elif control == buttonAlbert:
                # pulls up search bar
                if value:
                    subprocess.run(["xdotool", "key", 'ctrl+space'])
            elif control == buttonListen:
                if value:
                    listen = not listen
                    print('not listening')

        elif eventType == 'AXIS':
            # Joystick changed
            if control == dpadYAxis:
                # Speed control (inverted)
                if value == 1:
                    subprocess.run(['xdotool', 'key', 'ctrl+super+Down'])
                elif value == -1:
                    subprocess.run(['xdotool', 'key', 'ctrl+super+Up'])
            elif control == dpadXAxis:
                # Steering control (not inverted)
                if value == 1:
                    subprocess.run(['xdotool', 'key', 'ctrl+super+Right'])
                elif value == -1:
                    subprocess.run(['xdotool', 'key', 'ctrl+super+Left'])

    elif eventType == 'BUTTON':
        if control == buttonListen:
            if value:
                listen = not listen
                print('listening')
        else:
            print('Controls locked. Press L2.')


