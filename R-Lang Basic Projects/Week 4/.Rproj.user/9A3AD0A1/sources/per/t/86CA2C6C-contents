loan <- read.csv("~/DSCI 302/Week 4/loan.csv")
View(loan)
#######spacer#######################################################################################################################################################

1.#Read the dataset in loan.csv  Download loan.csvinto R. Call the loaded data, loan. Make sure that you have the directory set to the correct location for the data. 
2.#Which variables (columns) are continuous/numerical variables? Which columns are factors (categorical variables)?' 
3.#Calculate the minimum, maximum, mean, median, standard deviation and three quartiles (25th, 50th and 75th  percentiles) of loan_amnt.'' 
4.#Calculate the minimum, maximum, mean, median, standard deviation and three quartiles (25th, 50th and 75th  percentiles) of int_rate. 
5.#Calculate the correlation coefficient of the two variables: int_rate and installment. Do they have a strong relationship? 
6.#Calculate the frequency table of term? What’s the mode of term variable? 
7.#Calculate the proportion table of loan_status? What’s the mode of loan_status variable? 
8 #Calculate the cross table of term and loan_status. Then produce proportions by row and column respectively.
9.#The data is stored in the data frame, loan. Please summarize all the variables using one command.' 

#######spacer#########################################################################################################################################################

#Question 2#
str(loan)
c<- sapply(loan,is.numeric)
which(c)
ch<- sapply(loan,is.character)
which(ch)
f<- sapply(loan,is.factor)
which(f)
# Indices that are considers numeric/continuous are 1,2,3,5, & 9. Whereas, the indices that are factors(characters in this case) are 3,6,7,8,10 & 11#

#Question 3#
is.numeric(loan$loan_amnt)
class(loan$loan_amnt)
min(loan$loan_amnt)
max(loan$loan_amnt)
mean(loan$loan_amnt)
median(loan$loan_amnt)
sd(loan$loan_amnt)
quantile(loan$loan_amnt, probs=c(.25,.50,.75))

#Question 4#
is.numeric(loan$int_rate)
class(loan$int_rate)
min(loan$int_rate)
max(loan$int_rate)
mean(loan$int_rate)
median(loan$int_rate)
sd(loan$int_rate)
quantile(loan$int_rate, probs=c(.25,.50,.75))

#Question 5#
cor(loan$int_rate,loan$installment)
# There is not a strong correlation due to its value being closer to zero than it is to one#

#Question 6#
is.numeric(loan$term)
class(loan$term)
loan$term<- as.factor(loan$term)
table(loan$term)
names(sort(-table(loan$term)))[1]
# The mode is 36 months#

#Question 7#
is.numeric(loan$loan_status)
loan$loan_status<- as.factor(loan$loan_status)
prop.table(table(loan$loan_status))
names(sort(prop.table(table(loan$loan_status))))[1]
# The mode of the Table is Charged off #

#Question 8#
loan$loan_status<- as.factor(loan$loan_status)
loan$term<- as.factor(loan$term)
xtab.term.loan_status<-xtabs(~term + loan_status, data=loan)
prop.table(xtab.term.loan_status, margin=1)
prop.table(xtab.term.loan_status, margin=2)

#Question 9#
loan$grade<- as.factor(loan$grade)
loan$emp_length<- as.factor(loan$emp_length)
loan$home_ownership<- as.factor(loan$home_ownership)
loan$annual_inc<- as.factor(loan$annual_inc)
loan$verification_status<- as.factor(loan$verification_status)
str(loan)
summary(loan)