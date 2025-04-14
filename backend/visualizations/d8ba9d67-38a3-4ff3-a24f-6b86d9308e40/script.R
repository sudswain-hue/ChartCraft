
# 3D Scatter Plot using rgl
library(rgl)

# Sample data
x <- rnorm(100)
y <- rnorm(100)
z <- rnorm(100)

# Open 3D device and plot
plot3d(x, y, z, col = "blue", size = 5, type = "s", main = "3D Scatter Plot - rgl")

# Save widget
rglwidget() %>% htmlwidgets::saveWidget(file = "3d_plot.html", selfcontained = TRUE)