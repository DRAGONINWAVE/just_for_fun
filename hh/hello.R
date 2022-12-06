# library(openxlsx)
# z <- c(1:3, NA)
# z
# ind <- is.na(z)
# ind
# z[is.na(z)] <- 0
# z
# # is.nan()
# # is.finite()
# paste("My", "Job")
# labs <- paste("X", 1:6, sep = " ")
# labs
# # v <- 10:20
# v <- c(1, 2, 3, 4)
# v[-1:-3]
setwd("D:\\piles\\data (1)\\data")
# x <- read.table("Disease.txt", header = T)
# y <- read.csv("Growth.csv")
# all <- merge(x, y)
# write.table(all, "all.csv")
# products <- read.xlsx("products.xlsx")
# products
# Growth <- read.xlsx("Growth.xlsx")
# Growth
typeandday <- read.csv("typeandday.csv")
typeandday
typeandday$type <- as.factor(typeandday$type)
ba.an <- aov(lm(day ~ type, data = typeandday))
summary(ba.an)
