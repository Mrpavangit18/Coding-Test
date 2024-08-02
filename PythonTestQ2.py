# Task 2: Write a Python function to reverse a string.

# Function to reverse a string
def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage
original_string = "It is Data Analytics"
reversed_string = reverse_string(original_string)

# Display the original and reversed strings
print("Original String:", original_string)
print("Reversed String:", reversed_string)


