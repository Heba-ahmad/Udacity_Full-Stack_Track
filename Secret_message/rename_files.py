import os
# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
# I'll import os module to use methods like:
# listdir to return a list containing the name of files
# getcwd() to know what path you are currently in and chdir() to change the directory that we are currently running our Python session in
# and rename() to rename our files name
# translate() to delete characters

# Your code here.
def rename():
    
    file_list = os.listdir(r'C:\Users\InfoTech\Desktop\Udacity_Full-Stack_Track\Secret_message\top_secret')
    #print file_list
    cw_d = os.getcwd()
    os.chdir(r'C:\Users\InfoTech\Desktop\Udacity_Full-Stack_Track\Secret_message\top_secret')
    for file_name in file_list: 
        new_file_name = file_name.translate(None, '0123456789')
        print file_name, new_file_name
        os.rename(file_name, new_file_name)
    os.chdir(cw_d)
    print file_list
rename()
