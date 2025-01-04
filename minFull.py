from fuelFunction import decode, fuel_calculator_formula
from geneticAlgorithm import genetic_algorithm
from roadSegments import SEGMENTS

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Initialize lists to store results for each road segment
segment_labels = []  # Labels for each road segment
speeds = []  # Best speeds determined by the genetic algorithm
fuel_consumptions = []  # Fuel consumption corresponding to the best speeds
fitness_values = []  # Fitness values for the best solutions

i = 0
for segment in SEGMENTS:
    i += 1
    # Run the genetic algorithm for the current segment
    best, value = genetic_algorithm(100, segment)

    # Decode the best individual to get the corresponding speed
    speed = decode(best, segment)
    # Calculate the fuel consumption for the decoded speed
    fuel = fuel_calculator_formula(best, segment)

    # Append results to respective lists
    segment_labels.append(f"Segment {i}")
    speeds.append(speed)
    fuel_consumptions.append(fuel)
    fitness_values.append(value)

    # Print detailed results for the current segment
    print(f"\n-----------------SEGMENT {i} {segment}-----------------")
    print(f"Best individual (bits): {best}")
    print(f"Speed: {speed:.2f} km/h")
    print(f"Fuel consumption (l/100km): {fuel}")
    print(f"Fitness: {value:.4f}")

# Plotting the results using Matplotlib
fig, ax1 = plt.subplots(figsize=(12, 8))  # Create a figure with primary axis (ax1)

bar_width = 0.4  # Width of the bars for speed
x_positions = range(len(segment_labels))  # X-axis positions for bars

# Plot the speeds as a bar chart on the primary axis
ax1.bar(x_positions, speeds, color='skyblue', label='Speed (km/h)', width=bar_width, align='center')
ax1.set_ylabel('Speed (km/h)', fontsize=12)  # Label for the primary Y-axis
ax1.set_xlabel('Road Segments', fontsize=12)  # Label for the X-axis

# Set X-axis ticks with segment labels
plt.xticks(x_positions, segment_labels, rotation=45, ha='right', fontsize=10)

# Create a secondary Y-axis to plot fuel consumption
ax2 = ax1.twinx()
ax2.plot(x_positions, fuel_consumptions, color='orange', marker='o', label='Fuel (l/100 km)', linewidth=2)
ax2.set_ylabel('Fuel Consumption (l/100 km)', fontsize=12)  # Label for the secondary Y-axis

# Annotate fitness values on the bar chart
for i, fitness in enumerate(fitness_values):
    ax1.text(i, speeds[i] + 1, f"{fitness:.2f}", ha='center', va='bottom', fontsize=10, color='black')

# Add legends for both axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Add a title and grid for better visualization
plt.title('Genetic Algorithm Results for Different Road Segments', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
