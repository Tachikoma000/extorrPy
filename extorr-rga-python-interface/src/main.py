from extorr import ExtorrRGA

# Create an instance of the ExtorrRGA class
rga = ExtorrRGA()

# Set the mass range for the scan
rga.set_mass_range(1, 100)

# Start the scan
rga.start_scan()

# Wait for the scan to complete
while not rga.is_scan_complete():
    pass

# Get the acquired data
mass_to_charge_ratios, partial_pressures = rga.get_data()

# Print the acquired data
for mass, pressure in zip(mass_to_charge_ratios, partial_pressures):
    print(f"Mass-to-charge ratio: {mass} amu, Partial pressure: {pressure} Torr")
