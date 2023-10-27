import os

####################################################################################
# Working with built in python functions
####################################################################################

### .split() ###
# Using the .split() function, split the following sentence into individual words:

sentence = "Hello I hope you have a great day!"

# Store your results as a variable split_sentence

split_sentence = 

# What type of variable is split_sentence? 



# Print the last word in the split_sentence list

print()



### .strip() ###
# Using the .strip() function, remove the whitespace from the following sentence:

ws_sentence = "  Hello I hope you have a great day! \t\t   "

# Store your stripped sentence string as a variable stripped_ws

stripped_ws = 
prit(stripped_ws)

# What type of variable is stripped_ws? 

# Print the last character of stripped_ws


## Note: .rstrip() is frequently used to remove only trailing whitespace at the end of the string ##

### .startswith() ### 

# For the following lines of a fasta file, check if the first line starts with '>' using .startswith()

fasta_lines = ['>Homo_sapiens\n', 'ATCTAGGATTACATATTCATCAGTGAC\n', '>Pan troglodytes\n', 'ATCTAGGACTACATATTCATCAGAGAC\n', '>Gorilla gorilla\n', 'ATCTAGAATTACATACTCATCAGTGAC\n']

# Using a for loop, store each line that start with '>' in the variable species_names. Then remove trailing newline character.
# Replace text in #* *# with your code

for l, line in enumerate(fasta_lines):
	if #*your code here, check if species *# :
		species_name = line
		#*your code here, remove trailing newline character here*#
		print(species_name)

### .replace() ###
# Using .replace() replace the occurances of cat with CAT:

to_replace = "My cat is 6 years old. She is the best cat ever." 



####################################################################################
# Working with file paths and os
####################################################################################

### os module ### 
# Use find the current working directory (aka the directory where this file is stored) using the os module. Google how to do this.

cwd = 
print(cwd)

# Use os.path.join() to store the path for folder "new_folder" inside of the current working directory (cwd)
# Note: this command does not make a folder, it just stores a string for a folder that already exists # 

new_folder_path = os.path.join()
print(new_folder_path)

# The following command is a linux (aka bash) command that works like python's print() command. Say we want to print 'Hello world!'
# echo Hello world! 

# You can use os.system() to run linux commands in python. But they must be read as strings. Try running the linux command 'echo Hello world!' in python using os.system()




####################################################################################
# Working with files
####################################################################################

### Reading a file with open(, 'r') ###
# One way to read in a file is to use 'with open' for example:

#with open(`path_to_file`, 'r') as f:
#	lines = f.readlines()
#
#Or another method:
#
#with open (`path_to_file`, 'r') as f:
#	text = f.read()

# We use 'r' to read in a file. Using 'r' will not change the contents of a new file.

# Read in the fasta file stored in the new_folder using both the readlines() and read() method. Print lines and text variables and compare the difference. 
# Define the file path for the fasta file (hint: think of previous commands we learned)

file_path = 

