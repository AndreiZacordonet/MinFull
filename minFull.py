from fuelFunction import decode
from utils import genetic_algorithm

best, value = genetic_algorithm(100)

print(f"Best individual (bits): {best}")
print(f"Speed: {decode(best):.2f} km/h")
print(f"Fuel consumption fitness: {value:.4f}")
