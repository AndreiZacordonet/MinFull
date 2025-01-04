from random import uniform, random, sample, randint

from fuelFunction import BIT_LENGTH, fuel_calculator_formula, initialize_population, POPULATION_SIZE

EPSILON = 10**-4

NUM_GENERATIONS = 100000
CROSSOVER_RATE = 0.9
MUTATION_RATE = 0.02
VARIABLE_RANGE = (-5.12, 5.12)


def tournament_selection(population: list) -> list:
    return min(sample(population, 2), key=fuel_calculator_formula)


def crossover(parent1: list, parent2: list) -> list:
    if random() < CROSSOVER_RATE:
        point = randint(1, BIT_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return [child1, child2]
    return [parent1, parent2]


def mutate(individual: list) -> list:
    return [1 - bit if random() < MUTATION_RATE else bit for bit in individual]


def genetic_algorithm(number_of_generations: int) -> tuple:
    population = initialize_population()
    print(population)
    best_individual = min(population, key=fuel_calculator_formula)

    for generation in range(number_of_generations):
        new_population = [best_individual]  # Elitism

        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            children = crossover(parent1, parent2)
            new_population.extend([mutate(child) for child in children])

        population = new_population[:POPULATION_SIZE]
        best_individual = min(population, key=fuel_calculator_formula)

        if fuel_calculator_formula(best_individual) < EPSILON:
            break

    return best_individual, fuel_calculator_formula(best_individual)

