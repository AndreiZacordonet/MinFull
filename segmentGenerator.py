import random

def generate_road_segments(num_segments, file_name):

    with open(file_name, 'w') as file:
        for _ in range(num_segments):
            min_speed = round(random.uniform(10, 20), 2)  # Min speed (10-20 m/s)
            max_speed = round(random.uniform(21, 40), 2)  # Max speed (21-40 m/s)
            base_speed = round(random.uniform(min_speed, max_speed), 2)  # Base speed between min and max
            slope_angle = round(random.uniform(-10, 10), 2)  # Slope angle (-10 to 10 degrees)
            curve_angle = round(random.uniform(0, 90), 2)  # Curve angle (0 to 90 degrees)
            friction_coefficient = round(random.uniform(0.01, 0.05), 3)  # Road friction coefficient (0.01 to 0.05)
            resistivity_coefficient = round(random.uniform(0.001, 0.01), 4)  # Resistivity coefficient (0.001 to 0.01)

            segment = [
                min_speed,
                max_speed,
                base_speed,
                slope_angle,
                curve_angle,
                friction_coefficient,
                resistivity_coefficient
            ]
            file.write(",".join(map(str, segment)) + "\n")

# Example usage
num_segments = 5  # Change this value to generate more or fewer segments
file_name = "road_segments.txt"  # File to write the segments
generate_road_segments(num_segments, file_name)
print(f"Road segments written to {file_name}")
