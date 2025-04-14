library(plotly)

x <- seq(0, 10, length.out = 100)
y <- sin(x)
data <- data.frame(x = x, y = y)

p <- plot_ly(data, x = ~x, y = ~y, type = 'scatter', mode = 'lines',
             line = list(color = 'blue')) %>%
  layout(title = 'Interactive Sine Wave',
         xaxis = list(title = 'X'),
         yaxis = list(title = 'sin(X)'))

print(p)