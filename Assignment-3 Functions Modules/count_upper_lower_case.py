def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Ask the user to enter a string
user_input = input("Enter a string: ")

# Call the function to count upper and lower case letters
upper_count, lower_count = count_upper_lower(user_input)

# Print the results
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)
