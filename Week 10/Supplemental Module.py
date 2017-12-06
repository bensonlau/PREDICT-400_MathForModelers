# MSPA 400 Session 10 Supplemental Python Module 

# This is a supplemental module dealing with letter and limited text analysis.  
# The module and reading assignment are optional.

# Reading Assignment:
#"Think Python" 2nd Edition Chapter 9 (9.1-9.5), Chapter 13 (13.1-13.4)
#"Think Python" 3rd Edition Chapter 9 (pages 97-101),Chapter 13 (pages 147-150)

# Objective:  This program does letter analysis to demonstrate coding with 
# strings, lists, dictionaries and tuples.  For loops, functions and counters 
# are used. The program uses letter frequency analysis to illustrate the notions
# of statistical independence, dependence plus conditional probabilities.   


# This is a list of the alphabet to be used later.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

#This is an arbitrary string for analysis.  

string = 'thisthesmallregardharrietwhichknightleysitmostthingstruex'

# find() is a search and counting function which will match letter strings
# in the specified file against supplied string "letters" and do a count.

def find(letters,file):  
    count = 0
    for element in file:
        if element == letters:
            count = count + 1
    return count

# The following code searches the string supplied above for each letter in
# the alphabet and places the count of each letter found in a dictionary.
# The dictionary uses the letter found as a key to point at the count 
# determined for that letter in the string supplied.  The total count is 
# accumulated to compute probabilities.
    
d=dict()
total = 0  
for letter in alphabet:       
    count = find(letter, string)
    d[letter] = count
    total = total + count

# Now we can calculate the relative frequencies of occurrence and do various
# calculations.  The dictionary is useful since the key points at a count.
# The following print statements show the flexibility that is possible.

total = float(total)
print ("Probability of t = %r"  %round(d['t']/total,4))
print ("Probability of h = %r"  %round(d['h']/total,4))
product = (d['t']/total)*(d['h']/total)
print ("Product of the two probabilities = %r" %(round(product,4)))

# Creat a list of sequential pairs of characters from the string.
# Each pair is formed by concatenation of string elements and placed
# in the list, lpairs. Concatenation does not combine duplicate pairs 
# into a single element.  They are listed separately as found. 

lpairs = []
sum = 0.0
for index in range(0,len(string)-1):
    pair = string[index]+string[index+1]  # Concatenate to form the pair.
    lpairs = lpairs + [pair]              # Add to the list of pairs.
    sum = sum + 1                         # Count the total number.
    
# The find() function can be used on pairs. It works with strings.
# The relative frequency of joint occurrence is printed out. What follows
# is an example using the letters "t" and "h".

pair = 'th'
pair2 = 'ht'
count = find(pair,lpairs)+find(pair2,lpairs)
print ("Probability of joint occurrence =  %r" %(round(count/sum,4)))

#Conditional probabilities
print ("Probability h given t = %r" %(round((count/sum)/(d['t']/total),4)))
print ("Probability t given h = %r" %(round((count/sum)/(d['h']/total),4)))

# Tuples can be created from a dictionary and vice versa.
# Tuples are immutable and sometimes used as dictionary keys.

t = d.items()
new_d = dict(t)

# A string can be converted to a tuple, and the tuple used for searching.
# Tuples are immutable. Once defined, they can not be changed.

print ('\nThe string below will be converted to a tuple.\n')
print (string)

t = tuple(string)
print ('\nWhat follows is a tuple constructed from the string above.\n')
print (t)

# This demonstrates how a tuple can be used with the find() function.
print ("\nThe count of the letter 'i' in the tuple equals %r" %find('i',t))