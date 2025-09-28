FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    while True:
        try: 
            temperature_to_convert = float(input("Enter the temperature to convert: "))
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if temperature_unit not in ("C","F"):
            print("Invalid temperature unit. Please enter 'C' or 'F'")
        elif temperature_unit == "C":
            converted_temperature = convert_to_fahrenheit(temperature_to_convert)
            print(f"{temperature_to_convert}C is {converted_temperature}F")
        elif temperature_unit == "F":
            converted_temperature = convert_to_celsius(temperature_to_convert)
            print(f"{temperature_to_convert}F is {converted_temperature}C")
            
if __name__ == "__main__": 
    main()