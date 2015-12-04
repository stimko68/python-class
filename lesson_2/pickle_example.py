"""
Examples of how to use the pickle library to save arbitrary data for simple
tasks that don't require the use of a full database

NOTE: make sure to use binary mode when reading/writing to pickle files
      since you may not know the encoding used on the original file

Pickle reference: https://docs.python.org/2/library/pickle.html
"""
import pickle
from pprint import pprint

##############################################################################################
# - Saving data to a pickle file ---------------------------------------------------------- #
##############################################################################################
# Create the data to be pickled
death_star_requirements = {
    'shape': 'sphere',
    'size': 'small moon',
    'weapons': 'planet-killing laser',
    'weaknesses': ['thermal exhaust port', 'stormtroopers with poor aim'],
}

# Create the output file to save the data
pickle_file = open('death_star_plans.pkl', 'wb')

# Write the data to the file
pickle.dump(death_star_requirements, pickle_file)

# Close the file handle
pickle_file.close()

##############################################################################################
# - Retrieving data from a pickle file ----------------------------------------------------- #
##############################################################################################
# Create the file handle
pickle_file = open('death_star_plans.pkl', 'rb')

# Load the pickled data
data = pickle.load(pickle_file)
pprint(data)

# Close the file
pickle_file.close()