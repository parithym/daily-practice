# A list of numbers
numbers = [3, 6, 2, 10, 8, 4]

# Assume the first number is the biggest 
max = numbers[0]

# Go through each number in the list
for number in numbers:
    # If the current number is bigger than the current max
    if number > max:
        max = number  # Update max to this bigger number

# Print the biggest number found
print(max)


output:
       10

