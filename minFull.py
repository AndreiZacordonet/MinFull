from fuelFunction import decode, fuel_calculator_formula
from geneticAlgorithm import genetic_algorithm
from roadSegments import SEGMENTS

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


segment_labels = []
speeds = []
fuel_consumptions = []
fitness_values = []

i = 0
for segment in SEGMENTS:
    i += 1
    best, value = genetic_algorithm(100, segment)

    speed = decode(best, segment)
    fuel = fuel_calculator_formula(best, segment)

    segment_labels.append(f"Segment {i}")
    speeds.append(speed)
    fuel_consumptions.append(fuel)
    fitness_values.append(value)

    print(f"\n-----------------SEGMENT {i} {segment}-----------------")
    print(f"Best individual (bits): {best}")
    print(f"Speed: {speed:.2f} km/h")
    print(f"Fuel consumption (l/100km): {fuel}")
    print(f"Fitness: {value:.4f}")

# TODO: plotting the results
fig, ax1 = plt.subplots(figsize=(12, 8))


bar_width = 0.4
x_positions = range(len(segment_labels))
ax1.bar(x_positions, speeds, color='skyblue', label='Speed (km/h)', width=bar_width, align='center')
ax1.set_ylabel('Speed (km/h)', fontsize=12)
ax1.set_xlabel('Road Segments', fontsize=12)


plt.xticks(x_positions, segment_labels, rotation=45, ha='right', fontsize=10)


ax2 = ax1.twinx()
ax2.plot(x_positions, fuel_consumptions, color='orange', marker='o', label='Fuel (l/100 km)', linewidth=2)
ax2.set_ylabel('Fuel Consumption (l/100 km)', fontsize=12)


for i, fitness in enumerate(fitness_values):
    ax1.text(i, speeds[i] + 1, f"{fitness:.2f}", ha='center', va='bottom', fontsize=10, color='black')


ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Genetic Algorithm Results for Different Road Segments', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.tight_layout()


plt.show()
