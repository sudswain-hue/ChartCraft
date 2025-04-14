# Interactive Scatter Plot using plotly
library(plotly)

# Sample data
x <- rnorm(100)
y <- rnorm(100)

# Generate interactive plot
p <- plot_ly(x = ~x, y = ~y, type = 'scatter', mode = 'markers',
             marker = list(size = 10, color = 'rgba(255, 182, 193, .9)', line = list(color = 'rgba(152, 0, 0, .8)', width = 2))) %>%
  layout(title = "Interactive Scatter Plot - plotly")

# Save as HTML
htmlwidgets::saveWidget(p, "interactive_plot.html", selfcontained = TRUE)
