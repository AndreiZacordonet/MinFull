import math
import time

import numpy as np
from roadSegments import *

# car properties
CAR_WEIGHT = 1.2   # tons
C0 = 5      # base fuel consumption
k1 = 0.2    # slope influence coefficient
k2 = 0.05   # turn influence coefficient
# k3 = 0.01    # road quality influence coefficient
# k4 = 0.03   #
k5 = 0.0005     # weight influence coefficient
k6 = 0.001      # air friction influence coefficient

A = 2.2     # m**2 frontal area
p = 1.225   # air density
Cd = 0.3    # air friction coefficient

MIN_SPEED, MAX_SPEED, BASE_SPEED, SLOPE_ANGLE, TURN_ANGLE = SEGMENT4


a = 1     # fuel influence coefficient
s = 10     # fuels scaling factor
b = 1     # speed(time) influence coefficient


def fuel_calculator_formula(speed: list) -> float:
    speed = decode(speed)
    slope = SLOPE_ANGLE * (1 + speed / BASE_SPEED)
    turn = math.tan(TURN_ANGLE) * (1 + speed**2 / BASE_SPEED**2)
    # road = ROAD_FRICTION_COEFFICIENT * (1 + RESISTIVITY_COEFFICIENT * speed / BASE_SPEED)
    weight = CAR_WEIGHT * speed**2 / 2
    air = p * A * Cd * speed**2 / 2

    return C0 + k1 * slope + k2 * turn + k5 * weight + k6 * air


def fitness(speed: list) -> float:
    return a * s * fuel_calculator_formula(speed) - b * decode(speed)


BIT_LENGTH = 10
POPULATION_SIZE = 100


def decode(bits: list) -> float:
    bit_string = ''.join(map(str, bits))
    value = int(bit_string, 2)
    return MIN_SPEED + (MAX_SPEED - MIN_SPEED) * (value / (2**BIT_LENGTH - 1))


def initialize_population() -> list:
    np.random.seed(int(time.time()) % 100000)
    return [np.random.randint(0, 2, BIT_LENGTH).tolist() for _ in range(POPULATION_SIZE)]
