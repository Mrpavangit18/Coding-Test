# Task 3: Use python. Use python indentation.  Use comments where needed

# Function to count occurrences of a specific element in a list
def count_occurrences(lst, element):
    # Using the count() method to count occurrences
    count = lst.count(element)
    return count

# Example usage
sample_list = [1, 2, 3, 4, 2, 2, 5, 2, 6]
element_to_count = 2

# Call the function and store the result
occurrences = count_occurrences(sample_list, element_to_count)

# Display the result
print(f"The element {element_to_count} occurs {occurrences} times in the list.")

"""
Output:
The element 2 occurs 4 times in the list.
"""


