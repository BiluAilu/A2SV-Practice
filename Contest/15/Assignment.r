
#Quesion number 3

q3<-c(484,433, 494 ,448 ,454, 497, 414, 308, 400, 473,
      483, 495, 464, 456, 470 ,449 ,419, 457, 444 ,446,
      441 ,476 ,301, 401, 474, 436, 477, 441 ,444 ,317,
      450, 460 ,469, 445 ,467, 496, 480 ,477, 443, 303,
      471, 460, 419, 309, 477, 435, 449, 455, 460, 489)
# a

hist(q3,xlab = " The performance of 50 machine",col = "green", border = "black")

#b 
# Artimetic mean
mean(q3)  #442.2
#Standard deviation
sd(q3, na.rm = TRUE)  #50.84872
#c
#median value
median(q3) #454.5

# mode value
#define function to calculate mode
find_mode <- function(x) {
  u <- unique(x)
  tab <- tabulate(match(x, u))
  u[tab == max(tab)]
}

find_mode(x)  #477 460

#Question number 5


Before<-c(48 ,40 ,35 ,46, 35, 42, 31, 40, 28, 26)
After<-c(45 ,42 ,40 ,54, 30 ,52 ,28, 27, 22 ,22)
MeanBefore<-mean(Before)
MeanAfter<-mean(After)

MeanBefore #37.1
MeanAfter #36.2

SdBefore<-sd(Before)
SdAfter<-sd(After)

SdBefore # 7.385421
SdAfter # 11.95175


t=(MeanBefore-MeanAfter)/sqrt((SdBefore)^2/10+(SdAfter)^2/10)
t # 0.2025728
#Then lets find the critical value with the significance of 2% and df=18 (10+10-2)
cv<-qt(0.02,df=18,lower.tail = FALSE)
cv # 2.213703
#Since our t is less than our cv we fail to reject the null hypothesis that there is no difference between the mean typing speeds before and after training at a significance level of 0.021.


#Question number 10


# Create a data frame with the given data
hen_weights <- c(3.3, 3.6, 4.4, 1.2, 3.8, 3.3, 4.6, 4.6, 5.4, 3.5)
feed_intake <- c(43, 46, 45, 46, 50, 46, 48, 49, 46, 47)
data <- data.frame(hen_weights, feed_intake)

# Fit a linear regression model
model <- lm(feed_intake ~ hen_weights, data = data)

# Test the null hypothesis that regression is not significant
summary(model)

# Construct a confidence interval of the regression coefficient
confint(model)

# Compute the coefficient of determination
summary(model)$r.squared





#Question number 11

x<-c( 29, 19, 56 ,58, 21, 15, 59, 47, 41, 11,52)
y<-c(59 ,56, 54 ,28 ,54 ,26, 57 ,75, 40 ,27 ,47)

correlation<-cor(x,y)
correlation #0.2816809

cor.test(x,y)

# # Pearson's product-moment correlation

# data:  x and y
# t = 0.8807, df = 9, p-value = 0.4014
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  -0.3828928  0.7541283
# sample estimates:
#       cor
# 0.2816809
