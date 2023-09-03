# Ask the user to enter a list of integers separated by spaces
user_input = input("Enter a list of integers separated by spaces: ")

# Split the user input into a list of strings and convert them to integers
input_list = [int(x) for x in user_input.split()]

# Define a function to triple a number
def triple(x):
    return x * 3

# Use the map function to triple all the numbers in the list
result_list = list(map(triple, input_list))

# Print the result
print("Triple of list numbers:", result_list)
