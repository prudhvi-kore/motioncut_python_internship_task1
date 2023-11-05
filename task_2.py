def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def temperature_converter():
    print("Temperature Converter: Celsius to Fahrenheit and Fahrenheit to Celsius")
    
    while True:
        try:
            value = float(input("Enter a temperature value to convert: "))
            source_unit = input("Enter the source unit (Celsius or Fahrenheit): ").strip().lower()
            target_unit = input("Enter the target unit (Celsius or Fahrenheit): ").strip().lower()

            if source_unit == "celsius" and target_unit == "fahrenheit":
                result = celsius_to_fahrenheit(value)
                print(f"{value} degrees Celsius is equal to {result:.2f} degrees Fahrenheit.")
            elif source_unit == "fahrenheit" and target_unit == "celsius":
                result = fahrenheit_to_celsius(value)
                print(f"{value} degrees Fahrenheit is equal to {result:.2f} degrees Celsius.")
            else:
                print("Unsupported unit conversion. Please enter 'Celsius' or 'Fahrenheit'.")
        
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

        another_conversion = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if another_conversion != "yes":
            break

def length_converter():
    print("Length Converter: Meters to Feet and Feet to Meters")
    
    while True:
        try:
            value = float(input("Enter a value to convert: "))
            source_unit = input("Enter the source unit (meters or feet): ").strip().lower()
            target_unit = input("Enter the target unit (meters or feet): ").strip().lower()

            if source_unit == "meters" and target_unit == "feet":
                result = meters_to_feet(value)
                print(f"{value} meters is equal to {result:.2f} feet.")
            elif source_unit == "feet" and target_unit == "meters":
                result = feet_to_meters(value)
                print(f"{value} feet is equal to {result:.2f} meters.")
            else:
                print("Unsupported unit conversion. Please enter 'meters' or 'feet'.")
        
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

        another_conversion = input("Do you want to convert another value? (yes/no): ").strip().lower()
        if another_conversion != "yes":
            break

def weight_converter():
    print("Weight Converter: Kilograms to Pounds and Pounds to Kilograms")
    
    while True:
        try:
            value = float(input("Enter a weight value to convert: "))
            source_unit = input("Enter the source unit (kilograms or pounds): ").strip().lower()
            target_unit = input("Enter the target unit (kilograms or pounds): ").strip().lower()

            if source_unit == "kilograms" and target_unit == "pounds":
                result = kilograms_to_pounds(value)
                print(f"{value} kilograms is equal to {result:.2f} pounds.")
            elif source_unit == "pounds" and target_unit == "kilograms":
                result = pounds_to_kilograms(value)
                print(f"{value} pounds is equal to {result:.2f} kilograms.")
            else:
                print("Unsupported unit conversion. Please enter 'kilograms' or 'pounds'.")
        
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

        another_conversion = input("Do you want to convert another weight? (yes/no): ").strip().lower()
        if another_conversion != "yes":
            break

if __name__ == "__main__":
    while True:
        print("Unit Converter Menu:")
        print("1. Temperature Converter")
        print("2. Length Converter")
        print("3. Weight Converter")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            temperature_converter()
        elif choice == '2':
            length_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
