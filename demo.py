def sum_two_numbers(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b  # Add the two numbers and return the result

# This block runs only if the script is executed directly
if __name__ == "__main__":
    num1 = 5  # First number to add
    num2 = 7  # Second number to add
    result = sum_two_numbers(num1, num2)  # Call the function and store the result
    print(f"The sum of {num1} and {num2} is {result}")  # Print the result to the console