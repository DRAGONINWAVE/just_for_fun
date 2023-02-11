# rate <- c(20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42)
# impurity <- c(8.4, 9.5, 11.8, 10.4, 13.3, 14.8, 13.2, 14.7, 16.4, 16.5, 18.9, 18.5)
# plot(impurity ~ rate)
# reg <- lm(impurity ~ rate)
# abline(reg, col = "red")
# summary(reg)
# par()
# mfrowl <- par(mfrow = c(4, 5))
# for (i in 1:20)
# {
#     plot(c(1:i), main = paste("I'm image: ", i))
# }
# for (i in 1:10) print(i)
# {

# }
# x <- 3
# switch(x,
#     2 + 2,
#     mean(1:10),
#     rnorm(4)
# )
# switch(2,
#     2 + 2,
#     mean(1:10),
#     rnorm(4)
# )
# w <- switch(6,
#     2 + 2,
#     mean(1:10),
#     rnorm(4)
# )
# w

# library(agricolae)
d <- read.csv("D:/piles/1tongjing (1).csv")
x <- d[, -4]
x
