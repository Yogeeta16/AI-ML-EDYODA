def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Ask the user to enter a list of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Split the user input into a list of strings and convert them to integers
input_list = [int(x) for x in user_input.split()]

# Call the function and print the result
result = sum_numbers(input_list)
print("Sum of numbers:", result)
