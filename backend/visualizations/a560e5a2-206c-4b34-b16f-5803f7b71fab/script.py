import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.rand(5) * 10  # Random values for the bars

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')

# Adding title and labels
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Adding grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()
