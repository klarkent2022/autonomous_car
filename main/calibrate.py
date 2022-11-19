import time

def step_right(motor1, motor2):
    motor1.speed = -50, -50
    motor2.speed = -50, -50
    time.sleep(0.1)
    motor1.speed = 0, 0
    motor2.speed = 0, 0

def step_left(motor1, motor2):
    motor1.speed = 50, 50
    motor2.speed = 50, 50
    time.sleep(0.1)
    motor1.speed = 0, 0
    motor2.speed = 0, 0

def calibration(ir1, ir2, motor1, motor2):
    # ir1 - right
    for i in range(10):
        ir1_reading = ir1.proximity
        ir2_reading = ir2.proximity

    if (ir1_reading in range(40)) and (ir2_reading in range(80, 100)):
        step_right(motor1, motor2)
    elif (ir1_reading in range(80, 100)) and (ir2_reading in range(40)):
        step_left(motor1, motor2)


        

