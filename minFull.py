from fuelFunction import decode, fuel_calculator_formula
from geneticAlgorithm import genetic_algorithm
from roadSegments import SEGMENTS

best, value = genetic_algorithm(100, SEGMENTS[0])

print(f"Best individual (bits): {best}")
print(f"Speed: {decode(best, SEGMENTS[0]):.2f} km/h")
print(f"Fuen consumption (l/100km): {fuel_calculator_formula(best, SEGMENTS[0])}")
print(f"Fitness: {value:.4f}")

# TODO: plotting the results
