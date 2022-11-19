import modi
import time
from calibrate import calibration
from utils import *

'''
    This is the main driver function of the autonomous car

    Author: Sanjar, Uzair, Abish 
'''
 
 
def move(motor1, motor2, path, orientation = "s"):
    for i in path[:len(path)]:
        if i == "down":
            if orientation == "e":
                turn_right(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "w":
                turn_left(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "n":
                turn_left(motor1, motor2)
                turn_left(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "s":
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            orientation = 's'
        elif i == "up":
            if orientation == "e":
                turn_left(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "w":
                turn_right(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "n":
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "s":
                turn_left(motor1, motor2)
                turn_left(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            orientation = 'n'
        elif i == "right":
            if orientation == "e":
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "w":
                turn_right(motor1, motor2)
                turn_right(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "n":
                turn_right(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "s":
                turn_left(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            orientation = 'e'
        elif i == "left":
            if orientation == "e":
                turn_left(motor1, motor2)
                turn_right(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "w":
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "n":
                turn_left(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            elif orientation == "s":
                turn_right(motor1, motor2)
                calibration(ir1, ir2, motor1, motor2)
                go_forward(motor1, motor2)
            orientation = 'w'
 
 
if __name__ == "__main__":
    path = ['down', 'down', 'right', 'right', 
    'down', 'down', 'right', 'down', 'down', 'right', 'right', 'down', 'right', 'right']
    bundle = modi.MODI()    
    ir1 = bundle.irs[0]
    ir2 = bundle.irs[1]
    motor1 = bundle.motors[0]
    motor2 = bundle.motors[1]
    time.sleep(2)
    move(motor1, motor2, path)