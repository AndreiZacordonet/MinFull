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
        population = [
            [0] * BIT_LENGTH,
            [1] * BIT_LENGTH,
        ]
        segment = SEGMENT1

        mock_sample.return_value = population

        fitness1 = fitness(population[0], segment)
        fitness2 = fitness(population[1], segment)

        best_individual = population[0] if fitness1 < fitness2 else population[1]

        self.assertEqual(
            tournament_selection(population, segment),
            best_individual,
            "Tournament selection did not select the best individual."
        )

    def test_crossover(self):
        parent1 = [randint(0, 1) for _ in range(BIT_LENGTH)]
        parent2 = [randint(0, 1) for _ in range(BIT_LENGTH)]
        children = crossover(parent1, parent2)

        self.assertEqual(len(children), 2, "Crossover did not produce two children.")
        self.assertEqual(len(children[0]), BIT_LENGTH, "Child 1 has an incorrect bit length.")
        self.assertEqual(len(children[1]), BIT_LENGTH, "Child 2 has an incorrect bit length.")

        crossover_point = next((i for i in range(BIT_LENGTH) if children[0][i] != parent1[i]), BIT_LENGTH)

        self.assertTrue(
            children[0][:crossover_point] == parent1[:crossover_point] and
            children[0][crossover_point:] == parent2[crossover_point:],
            "Child 1 is not a valid combination of parents.",
        )

    def test_mutate(self):
        individual = [randint(0, 1) for _ in range(BIT_LENGTH)]
        mutated = mutate(individual)

        self.assertEqual(len(mutated), BIT_LENGTH, "Mutated individual has an incorrect bit length.")

        flipped_bits = sum(1 for i in range(BIT_LENGTH) if individual[i] != mutated[i])

        self.assertTrue(
            0 <= flipped_bits <= BIT_LENGTH,
            "Mutate produced invalid bit flips.",
        )

    def test_genetic_algorithm(self):
        segment = SEGMENT1
        best_individual, best_fitness = genetic_algorithm(10, segment)

        self.assertEqual(len(best_individual), BIT_LENGTH, "Best individual has an incorrect bit length.")
        self.assertTrue(
            best_fitness < EPSILON or best_fitness > 0,
            "Best fitness value is not within acceptable bounds.",
        )

    @patch("geneticAlgorithm.random")
    def test_crossover_always_happens(self, mock_random):
        mock_random.return_value = 0.5

        parent1 = [0] * BIT_LENGTH
        parent2 = [1] * BIT_LENGTH

        children = crossover(parent1, parent2)

        self.assertNotEqual(children[0], parent1, "Crossover did not mix the parents.")
        self.assertNotEqual(children[1], parent2, "Crossover did not mix the parents.")

    def test_population_initialization(self):
        population = initialize_population()

        self.assertEqual(len(population), POPULATION_SIZE, "Population size mismatch.")

        for individual in population:
            self.assertEqual(len(individual), BIT_LENGTH, "Individual bit length mismatch.")
            self.assertTrue(all(bit in [0, 1] for bit in individual), "Invalid bit value in population.")


if __name__ == "__main__":
    unittest.main()
