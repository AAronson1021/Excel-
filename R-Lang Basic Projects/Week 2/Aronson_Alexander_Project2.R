library(readxl)
SP500 <- read_excel("SP500.xlsx")
View(SP500)
#2. How many rows are in the data set? How many columns are in the data set?
nrow(SP500)
ncol(SP500)
# There are 1773 rows and 6 columns#

#3. Select the following three columns: SP500, CPI, and Rate.
SP500[,c(2,5,6)]

#4. Select the 10th, 100th, 500th, and 1500th rows.
SP500[c(10, 100, 500, 1500),]

#5. Select all the observations such that SP500 is greater than 2000 or CPI is less than 100.
x<- subset(SP500,(SP500>2000) | (CPI<100))
print(x)

#6. Select the data such that Earnings greater than 50 and Rate less than 3 with columns SP500 and Dividend only.
y<- subset(SP500,(Earnings>50) & (Rate < 3), select = c(SP500, Dividend))
print(y)

#7. Remove the entire column of Rate.
Data.new<- SP500[,-c(6)]
print(Data.new)

#8. Real price is the inflation adjusted price, which is given by the following formula:  
  # Real Price at time t = (SP 500 price at time t)* CPI(t)/CPI(2018.09), where CPI(2018.09) is the latest consumer price index in the data set. Based on formula above, you need to add one more column, RealPrice. 
CPILast<- tail(SP500$CPI,1)
SP500$RealPrice<- (SP500$CPI)*(SP500$CPI/CPILast)
head(SP500)

#9. Real earnings are the inflation adjusted earnings, which is given by the following formula:
  # Real earnings at time t = (earnings at time t)* CPI(t)/CPI(2018.09), where CPI(2018.09) is the latest consumer price index in the data set. Based on formula above, you need to add one more column, RealEarnings. 
CPILast<- tail(SP500$CPI,1)
SP500$RealEarnings<- (SP500$Earnings)*(SP500$CPI/CPILast)
head(SP500)

#10.Price to earnings ratio is given by the following formula: 
  # P/E Ratio = RealPrice/RealEarnings Based on the formula above, please add one more column, PERatio. 
SP500$PERatio<- SP500$RealPrice/SP500$RealEarnings
head(SP500)
