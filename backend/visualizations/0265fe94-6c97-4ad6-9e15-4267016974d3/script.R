# Static Bar Plot using ggplot2
library(ggplot2)

# Sample data
data <- data.frame(
  category = c("A", "B", "C", "D"),
  value = c(23, 17, 35, 29)
)

# Generate plot
p <- ggplot(data, aes(x = category, y = value, fill = category)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  ggtitle("Static Bar Plot - ggplot2")

# Save the plot
ggsave("static_plot.png", plot = p)
