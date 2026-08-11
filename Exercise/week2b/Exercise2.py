# This function converts the temperature from Fahrenheit to Celsius.
def to_celsius(temperature):
    return (temperature - 32) * 5 / 9

# This function converts the temperature from Celsius to Fahrenheit.
def to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32

# This class converts the temperature from Fahrenheit to Celsius and vice versa.
#  The user can input the temperature with a prefix of 'C' or 'F' to indicate the unit of the temperature.
#  The program will then convert the temperature to the other unit and display the result.
class temperature_converter:

    def input_temperature(self):
        temperature = input(
            "Enter the temperature: (e.g., F10 or C10) "
        ).strip()

        if len(temperature) < 2:
            print("Invalid input. Please enter the temperature with the correct 'C' or F' prefix.")
            return

        prefix = temperature[0]
        value = temperature[1:]

        if prefix not in ("C", "F"):
            print("Invalid input. Please enter the temperature with the correct 'C' or F' prefix.")
            return

        try:
            value = float(value)
        except ValueError:
            print("Invalid input. Please enter the temperature with the correct 'C' or F' prefix.")
            return

        if prefix == "F":
            converted = to_celsius(value)
            print(
                f"F{value:g} degrees Fahrenheit is converted to "
                f"{converted:.2f} degrees Celsius"
            )

        elif prefix == "C":
            converted = to_fahrenheit(value)
            print(
                f"C{value:g} degrees Celsius is converted to "
                f"{converted:.2f} degrees Fahrenheit"
            )


if __name__ == "__main__":
    temp_converter = temperature_converter()
    temp_converter.input_temperature()