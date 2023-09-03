# Ask the user to enter a number
user_input = float(input("Enter a number: "))

# Define a lambda function to add 25 to a number
add_25 = lambda x: x + 25

# Use the lambda function to add 25 to the user's input
result = add_25(user_input)

# Print the result
print("Result after adding 25:",int(result))
