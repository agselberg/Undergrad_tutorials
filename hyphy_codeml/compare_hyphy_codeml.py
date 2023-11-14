#############################################################################################################################
### IN THIS EXERCISE, YOU WILL BE RUNNING HYPHY ON DATA THAT HAS ALREADY BEEN RUN IN CODEML (ANOTHER SIMILAR MODEL) ###
#############################################################################################################################


### Note: throughout this tutorial, I will write comments with three hashtags and will start code for you with as #* 
### As you work through this tutorial, you should uncomment #* 

import os 

### We will be working out of data from a CodeML tutorial, please copy it now with the following shell command:
### git clone https://github.com/abacus-gene/paml-tutorial.git codeml_git_data

### once you have cloned that directory, look through them a bit, but especiallly the subdirectories in:
### codeml_git_data/positive-selection/01_protocol_analyses


### using os modules, store the file path to 01_protocol_analyses as a variable

#*base_dir = 

### look through this directory. Notice we have 
### 1. tree files with extension .tree 
### 2. a sequence alignment file with extension .phy
### 3. directories that were used to run various hypotheses of the branch-site model

### Lets start with the branch-site folder. There are subdirectories inside the branch folder (bird, chicken, etc) 
### We want to get a list of each of these directories. Can you do this with list comprehension? 

#*bs_sub_dirs =

### Now look through these four directories (bird, chicken, duck, duckchicken)
### each of these directories should have a subdirectory called CODEML
### within CODEML, we are going to find one file that ends with .ctl
### this .ctl file contains the parameters for running the codeml model. 
### we will simpy be looking at the parameters to decide which model to compare to hyphy




### I will walk you through this step by step, so only uncomment 1 step at a time 
### run the program before moving to your next step

### STEP 1: SETTING UP YOUR FOR LOOP  ###
### here we set up the for loop to loop through each file. uncomment #* to follow along. 

#*for ind, dir in enumerate(bs_sub_dirs):
	### we are considering the specific directory dir
	#*print(dir)



	### STEP 2: OPENING YOUR CTL FILE ###	
	### from dir, how can we use os.path.join() to create the full path to our .ctl files?
	### use pwd to compare the file paths of each of the control files

	#*ctl_path = 										 
	
	### open your ctl file using ctl_path you just created, and read in the file
	### store the lines as ctl_lines

	#*with open(ctl_path ......
		#*ctl_lines = 



	### STEP 3: GET THE SPECIFIC LINE ON OUR CTL FILES WHERE THE INPUT INFORMATION IS GIVEN
	### look at your ctl files. notice the input for the model is two lines:
	### one that starts with 'seqfile = ' and another that starts with 'treefile = '
	### get the lines that start with seqfile and treefile by using list comprehension

	#*seq_list = 

	#*tree_list = 

	### this is a list, but it is a list of one. get the one item from the list and store it in new variables

	#*seq_line = 

	#*tree_line = 

	#*print(seq_line)
	#*print(tree_line)



	### STEP 4: PARSE OUR LINES TO CLEAN IT UP A BIT
	### using .split() function, we will get the names of our seq and tree files and none of the extra stuff
	### Notice every ctl file has the file path '../../../' before the name of the phy and tree files.
	### we just want the name of the file here, not the path that was used when they ran this with codeml
	### use .split() function to get rid of the file path and everything that comes before it on our seq_line and tree_line variables

	#seq_split_beg = 
	#tree_split_beg = 

	### now what comes after the file names in all of our ctl files? 
	### use the split function again to get rid of everything that comes after the name of our seq and tree files 
	
	#*seq_name = 
	#*tree_name = 



	### STEP 5: OPEN THE TREE FILE AND REPLACE THE LABELING ###
	### Now that we know the name of the tree file, we can open it
	### recall from your previous tutorial when you replaced labeleing #1 with {FOREGROUND}
	### as you did before, open the file tree_name and read in the tree string
	### replace ' #1' with '{FOREGROUND}'
	### write a new file as output that adds the extension '.lab.nwk' (for example, Mx_branch_chicken.tree become Mx_branch_chicken.tree.lab.nwk)
	#*with open( ......)
	
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*
	#*



	### STEP 6: RUN HYPHY'S BRANCH-SITE MODEL (BUSTED!) ###
	### now that we know the name of the input used in codeml, lets do it in hyphy
	### using the following command to run BUSTED:
	### 'hyphy busted --alignment xxx.pml --tree xxx.nwk --output xxx.json' 
	### run hyphy using os.system()
	### for the output file, let it be the dir name name (example: Branchsite_model_chicken) + '.json' in the results directory os.path.join(base_dir, hyphy_bs_results)




	
	
	










