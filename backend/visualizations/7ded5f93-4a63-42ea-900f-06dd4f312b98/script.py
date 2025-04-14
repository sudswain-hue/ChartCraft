import matplotlib.pyplot as plt
import numpy as np

# Generate data
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.rand(5) * 10

# Create bar chart
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.7)
