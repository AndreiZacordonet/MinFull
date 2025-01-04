import unittest
import numpy as np
from roadSegments import SEGMENT1, SEGMENT2  # Assuming SEGMENT1 and SEGMENT2 are test cases
from fuelFunction import (
    fuel_calculator_formula,
    fitness,
    decode,
    initialize_population,
    BIT_LENGTH,
    POPULATION_SIZE,
)


class TestFuelCalculator(unittest.TestCase):

    def test_decode(self):
        # Test the decode function to ensure it correctly converts bit strings to speeds
        segment = SEGMENT1
        min_speed, max_speed, _, _, _ = segment

        # Test with a bit string representing the minimum speed
        bits = [0] * BIT_LENGTH
        self.assertAlmostEqual(decode(bits, segment), min_speed)

        # Test with a bit string representing the maximum speed
        bits = [1] * BIT_LENGTH
        self.assertAlmostEqual(decode(bits, segment), max_speed)

        # Test with a bit string representing a speed between min and max
        bits = [0] * (BIT_LENGTH - 1) + [1]
        expected = min_speed + (max_speed - min_speed) * (1 / (2 ** BIT_LENGTH - 1))
        self.assertAlmostEqual(decode(bits, segment), expected)

    def test_fuel_calculator_formula(self):
        # Test the fuel_calculator_formula function to ensure it returns a positive fuel value
        segment = SEGMENT1
        speed = [0] * BIT_LENGTH  # Speed is initially zero
        fuel = fuel_calculator_formula(speed, segment)

        # Fuel consumption should be greater than zero
        self.assertGreater(fuel, 0, "Fuel consumption should be greater than zero.")

    def test_fitness(self):
        # Test the fitness function to ensure it returns a valid float value
        segment = SEGMENT2
        speed = [1] * BIT_LENGTH  # Maximum speed (all bits set to 1)
        fit = fitness(speed, segment)

        # Fitness should be a float and should not return zero for valid inputs
        self.assertIsInstance(fit, float, "Fitness should return a float value.")
        self.assertNotEqual(fit, 0, "Fitness should not return zero for valid inputs.")

    def test_initialize_population(self):
        # Test the initialize_population function to ensure it generates the correct population size
        population = initialize_population()

        # Population size should match the defined POPULATION_SIZE
        self.assertEqual(len(population), POPULATION_SIZE, "Population size mismatch.")

        # Each individual should have the correct bit length, and all bits should be either 0 or 1
        for individual in population:
            self.assertEqual(len(individual), BIT_LENGTH, "Bit length mismatch in individual.")
            self.assertTrue(all(bit in [0, 1] for bit in individual), "Invalid bit value found.")

    def test_decode_consistency(self):
        # Test the consistency of the decode function across the population
        segment = SEGMENT1
        population = initialize_population()

        # For each individual, decode the speed and check it falls within the min and max speed range
        for individual in population:
            decoded_speed = decode(individual, segment)
            min_speed, max_speed, _, _, _ = segment

            # Decoded speed should be within the range of min_speed and max_speed
            self.assertTrue(
                min_speed <= decoded_speed <= max_speed,
                "Decoded speed out of range.",
            )


if __name__ == "__main__":
    unittest.main()
