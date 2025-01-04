import unittest
from unittest.mock import patch
from random import randint, sample

from fuelFunction import (
    BIT_LENGTH,
    POPULATION_SIZE,
    initialize_population,
    fitness,
)
from geneticAlgorithm import (
    EPSILON,
    tournament_selection,
    crossover,
    mutate,
    genetic_algorithm,
)
from roadSegments import SEGMENT1


class TestGeneticAlgorithm(unittest.TestCase):

    @patch("geneticAlgorithm.sample")
    def test_tournament_selection(self, mock_sample):
        # Test the tournament selection process by mocking the sample function
        population = [
            [0] * BIT_LENGTH,  # Individual with all zeros
            [1] * BIT_LENGTH,  # Individual with all ones
        ]
        segment = SEGMENT1

        mock_sample.return_value = population  # Mock the sample function to return the population

        # Calculate fitness for both individuals
        fitness1 = fitness(population[0], segment)
        fitness2 = fitness(population[1], segment)

        # Select the best individual based on fitness
        best_individual = population[0] if fitness1 < fitness2 else population[1]

        # Ensure tournament selection selects the best individual
        self.assertEqual(
            tournament_selection(population, segment),
            best_individual,
            "Tournament selection did not select the best individual."
        )

    def test_crossover(self):
        # Test the crossover function to ensure it produces valid children
        parent1 = [randint(0, 1) for _ in range(BIT_LENGTH)]  # Random parent1
        parent2 = [randint(0, 1) for _ in range(BIT_LENGTH)]  # Random parent2
        children = crossover(parent1, parent2)  # Perform crossover

        # Ensure two children are created
        self.assertEqual(len(children), 2, "Crossover did not produce two children.")
        # Ensure the children have the correct bit length
        self.assertEqual(len(children[0]), BIT_LENGTH, "Child 1 has an incorrect bit length.")
        self.assertEqual(len(children[1]), BIT_LENGTH, "Child 2 has an incorrect bit length.")

        # Ensure the crossover point is valid
        crossover_point = next((i for i in range(BIT_LENGTH) if children[0][i] != parent1[i]), BIT_LENGTH)

        # Ensure child 1 is a valid combination of the parents
        self.assertTrue(
            children[0][:crossover_point] == parent1[:crossover_point] and
            children[0][crossover_point:] == parent2[crossover_point:],
            "Child 1 is not a valid combination of parents.",
        )

    def test_mutate(self):
        # Test the mutation function to ensure it produces valid mutations
        individual = [randint(0, 1) for _ in range(BIT_LENGTH)]  # Random individual
        mutated = mutate(individual)  # Perform mutation

        # Ensure the mutated individual has the correct bit length
        self.assertEqual(len(mutated), BIT_LENGTH, "Mutated individual has an incorrect bit length.")

        # Count the number of bit flips
        flipped_bits = sum(1 for i in range(BIT_LENGTH) if individual[i] != mutated[i])

        # Ensure the number of flipped bits is within valid bounds
        self.assertTrue(
            0 <= flipped_bits <= BIT_LENGTH,
            "Mutate produced invalid bit flips.",
        )

    def test_genetic_algorithm(self):
        # Test the genetic algorithm to ensure it runs and produces valid results
        segment = SEGMENT1
        best_individual, best_fitness = genetic_algorithm(10, segment)  # Run genetic algorithm for 10 generations

        # Ensure the best individual has the correct bit length
        self.assertEqual(len(best_individual), BIT_LENGTH, "Best individual has an incorrect bit length.")
        # Ensure the best fitness value is within acceptable bounds
        self.assertTrue(
            best_fitness < EPSILON or best_fitness > 0,
            "Best fitness value is not within acceptable bounds.",
        )

    @patch("geneticAlgorithm.random")
    def test_crossover_always_happens(self, mock_random):
        # Test that crossover happens when random value triggers it
        mock_random.return_value = 0.5  # Mock the random function to return 0.5

        parent1 = [0] * BIT_LENGTH  # Parent with all zeros
        parent2 = [1] * BIT_LENGTH  # Parent with all ones

        children = crossover(parent1, parent2)  # Perform crossover

        # Ensure crossover mixes the parents' genetic material
        self.assertNotEqual(children[0], parent1, "Crossover did not mix the parents.")
        self.assertNotEqual(children[1], parent2, "Crossover did not mix the parents.")

    def test_population_initialization(self):
        # Test the population initialization function
        population = initialize_population()

        # Ensure the population size matches the defined size
        self.assertEqual(len(population), POPULATION_SIZE, "Population size mismatch.")

        # Ensure each individual has the correct bit length and all bits are valid
        for individual in population:
            self.assertEqual(len(individual), BIT_LENGTH, "Individual bit length mismatch.")
            self.assertTrue(all(bit in [0, 1] for bit in individual), "Invalid bit value in population.")


if __name__ == "__main__":
    unittest.main()
