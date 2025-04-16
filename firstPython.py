# Simulate a temperature sensor function
def read_temperature_sensor():
    """Simulate reading temperature from an IoT device."""
    return 25.0  # A fixed temperature for simplicity

# Check if the temperature is within a safe range
def is_temperature_safe(temp):
    """Check if the temperature is within the safe range."""
    return -10.0 <= temp <= 40.0

# Main script to test the system
temperature = read_temperature_sensor()
print(f"Temperature reading: {temperature}°C")

if is_temperature_safe(temperature):
    print("The temperature is within the safe range.")
else:
    print("Warning: The temperature is outside the safe range!")
