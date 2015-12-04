"""
Examples of how to handle exceptions and raise custom ones
"""
##############################################################################################
# - Handling built-in exceptions ----------------------------------------------------------- #
##############################################################################################
# Trying to access a key that doesn't exist in a dictionary will raise a KeyError
my_dictionary = {}
the_force = 'the_force'
print my_dictionary[the_force]

# Handle the exception using a try block
try:
    print my_dictionary[the_force]
except KeyError:
    print "{} doesn't exist!".format(the_force)

# Similarly, trying to access the wrong index in a list will raise an IndexError
my_list = []
print my_list[1]

# Handle the exception
try:
    print my_list[1]
except IndexError:
    print "That index doesn't exist!"

# If you want the exception's message available to use (say, for logging)
try:
    print my_list[1]
except IndexError as e:
    print e

##############################################################################################
# - Defining custom exceptions ------------------------------------------------------------- #
##############################################################################################
# To define your own exceptions, you need to subclass Exception
# Basic custom exception example
# This allows you to raise your custom exception and pass a custom message
class ForceException(Exception):
    pass

# Define a simple function that will throw the exception so we can catch it
def force_function():
    raise ForceException('The force does exist!')

# Catch the exception and print out the message
try:
    force_function()
except ForceException as fe:
    print fe