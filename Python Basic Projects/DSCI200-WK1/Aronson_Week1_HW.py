''' 
Week 1  Homework

Instruction: 
1.	Download the “Week1_HW.py” file from Canvas Assignment Week1_HW and save it to your computer. I suggest you to creating a folder named “DSCI 200-Week 1”
2.	Run the software Spyer from the start menu
3.	Change the working directory to the folder  “DSCI 200-Week 1”
4.	Open the python file “Week1_HW.py”
5.	Debug your codes to make sure there is no error
6.	Save the python file 
7.	Submit the python file “Week1_HW.py” in Canvas Assignment Week1_HW
8.	Watch the homework demo video

Questions:
    
'''
#%%
'''
1.	TV Price
A type of 65” LG smart TV is on sale in Walmart. The original price is $780. It is 20% off now. The sales tax is 8.9 %.
a)	Write codes to calculate the amount paid for that TV including tax. Name the amount as TV_Price
b)	Print(‘ The TV is $ {}’.format(TV_Price))
'''
# write your codes below for Question 1 

price=780
discount=.20
tax=.089
TV_Price=price*(1-discount)*(1+tax)
print("The TV is $ {}".format(TV_Price))

#%%
'''
2.	Numbers
Let three numbers be a =301,000, b=5.2, c= 1-2j,
a)	Print the types of the three numbers
b)	Write a as a scientific notation form
c)	Convert a to a float number
d)	Convert b to a integer number
e)	Convert b to a complex number
'''
# write your codes below for Question 2

a=301000
b=5.2
c=1-2j

print(type(a))
print(type(b))
print(type(c))

print("{:.1e}".format(a))

print(float(a))
print(int(b))
print(complex(b))
#%%
'''
3.	Strings
Given a string variable Program =’  Data Science,’ , School= ’ Maryville   University  ‘
a)	Add the two strings Program and School, then name it College
b)	Find the character at position 4 of College. ( remember that the first character has the position 0)
c)	Find the characters from position 4 to 10 of College.
d)	Change the string variable College to upper case and name it College_upper
e)	Change the string variable College to lower case and name it College_lower
f)	Remove the white spaces in the string variable College_upper and name it College_new
g)	Replace ‘DATA’ by ‘ACTUARIAl’ in the string College_new
h)	Splits the string College_new into substrings if it finds instances of the separator ‘,’
i) Find the length of the string variable Program
'''
# write your codes below for Question 

Program = 'Data Science'
School =' Maryville University'
College = Program + School
print(College)

print(College[4])

print(College[4:10])

College_upper = College
print(College_upper.upper())

College_lower = College
print(College_lower.lower())

College_new = College_upper
print(College_new.strip())

print(College_new.replace('Data', 'Actuarial'))

print(College_new.split(',')) 

print(len(Program))           

#%%
'''
4.	Lists
Given a list, my_list=[2, 4, 6 , 8, 2, 2, 2, 10, 12, 'data']
a)	Find the length of my_list
b)	Find the item value at position 0
c)	Find the item values from position 2 to 5 not including position 5
d)	Find the item values from position 2 to the end
e)	Change the value of 8 by 100
f)	Add an item value 200 to the end of my_list 
g)	Insert an item value ‘Python’ at position 3
h)	Remove the last item
i)	Remove the value of ‘data’
j)	Count the number of 2s
k)	Sort the list descending and ascending respectively, where the list a=['Math', 'English', 'Biology']
'''
# write your codes below for Question 4

my_list=[2, 4, 6 , 8, 2, 2, 2, 10, 12, 'data']
print(my_list[0])

print(my_list[2:5])

print(my_list[2:])

my_list[3]=100

my_list.append(200)
print(my_list)

my_list.insert(3,'Python')
print(my_list)

my_list.pop()
print(my_list)

my_list.remove('data')
print(my_list)

J = my_list.count(2)
print(J)

a = ['Math','English','Biology']
a.sort()
print(a)

a.sort(reverse=True)
print(a)


#%%
'''
5.	Tuples
Given a list, my_list=(2, 4, 6 , 8, 2, 2, 2, 10, 12, 'data')
a)	Find the length of my_tuple
b)	Find the item values from position 3 to 7 including position 7
c)	Count the number of 2s
'''
# write your codes below for Question 5

my_list=(2, 4, 6 , 8, 2, 2, 2, 10, 12, 'data')
my_tuple = my_list
print(len(my_tuple))

print(my_tuple[3:8])

my_tuple.count(2)
print(my_tuple)

#%%
'''
6.	Sets
Given a list, my_list={2, 4, 6 , 8, 2, 2, 2, 10, 12, 'data'}
a)	Find the length of my_set
b)	Add one item value 100
c)	Remove the item value of 2

'''
# write your codes below for Question 6

my_list={2, 4, 6 , 8, 2, 2, 2, 10, 12, 'data'}
my_set = my_list
print(my_set)
print(len(my_set))

my_set.add(100)
print(my_set)

my_set.remove(2)
print(my_set)

#%%
'''
7.	Dictionary
Given a list, my_dictionary={'Name':'Joshua', 'City': 'New York', 'Zipcode': 10020 }
a)	Find the length of my_dictionary
b)	Find the value of the key Zipcode
c)	Add an item with key 'State' and value 'NY'
d) Remove the item City
'''
# write your codes below for Question 7

my_dictionary={'Name':'Joshua', 'City': 'New York', 'Zipcode': 10020 }
print(len(my_dictionary))

print(my_dictionary['Zipcode'])

my_dictionary['State']='NY'
print(my_dictionary)

my_dictionary.pop('City')
print(my_dictionary)



