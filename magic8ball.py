import random
import time

answers = [
    "Yes, definitely!",
    "No way, buddy.",
    "Maybe... maybe not.",
    "Ask again later.",
    "Hmm, I'm not sure.",
    "The answer is unclear.",
    "It's a yes.",
    "It's a no."
]

print("")
print("Welcome to the Magic 8-Ball!")
question = input("Ask your question: ")

# Start time
start_time = time.process_time()

# Generate a random answer
random_answer = random.choice(answers)
print(random_answer)

# End time
end_time = time.process_time()

# Calculate differences
time_diff = round(end_time - start_time, 8)

print("")
print("----------------------------------------------------------------")
print(f"It took {time_diff} seconds to generate the answer")
print("----------------------------------------------------------------")
print("")