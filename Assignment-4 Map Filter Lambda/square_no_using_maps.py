# Ask the user to enter a list of integers separated by spaces
user_input = input("Enter a list of integers separated by spaces: ")

# Split the user input into a list of strings and convert them to integers
input_list = [int(x) for x in user_input.split()]

# Define a function to square a number
def square(x):
    return x ** 2

# Use the map function to square all the elements in the list
result_list = list(map(square, input_list))

# Print the result
print("Square of list elements:", result_list)
