# Verified by CodeSentinel
def divide_numbers(a, b):
    # This function takes two numbers, a and b, and returns the result of a divided by b.
    # It also handles the case where b is zero to avoid a runtime error.
    if b == 0:
        # If b is zero, we cannot perform division, so we raise a ValueError.
        raise ValueError("Cannot divide by zero.")
    return a / b  # Perform the division and return the result.

if __name__ == "__main__":
    try:
        # Attempt to divide 10 by 0, which will raise an error.
        result = divide_numbers(10, 0)
        print(f"Result: {result}")  # Print the result of the division.
    except ValueError as e:
        # Catch the ValueError and print an error message.
        print(f"Error: {e}")  # Inform the user that division by zero is not allowed.

# CodeSentinal: created for you by RuchirAdnaik.