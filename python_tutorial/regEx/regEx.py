# RegEx
# A sequence of characters that forms a search pattern.
# Can be used to check if a string contains the specified search pattern.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
print(x)

print()

# The findall() function
# Returns a list containing all matches.
txt = " The rain is Spain"
x = re.findall("ai", txt)
print(x)

print()

txt = "The rain in Spain"
x = re.findall("Portugal", txt)

print(x)

print()

# The search() function
# The search() function searches the string for a match, and returns a match object
# if there is a match.
# If there is more than one match, only thr first occurence of the match will be 
# returned.
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:" , x.start())

print()

# Example: make a search that retuns no match:
txt = "Train in Spain"
x = re.search("Portugal", txt)

print(x)

print()

# The split() function
# Returns a list where the string has been split at each match:
txt = "The rain is Spain"
x = re.split("\s", txt)

print(x)

print()

# You can contro the number of occurences by specifying the maxsplit parameter:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)

print(x)

print()

# The sub() function
# Replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)

print(x)

print()

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)

print(x)

print()

# Match object
# Contains information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match 
# Object
txt = "The rain in Spain"
x = re.search("ai", txt)

print(x)

print()

# Example
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

print(x.span())

print()

# Example:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

print(x.span())

print()

# Example:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

print(x.group()) 
