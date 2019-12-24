import numpy as np

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255,0)
blue = (0, 0, 255)
yellow = ( 255,200,0)
purple = (128,138,135)

def get_angle_diff(yaw1, yaw2):
    diff = yaw2 - yaw1
    if diff < -180:
        diff = diff + 360
    elif diff > 180:
        diff = diff - 360
    return diff

def get_yaw(x1, y1, x2, y2):
    return float(int(270 - np.math.atan2(y2-y1, x2-x1) * 180 / 3.1415926)%360)


def get_distance(x1, y1, x2, y2):
    return np.power((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2), 0.5)