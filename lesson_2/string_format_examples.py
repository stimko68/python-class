##############################################################################################
# - Old Style (similar to sprintf) --------------------------------------------------------- #
##############################################################################################
## https://docs.python.org/2/library/stdtypes.html#string-formatting
# String replacement
print 'Laugh it up, %s!' % 'fuzzball'
print 'Why, you %s, %s, %s %s!' % ('stuck up', 'half-witted', 'scruffy-looking', 'nerf herder')

# Integers
print 'This is the ship that completed the Kessel run in %d parsecs' % 12

# Floats
print 'Actually it was more like %f parsecs' % 12.11
print 'Really it was more like %.2f parsecs' % 12.11

# Using values from a dictionary
source = {
    'noun1': 'apple',
    'verb': 'throws',
    'noun2': 'banana',
    'number': 10,
}
print "This %(noun1)s %(verb)s just like a %(noun2)s! I'll take %(number)d of them!" % source

##############################################################################################
# - New Style String Formatting ------------------------------------------------------------ #
##############################################################################################
## https://docs.python.org/2/library/string.html#format-string-syntax
# String replacement
print 'Laugh it up, {}!'.format('fuzzball!')
print 'Why, you {}, {}, {} {}!'.format('stuck up', 'half-witted', 'scruffy-looking', 'nerf herder')

# Reusing strings
print '{0}{1}{2}{1}{0}'.format('R', 'A', 'D')

# Integers and Floats
print 'This is the ship that completed the Kessel run in {} parsecs'.format(12)
print 'Actually it was more like {} parsecs'.format(12.11)
print 'Really it was more like {:.4f} parsecs'.format(12.11)
print 'The odds of surviving are {:,} to 1!'.format(3720)

# Using values from a dictionary
source = {
    'noun1': 'apple',
    'verb': 'throws',
    'noun2': 'banana',
    'number': 10,
}
print "This {noun1} {verb} just like a {noun2}! I'll take {number} of them!".format(**source)

# Formatting dates
## https://docs.python.org/2/library/datetime.html#datetime-objects
from datetime import datetime
d = datetime.now()

print 'The current date is {:%B %d, %Y}'.format(d)
print 'The current timestamp is {:%Y-%m-%d %H:%M:%S}'.format(d)