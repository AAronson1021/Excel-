#Read the data set in BlackFriday.xlsx into R. Call the loaded data BlackFriday.xlxs  Download BlackFriday.xlxs. Make sure that you have the directory set to the correct location for the data.
library(readxl)
BlackFriday <- read_excel("~/DSCI 302/Week 3/BlackFriday.xlsx")
View(BlackFriday)
head(BlackFriday)

#Find the average of purchase amount using for loop.
sum<- 0
for(idx in c(1:nrow(BlackFriday))){
  sum<- sum + BlackFriday[idx,"Purchase"]
  }
avg<- sum/nrow(BlackFriday)
print(avg)
    
#Find the average of purchase amount using while loop.
sum<- 0
idx<- 1
while(idx<= nrow(BlackFriday)){
  sum<- sum + BlackFriday[idx, "Purchase" ]
idx<- idx + 1}
avg<- sum/nrow(BlackFriday)
print(avg)

#Find the average of purchase amount using repeat loop.
sum<- 0
idx<- 1
repeat{
  sum<- sum+BlackFriday[idx,"Purchase" ]
  idx<- idx + 1
  if(idx > nrow(BlackFriday)){
    break
  }
}
avg<- sum/nrow(BlackFriday)
print(avg)

#Find the average of purchase amount for female shoppers using for loop.
sum<- 0
for(idx in c(1:nrow(BlackFriday))){
  if(BlackFriday[idx, "Gender"] == "F"){
  sum<- sum + BlackFriday[idx,"Purchase"]
  }
}
avg<- sum/nrow(BlackFriday)
print(avg)

#Find the average of purchase amount for female shoppers using while loop.
idx <- 1
sum <- 0
while(idx <= nrow(BlackFriday)) {
  if(BlackFriday[idx, "Gender"] == "F") {
  sum <- sum + BlackFriday[idx, "Purchase"]
}
  idx <- idx + 1
}
avg <- sum / nrow(BlackFriday)
print(avg)

#Find the average of purchase amount for female shoppers using repeat loop.
idx <- 1
sum <- 0
repeat {
  if(idx > nrow(BlackFriday)) {
    break
} 
  else if(BlackFriday[idx, "Gender"] == "F") {
    sum <- sum + BlackFriday[idx, "Purchase"]
}
  idx <- idx + 1
}
avg <- sum / nrow(BlackFriday)
print(avg)

#Find the differences between the average of purchase amount for female and male shoppers.
avg_f <- 0
avg_m <- 0
for(idx in c(1:nrow(BlackFriday))){
  if(BlackFriday[idx, "Gender"] == "F"){
  avg_f<- avg_f + BlackFriday[idx,"Purchase"]
}
  else if (BlackFriday[idx, "Gender"] == "M") {
  avg_m <- avg_m + BlackFriday[idx, "Purchase"]
}
}
avg_f <- avg_f/nrow(BlackFriday)
avg_m <- avg_m/nrow(BlackFriday)
diff <- avg_m - avg_f
print(diff)











