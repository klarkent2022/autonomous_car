import time

def turn_left(motor1, motor2):
    motor1.speed = 40, 40
    motor2.speed = 40, 40
    time.sleep(1.05)
    motor1.speed = 0, 0
    motor2.speed = 0, 0
 
def turn_right(motor1, motor2):
    motor1.speed = -40, -40
    motor2.speed = -40, -40
    time.sleep(1.05)
    motor1.speed = 0, 0
    motor2.speed = 0, 0
 
def go_forward(motor1, motor2):
    motor1.speed = -50, 50
    motor2.speed = 50, -50
    time.sleep(1.90)
    motor1.speed = 0, 0
    motor2.speed = 0, 0