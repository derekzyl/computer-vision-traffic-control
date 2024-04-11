import time

import RPi.GPIO as GPIO

from tracker import callLight
from traffic_time import calculate_light_time
from videos import capture_lane_video

# Set GPIO mode and configure pins

GPIO.setmode(GPIO.BCM)
# 3
# 5
# 7
# 11
# 13
# 15
# 19
# 21
# 23
# 29
# 31
# 33
# 35
# 37


vehicle_count_x1 = 0
vehicle_count_x2 = 0
vehicle_count_y1 = 0
vehicle_count_y2 = 0


vehicle_counts: dict[str, int] = {
    "vehicle_count_x1": vehicle_count_x1,
    
    "vehicle_count_x2": vehicle_count_x2,
    

    "vehicle_count_y1": vehicle_count_y1,
    "vehicle_count_y2": vehicle_count_y2,
}


s = [vehicle_count_x1,  vehicle_count_y1, vehicle_count_x2, vehicle_count_y2] # lane_1, lane_2, lane_3, lane_4

video_names = ['lane_1.mp4', 'lane_2.mp4', 'lane_3.mp4', 'lane_4.mp4']

def get_vehicles_count():
    global vehicle_count_x1, vehicle_count_x2, vehicle_count_y1, vehicle_count_y2,  vehicle_counts
    for i in range(4):
        capture_lane_video(i)
    for i in range(4):
       count = callLight(source=video_names[i])
       vehicle_counts[i] = count["total_count"]
       
       



def get_traffic_time():
    
    """
    The function `get_traffic_time` calculates the traffic light times for two directions based on
    vehicle counts.
    :return: The function `get_traffic_time` is returning the values of `x` and `y`, which are
    calculated by calling the functions `calculate_light_time` with specific parameters.
    """
    global vehicle_count_x1, vehicle_count_x2, vehicle_count_y1, vehicle_count_y2
    get_vehicles_count()
    x= calculate_light_time(type="x", max_in_x=max(vehicle_count_x1, vehicle_count_x2), max_in_y=max(vehicle_count_y1, vehicle_count_y2))
    y= calculate_light_time(type="y", max_in_x=max(vehicle_count_x1, vehicle_count_x2), max_in_y=max(vehicle_count_y1, vehicle_count_y2))

    print(f'traffic time  x: {x}, y: {y}')

    return x, y
        

get_traffic_time()


# the led light indicators
ledRedX, ledYellowX, ledGreenX = 17, 27, 22
ledRedY, ledYellowY, ledGreenY = 5, 6, 13 

# the motor controller pins 
IN1, IN2, IN3, IN4 = 23, 24, 25,8


#  responsible to show the count down timer 
SegmentPinAX, SegmentPinBX, SegmentPinCX, SegmentPinDX = 4, 14, 15, 18
SegmentPinAY, SegmentPinBY, SegmentPinCY, SegmentPinDY = 12, 16, 20, 21



#  responsible to show the count down timer
multiplex1, multiplex2, multiplex3 = 2, 3, 4


# def get_vehicles_count():
#     global vehicle_count_x1, vehicle_count_x2, vehicle_count_y1, vehicle_count_y2
#     for i in range(4):
#        count = callLight(source=video_names[i])



# Set GPIO mode and configure pins
GPIO.setmode(GPIO.BCM)

# set up leds
for i in [ledRedX, ledYellowX, ledGreenX, ledRedY, ledYellowY, ledGreenY]:
    GPIO.setup(i, GPIO.OUT)
# setup stepper motor    
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# setup 7 segment display
for i in [SegmentPinAX, SegmentPinBX, SegmentPinCX, SegmentPinDX, SegmentPinAY, SegmentPinBY, SegmentPinCY, SegmentPinDY]:
    GPIO.setup(i, GPIO.OUT)


# set up multiplexers
for i in [multiplex1, multiplex2, multiplex3]:
    GPIO.setup(i, GPIO.OUT)


# lets set up the timer for the lightgett

# Define constants
DEG_PER_STEP = 1.8
STEPS_PER_REVOLUTION = int(360 / DEG_PER_STEP)

# Define sequence for 28BYJ-48 stepper motor
seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Function to rotate the stepper motor one step
def step(delay, step_sequence):
    for i in range(4):
        GPIO.output(IN1, step_sequence[i][0])
        GPIO.output(IN2, step_sequence[i][1])
        GPIO.output(IN3, step_sequence[i][2])
        GPIO.output(IN4, step_sequence[i][3])
        time.sleep(delay)

# Function to move the stepper motor one step forward and captures image as it progresses
def step_forward(delay, steps):
    for _ in range(steps):
        capture_lane_video("1")
        step(delay, seq[0])
        capture_lane_video("2")
        
        step(delay, seq[1])
        capture_lane_video("3")
        step(delay, seq[2])
        capture_lane_video("4")
        step(delay, seq[3])

# Function to move the stepper motor one step backward
def step_backward(delay, steps):
    for _ in range(steps):
        step(delay, seq[3])
        step(delay, seq[2])
        step(delay, seq[1])
        step(delay, seq[0])

try:
    # Set the delay between steps
    delay = 0.005

    while True:
        # Rotate one revolution forward (clockwise)
        step_forward(delay, STEPS_PER_REVOLUTION)

        # Pause for 2 seconds
        time.sleep(2)

        # Rotate one revolution backward (anticlockwise)
        step_backward(delay, STEPS_PER_REVOLUTION)

        # Pause for 2 seconds
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting the script.")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()