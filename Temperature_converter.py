def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def temperature_converter():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == 2:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    else:
        print("Invalid choice.")

temperature_converter()
