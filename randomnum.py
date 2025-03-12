import random

# Set the range of the random numbers to be generated
start_range = 10**9
end_range = (10**10)-1

# Generate 12 random numbers and store them in a list
random_numbers0 = [random.randint(start_range, end_range) for _ in range(12)]

# Print the list of random numbers
print(random_numbers0)

# Generate 12 random numbers and store them in a list
random_numbers1 = [random.randint(start_range, end_range) for _ in range(12)]

# Print the list of random numbers
print(random_numbers1)
