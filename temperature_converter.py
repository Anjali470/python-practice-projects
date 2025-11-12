def celsius_to_fahrenheit(temp):
    return ((temp * 9) / 5) + 32

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9

def celsius_to_kelvin(temp):
    return temp + 273.15

def kelvin_to_celsius(temp):
    return temp - 273.15

def fahrenheit_to_kelvin(temp):
    return celsius_to_kelvin(fahrenheit_to_celsius(temp))

def kelvin_to_fahrenheit(temp):
    return celsius_to_fahrenheit(kelvin_to_celsius(temp))

def main():

    print("1. celsius to fahrenheit\n2. fahrenheit to celsius\n3. celsius to kelvin\n4. kelvin to celsius\n5. fahrenheit to kelvin\n6. kelvin to fahrenheit")

    choice = int(input("Select your conversion: "))

    if choice not in (1,2,3,4,5,6):
        print("Invalid choice")
        return
    temperature = float(input("Enter your temperature: "))

    if choice == 1:
        result = celsius_to_fahrenheit(temperature)
        print(f"Temperature in Fahrenheit: {result:.2f}")
    elif choice == 2:
        result = fahrenheit_to_celsius(temperature)
        print(f"Temperature in Celsius: {result:.2f}")
    elif choice == 3:
        result = celsius_to_kelvin(temperature)
        print(f"Temperature in Kelvin: {result:.2f}")
    elif choice == 4:
        result = kelvin_to_celsius(temperature)
        print(f"Temperature in Celsius: {result:.2f}")
    elif choice == 5:
        result = fahrenheit_to_kelvin(temperature)
        print(f"Temperature in Kelvin: {result:.2f}")
    elif choice == 6:
        result = kelvin_to_fahrenheit(temperature)
        print(f"Temperature in Fahrenheit: {result:.2f}")

    pass

if __name__ == "__main__":
    main()