with open(#* file_path, read_the_file*#) as f:
	#* use readlines() *#
print()

with open(#* file_path, read_the_file*#) as f:
	#* use read() *#
print()


### Writing a file with open(,'w') ### 

# Similar to reading a file we can create a new file also using 'with open' . 
# When you open a file to write it, this action immediately deletes the entire contents of the file for you to write new text
# For this reason, we often create a new file if we want to modify an existing file. 
# We already opened the fasta file using readlines, so we will write those lines into a new file

# To write a new file, we use use following format:

#with open(`path_to_file`, 'w') as f:
#	f.write("some text to store in file")
#
#with open(`path_to_file`, 'w') as f:
#	f.writelines("some text to store in file")

# First, define our file path to our new fasta file. Lets call this new fasta: new_fasta.fasta
# Lets keep this new_fasta.fasta in the same new_folder as our old fasta file

new_fasta_path = 

# Write the file using .write() (not .writelines()). Use the contents of our original fasta file that you got from this part:
### with open(#* file_path, read_the_file*#) as f:
###		#* use read() *#


with open(#*path_to_new_fasta*#, 'w') as file:
	#* write new_fasta here*#


# After running this part, look at the file you created

# Now lets try writing the file using the lines you gathered from .writelines(), (from this part):
### with open(#* file_path, read_the_file*#) as f:
### 	#* use readlines() *#


# Define a second new file path
new_path_lines = 

with open(#*path_to_new_fasta*#, 'w') as file:
	for l, line in enumerate(#* list of lines from 113*#):
		#* write new_fasta here*#


####################################################################################
# Working with dictionaries and lists
###################################################################################

# Python dictionaries and lists are used to store many things in one variable. They can even be different types.
# for example: 
# example_list = ['first_name', 'last_name', 'age']

# make a list that stores 3 items: your first name, your last name, and your age

my_list = 

# Add one more item to your list using the .append() function. The syntax for .append() is:
# list.append(new_item)

# Add your pet's name to your list using .append()

#your code here#
print(my_list)

# Print the last item of your list

print()

# We also use dictionaries for storing information in python. These are similar to lists but are identified using keys instead of indexes
# For example:
# example_dict = {"First" : "Jane", "Last" : "Doe", "Age" : 30}

# Make a dictionary called your_name_dict, similar to example_dict

your_name_dict = 
print(your_name_dict)

# To add an item to the dictionary we do that by defining a new key. For example:
#example_dict['month'] = 'January'
# Try adding a new item called 'list' to your_name_dict, where list is my_list from before

#* your code here*#
print(your_name_dict['list'])


####################################################################################
# Defining functions
###################################################################################

# In python we can define a function if we are going to use the same process multiple times
# This makes our code cleaner

# To define a function:

#def my_function(arg1, arg2):
#	contents_of function

# To run the function:
# my_function(your_arg1, your_arg2)

# inside of my_function you can see we have optional arguments. These arguments act as our inputs for the function. 
# There can be as many or as little arguments as you want

# Define a function with no arguments that prints hello world. Then run the function






# Define a function that concatenates "GREAT" at the end of your string and prints your concatenated string.
# Your function should take in 1 argument, which you can call string
# Then run your function 









# Instead of printing we can also use the return command to store results form the function as a variable. 
# For example:

#def my_function(arg1, arg2):
#	contents_of_function
# 	result = new_contents
#	return result

# Define a new function that takes in one argument (a string) and concatenates "THAT'S SO GREAT"  to the end of the string. 
# Instead of printing the results, return the results and store the results in a variable called results 

def new_function_return()
	#*contents here*#

results = new_function_return()
print(results)


####################################################################################
# For loops break statements, continue statements
##################################################################################

### For loops with enumerate ###
# You have seen for loops before, but here is a refresher of the structure when we use enumerate()

# for index, item in enumerate(list):
# 	action_to happen to each item in the for loop

# we can have nested for loops where we loop through two lists at once, just be sure to use unique variable names for each list
# for example
# list1 = ['Jane', 'Doe']
# list2 = ['January', '30']

# for ind_1, item1 in enumerate(list1):
#	print(item1, '\n')
#	for ind_2, item2 in enumerate(list2):
#		print(item2, '\n')

# Notice the indentation! This is very important
# Lets walk through this part. First, define two lists similar to my lists from the example

your_name = 
#just first and last name go above#
your_info = 
# include your month, age, and year born (3 items in this list)

# make a for loop that goes through *just* the list your_name and print each item one at a time





# make a for loop that goes through *just* the list your_info and print each item one at a time







# make a nested for loop that goes through both lists, nesting your_info inside of your_name. 
# print(name, info) inside both nested lists








### break statements ###

# Often times we include break statements when we want to get out of the loop. 
# These break statements are often used as part of conditional if/elif/else statements
#For example, try running the following lines:

# list1 = ['Jane', 'A.' 'Doe']
# list2 = ['January', '1', '1993']

# for ind_1, item1 in enumerate(list1):
#	if item1 == "A.":
#		break
#	else:
#		print(item1)

# for ind_1, item1 in enumerate(list1):
#	print(item1, '\n')
#	for ind_2, item2 in enumerate(list2):
#		if item2 == "27"
#			break
#		else:
#			print(item2, '\n')

# by running the example above, we can see that the break statements breaks out of the innermost for loop, and continues on with any outer for loops
# (we broke out of our list2 for loop but continued with list1 for loop. Because of this, we started over the list2 for loop. 

# try make a break statement yourself.

# 1. define a list of your family names (at least 4 people), with your name second to last in the list 

family_names = 

# 2. define a list of your family ages, that correspond to the ages of each family member from family names
# if you don't know their age that's okay, just guess. 
# This should be a list of integers, not a list of strings

family_ages = 

# 3. set up a nested for loop that 
# a. first loops through your family_names (the outermost list)
# b. then loops through your family_ages (the innermost list)
# c. then inside of both lists, print(name, age) (this will not be a list of peoples ages and names, it will be everyones age for each name)












# 4. copy and paste your for loop from above, but now we will add a conditional
# Inside of both for loops, add the conditional:
# if the name is Kat, break out of the innermost for loop
















#YAY! Now lets try contiue statements
### continue statements ### 
# Continue statements are often used when you just want to skip the current iteration in our for loop
# for example, try running the following code:

# list1 = ['Jane', 'A.' 'Doe']
# list2 = ['January', '1', '1993']

# for ind_1, item1 in enumerate(list1):
#	if item1 == "A.":
#		continue	
#	else:
#		print(item1)

# do you notice how this is different from the break statment? 

# copy and paste your nested for loop from part 4 of break statments
# replace the break statement with a continune statement





















####################################################################################
# List and dictionary comprehension
####################################################################################

# In python there is a way to combine for loops with making a list. This is called list composition. Here is an example:
# Say you have a list, example
# example = ['Jane', 'A.', 'Doe']

# Now lets use list comprehension to define a new list, new_example using the items from example
#new_example = [item for item in example_list]
# print(new_example)

# Writing it this way is the same as the following for loop:
# new_example = []
# for item in example:
#	new_example.append(item)
# print(new_example)

# so we took a three line process and turned it into one. List comprehension works faster than the for loop. 
# but why would we want to duplicate the list in this way? 
# sometimes we might want to do some function to each item in the list. 
# For example, we might want to make the following for loop in list comprehension

# new_example = []
# for item in example:
#	to_add = item.upper()
#	new_example.append(to_add)
#print(new_example)

# which becomes:
# new_example = [item.upper() for item in example]

# Try it yourself! Turn the following for loop into list comprehension. First, define a list of strings:
your_list = 

# Now take the following code block:
#your_new_list = []
#for item in your_list:
#	to_add = item + " IS GREAT"
#	your_new_list.append(to_add)

# and instead use list comprehension to make your_new_list !

your_new_list = [#* list comprehension code here *#]
print(your_new_list)

# it's a similar idea for dictionary comprehension. For example:
 
#keys = ['a','b','c','d','e']
#values = [1,2,3,4,5]  
# 
#my_dict = { k:v for (k,v) in zip(keys, values)}  
#print(my_dict)


# lets make a dictionary out of two lists. 
# 1. make a list of family members names, in all lowercase letters. Make the list 5 names long. 

family_names = 

# 2. make a list of family members ages that correspond to their names.

family_ages = 

# 3. create a dictionary using dictionary comprehension. 
# but for each item in family_names- convert the name to uppercase
# and for each item in family_ages- add 7 to the age to make a dictionary of their ages in 2030.

family_dictionary = 
print(family_dictionary)





















