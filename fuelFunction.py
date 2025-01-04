import math
import time

import numpy as np
from roadSegments import *

# car properties
CAR_WEIGHT = 1.2   # Weight of the car in tons
C0 = 5      # Base fuel consumption
k1 = 0.2    # Slope influence coefficient
k2 = 0.05   # Turn influence coefficient
# k3 = 0.01    # Road quality influence coefficient
# k4 = 0.03   #
k5 = 0.0005     # Weight influence coefficient
k6 = 0.001      # Air friction influence coefficient

A = 2.2     # Frontal area of the car in m**2
p = 1.225   # Air density (kg/m**3)
Cd = 0.3    # Air friction coefficient

a = 1     # Fuel influence coefficient
s = 10     # Fuel scaling factor
b = 1     # Speed (time) influence coefficient


def fuel_calculator_formula(speed: list, segment: tuple) -> float:
    # Calculates the fuel consumption based on the given speed and road segment
    _, _, base_speed, slope_angle, turn_angle = segment

    speed = decode(speed, segment)  # Decode the speed from the bit string
    slope = slope_angle * (1 + speed / base_speed)  # Adjust slope based on speed
    turn = math.tan(turn_angle) * (1 + speed**2 / base_speed**2)  # Adjust turn based on speed
    # road = ROAD_FRICTION_COEFFICIENT * (1 + RESISTIVITY_COEFFICIENT * speed / BASE_SPEED)
    weight = CAR_WEIGHT * speed**2 / 2  # Calculate the weight influence on fuel consumption
    air = p * A * Cd * speed**2 / 2  # Calculate air friction influence on fuel consumption

    # Return the total fuel consumption based on various factors
    return C0 + k1 * slope + k2 * turn + k5 * weight + k6 * air


def fitness(speed: list, segment: tuple) -> float:
    # Calculates the fitness of the solution based on fuel consumption and speed
    return a * s * fuel_calculator_formula(speed, segment) - b * decode(speed, segment)


BIT_LENGTH = 10  # Number of bits used for encoding the speed
POPULATION_SIZE = 100  # Size of the population in the genetic algorithm


def decode(bits: list, segment: tuple) -> float:
    # Decodes a list of bits to a speed value within the given range
    min_speed, max_speed, _, _, _ = segment
    bit_string = ''.join(map(str, bits))  # Convert the list of bits to a string
    value = int(bit_string, 2)  # Convert the bit string to an integer
    # Scale the integer value to the speed range
    return min_speed + (max_speed - min_speed) * (value / (2 ** BIT_LENGTH - 1))


def initialize_population() -> list:
    # Initializes the population by generating random individuals
    np.random.seed(int(time.time()) % 100000)  # Set a seed based on the current time
    # Generate random binary individuals
    return [np.random.randint(0, 2, BIT_LENGTH).tolist() for _ in range(POPULATION_SIZE)]

