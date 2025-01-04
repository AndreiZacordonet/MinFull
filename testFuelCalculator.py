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
        segment = SEGMENT1
        min_speed, max_speed, _, _, _ = segment
        bits = [0] * BIT_LENGTH
        self.assertAlmostEqual(decode(bits, segment), min_speed)

        bits = [1] * BIT_LENGTH
        self.assertAlmostEqual(decode(bits, segment), max_speed)

        bits = [0] * (BIT_LENGTH - 1) + [1]
        expected = min_speed + (max_speed - min_speed) * (1 / (2 ** BIT_LENGTH - 1))

        self.assertAlmostEqual(decode(bits, segment), expected)

    def test_fuel_calculator_formula(self):
        segment = SEGMENT1
        speed = [0] * BIT_LENGTH
        fuel = fuel_calculator_formula(speed, segment)

        self.assertGreater(fuel, 0, "Fuel consumption should be greater than zero.")

    def test_fitness(self):
        segment = SEGMENT2
        speed = [1] * BIT_LENGTH
        fit = fitness(speed, segment)

        self.assertIsInstance(fit, float, "Fitness should return a float value.")
        self.assertNotEqual(fit, 0, "Fitness should not return zero for valid inputs.")

    def test_initialize_population(self):
        population = initialize_population()

        self.assertEqual(len(population), POPULATION_SIZE, "Population size mismatch.")

        for individual in population:
            self.assertEqual(len(individual), BIT_LENGTH, "Bit length mismatch in individual.")
            self.assertTrue(all(bit in [0, 1] for bit in individual), "Invalid bit value found.")

    def test_decode_consistency(self):
        segment = SEGMENT1
        population = initialize_population()

        for individual in population:
            decoded_speed = decode(individual, segment)
            min_speed, max_speed, _, _, _ = segment

            self.assertTrue(
                min_speed <= decoded_speed <= max_speed,
                "Decoded speed out of range.",
            )


if __name__ == "__main__":
    unittest.main()
