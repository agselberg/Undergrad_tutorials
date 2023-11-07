#########################################################################################
### Script to practice running BUSTED using python
#########################################################################################

### For this script you will practice running hyphy on a series of genes. 
### In this directory, you have subdirectories that each contain a sequence alignment and tree file pair
### you will be running hyphy on each of these genes with their respective tree

### Step 1: get a list of directories in the current directory
### first, assign the current working directory

#*cwd = 

### Next, get a list of the subdirectories in the current working directory. 
### This is a little tough, so I'll write it here for you as list comprehension

#*sub_dirs = [entry for entry in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, entry)]

### To understand what is happening here, turn this list comprehension into a for loop
### save the list as for_dirs and print for_dirs












### Step 2: set up for loop to go through each directory. print the name of each directory




















### Step 3 in the for loop you just created, use os.path.join() to print the full file path and name of:
### 1. the .nwk file in each subdirectory
### 2. the .fa file in each subdirectory
### define the nwk file path as tree_path inside the for loop
### define the fa file path as seq_path inside the for loop



### Step 4: define your results file path (again, use os.path.join() to do this)
### your results should go in cwd, and they should be named directory_name.json
### inside your for loop, us os.path.join() and define a variable called output for this output
### print output in your for loop



### Step 5: in the same for loop you created, run hyphy with the following command:
### 'hyphy BUSTED ---alignment {YOUR .FA FILE WITH FULL FILE PATH HERE} --tree {YOUR TREE FILE WITH FULL FILE PATH HERE} --output {YOUR DEFINED OUTPUT FULL PATH HERE}

