from fuelFunction import decode, fuel_calculator_formula
from geneticAlgorithm import genetic_algorithm

best, value = genetic_algorithm(100)

print(f"Best individual (bits): {best}")
print(f"Speed: {decode(best):.2f} km/h")
print(f"Fuen consumption (l/100km): {fuel_calculator_formula(best)}")
print(f"Fitness: {value:.4f}")
