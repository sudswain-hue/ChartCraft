library(ggplot2)

# Create sample data
data <- data.frame(
  category = c("A", "B", "C", "D", "E"),
  value = runif(5) * 10
)

# Create bar chart
p <- ggplot(data, aes(x = category, y = value)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Simple Bar Chart", x = "Categories", y = "Values") +
  theme_minimal()

# Display the plot
print(p)
