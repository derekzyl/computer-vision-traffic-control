import time

import RPi.GPIO as GPIO

# Define the GPIO pins connected to the 4511 IC inputs
# Assuming the GPIO pins are connected to A, B, C, and D inputs of 4511
pins = [11, 12, 13, 15]  # Change these pins according to your wiring

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BOARD)

# Set up GPIO pins as outputs
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Define BCD values for each digit from 0 to 9
# BCD mapping: [D, C, B, A]
digits = {
    0: [0, 0, 0, 0],
    1: [0, 0, 0, 1],
    2: [0, 0, 1, 0],
    3: [0, 0, 1, 1],
    4: [0, 1, 0, 0],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [0, 1, 1, 1],
    8: [1, 0, 0, 0],
    9: [1, 0, 0, 1]
}

# Function to display a single digit
def display_digit(digit):
    for i in range(4):
        GPIO.output(pins[i], digit[i])

# Example: Display numbers from 0 to 9 repeatedly
try:
    while True:
        for num in range(10):
            display_digit(digits[num])
            time.sleep(1)  # Display each digit for 1 second
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
