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

# Define the arrays
x1 = np.array([0.05, 0.22, 0.32, 0.45, 0.55])
x2 = np.array([0.11, 0.23, 0.54, 0.74, 0.81])
x3 = np.array([0.12, 0.24, 0.55, 0.92, 0.83])
x4 = np.array([0.07, 0.26, 0.56, 0.75, 0.89])
x5 = np.array([0.22, 0.27, 0.59, 0.77, 0.93])

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