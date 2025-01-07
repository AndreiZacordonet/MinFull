from random import random, sample, randint

from fuelFunction import BIT_LENGTH, fitness, initialize_population, POPULATION_SIZE


NUM_GENERATIONS = 1000000  # Maximum number of generations
CROSSOVER_RATE = 0.9  # Probability of crossover occurring
MUTATION_RATE = 0.02  # Probability of mutation occurring
VARIABLE_RANGE = (-5.12, 5.12)  # The range for the variable values


def tournament_selection(population: list, segment: tuple) -> list:
    # Selects two individuals randomly and returns the one with the best fitness
    return min(sample(population, 2), key=lambda x: fitness(x, segment))


def crossover(parent1: list, parent2: list) -> list:
    # Performs crossover between two parents to produce two children
    if random() < CROSSOVER_RATE:
        point = randint(1, BIT_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return [child1, child2]
    return [parent1, parent2]


def mutate(individual: list) -> list:
    # Applies mutation to an individual by flipping bits based on mutation rate
    return [1 - bit if random() < MUTATION_RATE else bit for bit in individual]


def genetic_algorithm(number_of_generations: int, segment: tuple) -> tuple:
    # Main function implementing the genetic algorithm
    population = initialize_population()  # Initialize population
    # print(population)  # Display the initial population
    best_individual = min(population, key=lambda x: fitness(x, segment))  # Select the best individual based on fitness

    for generation in range(number_of_generations):
        new_population = [best_individual]  # Elitism: retain the best individual

        while len(new_population) < POPULATION_SIZE:  # Fill the rest of the population
            parent1 = tournament_selection(population, segment)  # Select parent 1
            parent2 = tournament_selection(population, segment)  # Select parent 2
            children = crossover(parent1, parent2)  # Perform crossover to get children
            new_population.extend([mutate(child) for child in children])  # Apply mutation to children

        population = new_population[:POPULATION_SIZE]  # Set new population
        best_individual = min(population, key=lambda x: fitness(x, segment))  # Update the best individual

    return best_individual, fitness(best_individual, segment)  # Return the best solution and its fitness
