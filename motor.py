from gpiozero import OutputDevice
from time import sleep

# Define GPIO pins connected to the motor driver IN1 - IN4
IN1 = OutputDevice(17)
IN2 = OutputDevice(18)
IN3 = OutputDevice(27)
IN4 = OutputDevice(22)

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
step_delay = 0.005  # Delay between steps in seconds
steps_per_revolution = 4096  # Steps required for a full rotation

def step(direction, steps):
    for _ in range(steps):
        for pin in range(4):
            IN1.value = step_sequence[direction][0]
            IN2.value = step_sequence[direction][1]
            IN3.value = step_sequence[direction][2]
            IN4.value = step_sequence[direction][3]
            sleep(step_delay)

# Rotate the motor 360 degrees clockwise
step(1, steps_per_revolution)

# Rotate the motor 360 degrees counterclockwise
step(-1, steps_per_revolution)

# Cleanup GPIO
IN1.close()
IN2.close()
IN3.close()
IN4.close()