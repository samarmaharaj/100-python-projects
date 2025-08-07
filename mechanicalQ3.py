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
point_load_value1 = get_float_input("Enter the value of the point load 1 (in kN): ")
point_load_position1 = get_float_input("Enter the position of the point load 1 (in meters): ")
point_load_value2 = get_float_input("Enter the value of the point load 2 (in kN): ")
point_load_position2 = get_float_input("Enter the position of the point load 2(in meters): ")
distributed_load_start_value = get_float_input("Enter the start value of the distributed load (in kN/m): ")
distributed_load_end_value = get_float_input("Enter the end value of the distributed load (in kN/m): ")
distributed_load_start_position = get_float_input("Enter the start position of the distributed load (in meters): ")
distributed_load_end_position = get_float_input("Enter the end position of the distributed load (in meters): ")

# Define the beam
beam = Beam(beam_length)

# Define the supports
beam.pinned_support = pinned_support
beam.rolling_support = rolling_support

distributed_load_slope = (distributed_load_end_value - distributed_load_start_value) / (distributed_load_end_position - distributed_load_start_position)
# Apply loads to the beam
beam.add_loads((
    PointLoadV(point_load_value1, point_load_position1),
    PointLoadV(point_load_value2, point_load_position2),
    DistributedLoadV(distributed_load_start_value + (x - distributed_load_start_position) * distributed_load_slope, (distributed_load_start_position, distributed_load_end_position)),
))

# Generate the plot
fig = beam.plot_beam_diagram()
fig = beam.plot_bending_moment()
fig = beam.plot_shear_force()

# Save the plot as a PDF
fig.savefig("./results.pdf")

# If you want to display the plot in the script
plt.show()
