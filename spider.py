# This script creates a spider chart to visualize performance metrics of different machine learning models across various categories.
# ver 1.0.8
# santakd
# imports
import numpy as npy  # type: ignore # Import the NumPy library for numerical computations
import matplotlib.pyplot as plt  # type: ignore # Import Matplotlib for plotting graphs
import time  # type: ignore # Import the time module to measure execution time
import memory_profiler as mem # type: ignore # Import the memory profiler for calculating memory usage
 
# Start memory usage
m1 = mem.memory_usage()

# Start measuring the processing time
t1 = time.process_time()

def create_spider_chart(categories, data, title="Spider Chart"):
    # Creates a spider chart to visualize performance metrics across different categories.
    # Parameters:
    #    categories (list): List of category names to be plotted.
    #    data (list of tuples): Each tuple contains two elements: a list of performance scores and a label for the model.
    #    title (str): Title of the spider chart.
   
    # Determine the number of categories
    num_categories = len(categories) 

    # Generate evenly spaced angles from 0 to 2π for each category
    angles = npy.linspace(0, 2 * npy.pi, num_categories, endpoint=False).tolist()
    
    # Duplicate the first angle to close the polygon
    angles += angles[:1]

    # Create a figure with polar coordinates enabled and set the size to 8x8 inches
    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
    

    for d, label in data:
        values = d + d[:1]
        # Plot a line for each model with solid style and add a legend
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=label)
        
        # Fill the area under the curve for better visualization
        ax.fill(angles, values, alpha=0.25)

    # Set the starting angle of the plot to 90 degrees   
    ax.set_theta_offset(npy.pi / 2)  
    
    # Reverse the direction of the angles
    ax.set_theta_direction(-1)  
    
    # Set the x-ticks with the category names, excluding the last duplicate angle
    plt.xticks(angles[:-1], categories)
    
    # Position the radial labels at the start of each axis
    ax.set_rlabel_position(0)
    
    # Determine the maximum performance score across all models
    plt.yticks([i for i in range(1, max([max(d) for d, _ in data]) + 1)], 
               [str(i) for i in range(1, max([max(d) for d, _ in data]) + 1)], 
               color="grey", size=8)
   
    # Set y-ticks from 1 to the maximum score with integer steps
    plt.ylim(0, max([max(d) for d, _ in data]))
    
    # Set the title of the chart with specified font size and position
    plt.title(title, size=18, color='black', y=1.1)  
    
    # Place the legend outside the plot area at the upper right corner
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15))  
    
    # Display the spider chart
    plt.show()  
    
if __name__ == '__main__':
    
    # Main execution block that sets up and displays the spider chart.
    
    categories = ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"]
    
    # Define the performance scores for each model across all categories
    data = [
        ([8, 6, 7, 9, 6], "GPT 4o"),
        ([7, 8, 6, 8, 9], "DeepSeek R1"),
        ([8, 9, 8, 7, 8], "Claude 3.5 "),
        ([7, 8, 9, 6, 5], "LLama 3"),
        ([9, 6, 7, 8, 7], "Gemini 2"),
        ([6, 7, 9, 7, 8], "Flux"),
        ([8, 5, 7, 9, 7], "phi4"),
        ([9, 7, 8, 9, 8], "Grok3")
    ]
    
    # Generate and display the spider chart with specified parameters
    create_spider_chart(categories, data, title="ML Models Comparison")
    
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
