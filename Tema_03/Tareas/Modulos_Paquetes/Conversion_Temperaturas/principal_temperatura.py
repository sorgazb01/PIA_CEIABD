import temperatura

def main():
    celsius = float(input("Introduce una temperatura en Celsius: "))

    print(f"{celsius}°C = {temperatura.celsius_a_fahrenheit(celsius):.2f}°F")
    print(f"{celsius}°C = {temperatura.celsius_a_kelvin(celsius):.2f}K")

main()