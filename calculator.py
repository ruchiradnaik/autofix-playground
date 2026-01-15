# Verified by CodeSentinel
def divide_numbers(a, b):
    # This function takes two numbers, a and b, and returns the result of a divided by b.
    # It also handles the case where b is zero to prevent a runtime error (division by zero).
    if b == 0:
        # If b is zero, we raise a ValueError with a descriptive message.
        raise ValueError("Cannot divide by zero.")
    return a / b  # Perform the division and return the result.

if __name__ == "__main__":
    try:
        # Attempt to divide 10 by 0, which will raise an error.
        result = divide_numbers(10, 0)
        print(f"Result: {result}")  # Print the result of the division.
    except ValueError as e:
        # Catch the ValueError and print an error message.
        print(f"Error: {e}")  # Inform the user about the division by zero error.

# CodeSentinal: created for you by RuchirAdnaik.