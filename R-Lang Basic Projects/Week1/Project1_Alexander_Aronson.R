library(readxl)
CarInsurances <- read_excel("R Programming/CarInsurances.xlsx", 
                            sheet = "Data")
View(CarInsurances)
# 2.How many rows in the data set? What do the rows represent?
nrow(CarInsurances)
# The row represent the number of states,along with a row for average, and a header row.
# 3.How many columns in the data set? What do the columns represent? 
ncol(CarInsurances)
# The columns represent the specifiers of the data such as, cost/coverage, and state of data pool.
# 4.Assign the first eight rows of the data set to a variable:  first.eight.rows and print it out using print() function. 
first.eight.rows <- head(CarInsurances,8)
print(first.eight.rows)
# 5.Assign the last five rows of the data set to a variable: five.rows and print it out using print() function. 
five.rows <-tail(CarInsurances,5)
 print(five.rows)
# 6.List all objects in the memory using two methods.
objects()
ls()
# 7.1 What is the mean of MRC (annual premium of Minimum Required Coverage)? 
mean(CarInsurances$MRC)
'or'
summary(CarInsurances$MRC)
# 7.2 What is the mean of FC (annual premium of Full Coverage)? 
mean(CarInsurances$FC)
'or'
summary(CarInsurances$FC)
# 7.3 What is the mean of AD (annual premium differences between MRC and FC)? 
mean(CarInsurances$AD)
'or'
summary(CarInsurances$AD)
