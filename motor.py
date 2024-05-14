import RPi.GPIO as GPIO
from time import sleep

# The pins we will use to drive the motor on the Raspberry Pi
MOTOR_PIN_ARRAY = [17,18,27,22]

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

# Define the motor speed and number of steps for a full rotation
step_delay = 0.00293  # Delay between steps in seconds (0.00293 will result in 5 RPM)
#step_delay = 1

steps_per_revolution = 4096  # Steps required for a full rotation\

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
            print(step_sequence[motor_step_counter][pin])
        if direction == True:
            motor_step_counter = (motor_step_counter + 1) % 8
        elif direction == False:
            motor_step_counter = (motor_step_counter - 1) % 8
            print(f"*****{motor_step_counter}*****")
        else:
            print("That didn't work")
        sleep(step_delay)


if __name__ == "__main__":
    try:
        set_up_pins()
        turn_counter = 0

        # Rotate the motor 360 degrees clockwise
        for num in range(5):
            step(False, steps_per_revolution)
            turn_counter = turn_counter + 1
            print(f"Completed {turn_counter} revolution")

    except KeyboardInterrupt:
        print("Program was closed using ctrl+c")
        GPIO.cleanup()

    except Exception as e:
        print("Something went wrong.")
