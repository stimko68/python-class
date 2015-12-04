"""
Simple file I/O examples
"""
##############################################################################################
# - Reading Files -------------------------------------------------------------------------- #
##############################################################################################
# How to open a file
file_handle = open('captains.txt', 'rb')

# Read the entire file into a single string
file_handle.read()

# Read the entire file into a list object
file_handle = open('captains.txt', 'rb')
file_handle.read().split('\n')

# Same thing with shorter command
file_handle = open('captains.txt', 'rb')
file_handle.readlines()

# Read one line at a time
file_handle = open('captains.txt', 'rb')
file_handle.readline() # Read the first line
file_handle.readline() # Read the second line, etc

# Close the file
file_handle.close()

# Better syntax for reading a file
# Using the with keyword will automatically close the
# file handle when the block exits
with open('captains.txt', 'rb') as file_handle:
    captains = file_handle.readlines()

print captains

##############################################################################################
# - Writing to Files ----------------------------------------------------------------------- #
##############################################################################################
# Create a new file
# Using 'w' here will overwrite an existing file of the same name
new_file = open('new_file.txt', 'wb')

# Write a string to it
new_file.write("I'm a new line!\n")

# Write a list of strings to it
# Don't forget the newline characters!
new_lines = ["I'm another new line!", 'Here is some more text', 'Even more text']
new_text = '\n'.join(new_lines)
new_file.write(new_text)

# Close the file
new_file.close()

# Better way to do the same thing
new_file_lines = ["I'm a new line!", "I'm another new line!", 'Here is some more text', 'Even more text']
with open('new_file.txt', 'wb') as new_file:
    new_text = '\n'.join(new_file_lines)
    new_file.write(new_text)

# Append to an existing file
with open('new_file.txt', 'ab') as existing_file:
    existing_file.write("\nI'm an appended line!")