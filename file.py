def multiply_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their product.
    """
    result = num1 * num2
    return result

def add_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    """
    result = num1 + num2
    return result

def perform_operations(num1, num2):
    """
    This function performs multiplication and addition using the results
    of the multiply_numbers and add_numbers functions.
    """
    # Call the multiply_numbers function
    product = multiply_numbers(num1, num2)

    # Call the add_numbers function
    summation = add_numbers(num1, num2)

    # Return the results
    return product, summation

# Test Cases for perform_operations function
def test_perform_operations():
    # Test Case 1: Positive numbers
    result = perform_operations(3, 4)
    assert result == (12, 7), f"Test Case 1 failed: expected (12, 7), got {result}"

    # Test Case 2: Negative numbers
    result = perform_operations(-2, 6)
    assert result == (-12, 4), f"Test Case 2 failed: expected (-12, 4), got {result}"

    # Test Case 3: Zero and positive number
    result = perform_operations(0, 9)
    assert result == (0, 9), f"Test Case 3 failed: expected (0, 9), got {result}"

    # Test Case 4: Zero and negative number
    result = perform_operations(0, -5)
    assert result == (0, -5), f"Test Case 4 failed: expected (0, -5), got {result}"

# Run the test cases
test_perform_operations()
