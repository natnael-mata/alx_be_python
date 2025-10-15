# tepmrature 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit): 
     return ((fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius):
    return ((celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32)

def main():
    temperature = input("Enter the temperature to convert: ")

    try:
        temperature = float(temperature)
    except ValueError:
        print("Invalid Input Value")
        return 
    choise = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if choise == 'F':
        print(f"{temperature} °F is {convert_to_celsius(temperature)} °C")
    elif choise == 'C':
        print(f"{temperature} °C is {convert_to_fahrenheit(temperature)} °F")
    else: 
        print("invalid Choise ID")


main()
        
