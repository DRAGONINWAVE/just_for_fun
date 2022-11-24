library(dplyr)
a <- 1
print(a)
sex <- c("M", "F", "M", "F")
# 将一个列表输出不同因子
sexf <- factor(sex)
print(sexf)
levels(sexf)
sex.tab <- table(sexf)
sex.tab
height <- c(174, 165, 180, 171)
m <- tapply(height, sexf, mean)
m
# 快速构建因子向量
b <- gl(3, 5)
b
gl(3, 1, 15)
gl(3, 1, 30)
z <- 1:12
# dim(z) <- c(3, 4)
dim(z) <- c(3, 2, 2)
x <- array(1:12, dim = c(3, 4))
x
z <- matrix(1:15, nrow = 3, ncol = 5, byrow = TRUE)
z
a <- 1:24
dim(a) <- c(2, 3, 4)
a[2, 1, 2] <- 100
a[1, , ]
det(matrix(1:4, ncol = 2))
df <- data.frame(
    Name = c("Alice", "Becka", "James", "Jeffrey", "John"),
    Sex = c("F", "F", "M", "M", "M"),
    Age = c(13, 13, 12, 13, 12),
    Height = c(56.5, 65.3, 57.3, 62.5, 59.0),
    Weight = c(84.0, 98.0, 83.0, 84.0, 99.5)
)
df$Age
df[, 3]
attach(df)
df$d <- Weight / Height
df
detach(df)
# lst <- list(
#     Name = c("Alice", "Becka", "James", "Jeffrey", "John"),
#     Sex = c("F", "F", "M", "M", "M"),
#     Age = c(13, 13, 12, 13, 12),
#     Height = c(56.5, 65.3, 57.3, 62.5, 59.0),
#     Weight = c(84.0, 98.0, 83.0, 84.0, 99.5)
# )
# lst
# as.data.frame(lst)
