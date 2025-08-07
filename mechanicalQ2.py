# Import required libraries
from beambending import Beam, DistributedLoadV, PointLoadV, x
import matplotlib.pyplot as plt

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer value.")

# Get user inputs
beam_length = get_float_input("Enter the length of the beam (in meters): ")
pinned_support = get_float_input("Enter the position of the pinned support (in meters): ")
rolling_support = get_float_input("Enter the position of the rolling support (in meters): ")

# Define the beam
beam = Beam(beam_length)

# Define the supports
beam.pinned_support = pinned_support
beam.rolling_support = rolling_support

# Get point loads
point_loads = []
num_point_loads = get_int_input("Enter the number of point loads: ")
for i in range(num_point_loads):
    point_load_value = get_float_input(f"Enter the value of point load {i+1} (in kN): ")
    point_load_position = get_float_input(f"Enter the position of point load {i+1} (in meters): ")
    point_loads.append(PointLoadV(point_load_value, point_load_position))

# Get distributed loads
distributed_loads = []
num_distributed_loads = get_int_input("Enter the number of distributed loads: ")
for i in range(num_distributed_loads):
    distributed_load_start_value = get_float_input(f"Enter the start value of distributed load {i+1} (in kN/m): ")
    distributed_load_end_value = get_float_input(f"Enter the end value of distributed load {i+1} (in kN/m): ")
    distributed_load_start_position = get_float_input(f"Enter the start position of distributed load {i+1} (in meters): ")
    distributed_load_end_position = get_float_input(f"Enter the end position of distributed load {i+1} (in meters): ")
    distributed_load_slope = (distributed_load_end_value - distributed_load_start_value) / (distributed_load_end_position - distributed_load_start_position)
    distributed_loads.append(DistributedLoadV(distributed_load_start_value + (x - distributed_load_start_position) * distributed_load_slope, (distributed_load_start_position, distributed_load_end_position)))

# Apply point loads to the beam
for load in point_loads:
    beam.add_loads((load,))

# Apply distributed loads to the beam
for load in distributed_loads:
    beam.add_loads((load,))

# Generate the plot
fig = beam.plot_beam_diagram()
fig = beam.plot_bending_moment()
fig = beam.plot_shear_force()

# Save the plot as a PDF
fig.savefig("./results.pdf")

# If you want to display the plot in the script
plt.show()
