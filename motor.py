import RPi.GPIO as GPIO
from time import sleep

number_of_turns = 5

# The pins we will use to drive the motor on the Raspberry Pi
MOTOR_PIN_ARRAY = [23,22,27,17]

# Define the stepper motor sequence
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]


# Delay between steps in seconds
step_delay = 0.0009765625 

# STEP DELAY VALUES:
# DELAY = (60/RPM) / 4096
#   1 RPM: 0.0146484375
#   2 RPM: 0.00732421875
#   5 RPM: 0.0029296875
#  10 RPM: 0.00146484375
#  15 RPM: 0.0009765625


# Steps required for a full rotation\
steps_per_revolution = 4096  

# This number will assist in outputting our sequence
motor_step_counter = 0

def set_up_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in MOTOR_PIN_ARRAY:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        print(f"Pin {pin} set as output")


def step(direction, steps):
    global motor_step_counter

    print(f"step: {direction} {steps}")
    for i in range(steps):
        for pin in range(len(MOTOR_PIN_ARRAY)):
            GPIO.output(MOTOR_PIN_ARRAY[pin], step_sequence[motor_step_counter][pin])
        if direction == True:
            motor_step_counter = (motor_step_counter + 1) % 8
        elif direction == False:
            motor_step_counter = (motor_step_counter - 1) % 8
        else:
            print("That didn't work")
        sleep(step_delay)


if __name__ == "__main__":
    try:
        set_up_pins()
        turn_counter = 0

        # Rotate the motor 360 degrees clockwise
        for num in range(number_of_turns):
            step(True, steps_per_revolution)
            turn_counter = turn_counter + 1
            print(f"Completed {turn_counter} revolution")

    except KeyboardInterrupt:
        print("Program was closed using ctrl+c")
        GPIO.cleanup()

    except Exception as e:
        print("Something went wrong.")
