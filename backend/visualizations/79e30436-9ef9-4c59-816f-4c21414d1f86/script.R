library(ggplot2)

df <- data.frame(x = c("A", "B", "C"), y = c(3, 7, 2))
ggplot(df, aes(x, y)) + geom_bar(stat = "identity") + ggtitle("Static Bar Chart")
