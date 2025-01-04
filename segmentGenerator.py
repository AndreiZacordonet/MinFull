# NOT USED ANYMORE

import random

def generate_road_segments(num_segments, file_name):

    with open(file_name, 'w') as file:
        for _ in range(num_segments):
            min_speed = round(random.uniform(30, 50), 2)  # Min speed (30-50 km/h)
            max_speed = round(random.uniform(50, 130), 2)  # Max speed (50-130 km/h)
            base_speed = round(random.uniform(min_speed, max_speed), 2)  # Base speed between min and max
            slope_angle = round(random.uniform(-15, 15), 2)  # Slope angle (-15 to 15 degrees)
            turn_angle = round(random.uniform(0, 180), 2)  # Curve angle (0 to 180 degrees)

            segment = [
                min_speed,
                max_speed,
                base_speed,
                slope_angle,
                turn_angle,
            ]
            file.write(",".join(map(str, segment)) + "\n")

# Example usage
num_segments = 100
file_name = "road_segments.txt"
generate_road_segments(num_segments, file_name)
print(f"Road segments written to {file_name}")
