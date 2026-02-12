"""
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
"""

def fahrenheit_to_celsius(fahrenheit):
    try:
        input_temperature = input("Please enter the temperature in Fahrenheit: ")
        # Attempt to convert the input to a float
        fahrenheit = float(input_temperature)
        # Perform the conversion
        celsius = (fahrenheit - 32) * 5 / 9
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Invalid input. Please enter a numeric value for temperature.")
    else:
        # If conversion is successful, print the result
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        # Thank the user for using the application
        print("Thank you for using the weather forecast application.")


# Main program execution
if __name__ == "__main__":
    fahrenheit_to_celsius(0)