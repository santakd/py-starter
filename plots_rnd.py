# imports
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import pandas as pd # type: ignore
import numpy as np # type: ignore
import time  # type: ignore # Import the time module to measure execution time
import memory_profiler as mem # type: ignore # Import the memory profiler for calculating memory usage

# Start memory usage
m1 = mem.memory_usage()

# Start measuring the processing time
t1 = time.process_time()

# Set a random seed for reproducibility (optional)
np.random.seed(42)

# Generate random arrays with 5 elements each, between 0 and 1
x1 = np.random.rand(5)
x2 = np.random.rand(5)
x3 = np.random.rand(5)
x4 = np.random.rand(5)
x5 = np.random.rand(5)

# Print the arrays to verify
print("----------------------------------------------------------------")
print("x1:", x1)
print("x2:", x2)
print("x3:", x3)
print("x4:", x4)
print("x5:", x5)
print("----------------------------------------------------------------")

# Create the dataframe with matching elements
x = np.arange(len(x1)) + 1
df = pd.DataFrame({'a': x1, 'b': x2, 'c': x3, 'd': x4, 'e': x5, 'x': x})

# Melt the dataframe for plotting
df_long = df.melt('x')

# Plot using seaborn
ax = sns.barplot(data=df_long, x='x', y='value', dodge=True, hue='variable')

# Show the plot
plt.show()

# Stop measuring the processing time
t2 = time.process_time() 

# End memory usage
m2 = mem.memory_usage()

# Calculate the memory difference    
mem_diff = round(m2[0] - m1[0],8)

# Calculate the time difference
time_diff = round(t2 - t1,8)

# Print the total time taken to execute the program
print("----------------------------------------------------------------")
print(f"It took {time_diff} Secs and {mem_diff} Mb to generate the chart")
print("----------------------------------------------------------------")